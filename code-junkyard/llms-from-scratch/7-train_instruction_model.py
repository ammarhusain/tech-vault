#!/usr/bin/env python3
"""
Training script for instruction fine-tuning with LoRA or full model training.

Usage:
    python train_instruction_model.py lora
    python train_instruction_model.py full
"""

import argparse
import json
import math
import time
from copy import deepcopy
from functools import partial

import torch
from torch.utils.data import Dataset, DataLoader
import tiktoken

from llms_from_scratch_utils import (
    GPT_355M_FILE,
    GPT_MODEL_CONFIGS,
    BASE_GPT_CONFIG,
    PATH_PREFIX,
    train_model_simple,
    generate,
)
from llms_rasbt_repo import GPTModel


# ============================================================================
# Dataset preparation
# ============================================================================

def load_file(file_path):
    """Load JSON data from file."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def format_input(entry):
    """Format instruction data entry into prompt format."""
    instruction_text = (
        f"Below is an instruction that describes a task. "
        f"Write a response that appropriately completes the request."
        f"\n\n### Instruction:\n{entry['instruction']}"
    )
    input_text = f"\n\n### Input:\n{entry['input']}" if entry["input"] else ""
    return instruction_text + input_text


class InstructionDataset(Dataset):
    """Dataset for instruction fine-tuning."""

    def __init__(self, data, tokenizer):
        self.data = data
        self.encoded_texts = []

        for entry in data:
            instruction_plus_input = format_input(entry)
            response_text = f"\n\n### Response:\n{entry['output']}"
            full_text = instruction_plus_input + response_text
            self.encoded_texts.append(tokenizer.encode(full_text))

    def __getitem__(self, index):
        return self.encoded_texts[index]

    def __len__(self):
        return len(self.data)


def custom_collate_fn(
    batch,
    pad_token_id=50256,
    ignore_index=-100,
    allowed_max_length=None,
):
    """Custom collate function for batching variable-length sequences."""
    batch_max_length = max(len(item) + 1 for item in batch)
    inputs_lst, targets_lst = [], []

    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        padded = new_item + [pad_token_id] * (batch_max_length - len(new_item))

        inputs = torch.tensor(padded[:-1])
        targets = torch.tensor(padded[1:])

        # Replace padding tokens in targets with ignore_index
        mask = targets == pad_token_id
        indices = torch.nonzero(mask).squeeze()
        if indices.numel() > 1:
            targets[indices[1:]] = ignore_index

        if allowed_max_length is not None:
            inputs = inputs[:allowed_max_length]
            targets = targets[:allowed_max_length]

        inputs_lst.append(inputs)
        targets_lst.append(targets)

    inputs_tensor = torch.stack(inputs_lst)
    targets_tensor = torch.stack(targets_lst)

    return inputs_tensor, targets_tensor


def generate_and_save_responses(model, test_data, model_name, max_new_tokens=250):
    """
    Generate model responses for test data and save to JSON file.

    Args:
        model: The trained model
        test_data: List of test data entries
        model_name: Name of the model (used in output filename)
        max_new_tokens: Maximum tokens to generate per response

    Returns:
        Path to the saved JSON file
    """
    test_data_with_responses = []

    for entry in test_data:
        input_txt = format_input(entry)
        generated_text = generate(
            model=model,
            start_context=input_txt,
            max_new_tokens=max_new_tokens,
            context_size=1024,
            eos_id=50256
        )

        response_text = (
            generated_text[len(input_txt):]
            .replace("### Response:", "")
            .strip()
        )

        entry_with_response = entry.copy()
        entry_with_response['model_response'] = response_text
        test_data_with_responses.append(entry_with_response)

    # Save test responses
    test_responses_file = f"{PATH_PREFIX}{model_name}_responses.json"
    with open(test_responses_file, 'w', encoding='utf-8') as f:
        json.dump(test_data_with_responses, f, indent=4, ensure_ascii=False)

    return test_responses_file


# ============================================================================
# LoRA implementation
# ============================================================================

class LoRALayer(torch.nn.Module):
    """Low-Rank Adaptation layer."""

    def __init__(self, in_dim, out_dim, rank, alpha):
        super().__init__()
        self.A = torch.nn.Parameter(torch.empty(in_dim, rank))
        torch.nn.init.kaiming_uniform_(self.A, a=math.sqrt(5))
        self.B = torch.nn.Parameter(torch.zeros(rank, out_dim))
        self.alpha = alpha
        self.rank = rank

    def forward(self, x):
        x = (self.alpha / self.rank) * (x @ self.A @ self.B)
        return x


class LinearWithLoRA(torch.nn.Module):
    """Linear layer with LoRA adaptation."""

    def __init__(self, linear, rank, alpha):
        super().__init__()
        self.linear = linear
        self.lora = LoRALayer(linear.in_features, linear.out_features, rank, alpha)

    def forward(self, x):
        return self.linear(x) + self.lora(x)


def replace_linear_with_lora(model, rank, alpha):
    """Recursively replace all Linear layers with LinearWithLoRA."""
    for name, module in model.named_children():
        if isinstance(module, torch.nn.Linear):
            setattr(model, name, LinearWithLoRA(module, rank, alpha))
        else:
            replace_linear_with_lora(module, rank, alpha)


# ============================================================================
# Main training function
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Train instruction fine-tuned model")
    parser.add_argument(
        "model_type",
        type=str,
        choices=["lora", "full"],
        help="Type of training: 'lora' for LoRA fine-tuning or 'full' for full model fine-tuning"
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=5,
        help="Number of training epochs (default: 5)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=8,
        help="Batch size for training (default: 8)"
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=0.00005,
        help="Learning rate (default: 0.00005)"
    )
    parser.add_argument(
        "--lora-rank",
        type=int,
        default=16,
        help="LoRA rank (default: 16)"
    )
    parser.add_argument(
        "--lora-alpha",
        type=int,
        default=16,
        help="LoRA alpha (default: 16)"
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cpu",
        choices=["cpu", "cuda", "mps"],
        help="Device to train on (default: cpu)"
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="default",
        choices=["default", "alpaca"],
        help="Dataset to use: 'default' for instruction-data.json or 'alpaca' for alpaca_data.json (default: default)"
    )

    args = parser.parse_args()

    print(f"{'='*60}")
    print(f"Training {args.model_type.upper()} model")
    print(f"{'='*60}")

    # Load data
    print("Loading data...")
    if args.dataset == "default":
        file_path = "7-finetuning-data/instruction-data.json"
    else:  # alpaca
        file_path = "7-finetuning-data/alpaca_data.json"

    data = load_file(file_path)
    print(f"Dataset: {args.dataset}")
    print(f"Total entries: {len(data)}")

    # Split data
    train_portion = int(len(data) * 0.85)
    test_portion = int(len(data) * 0.1)
    val_portion = len(data) - train_portion - test_portion

    train_data = data[:train_portion]
    test_data = data[train_portion:train_portion + test_portion]
    val_data = data[train_portion + test_portion:]

    print(f"Train: {len(train_data)}, Test: {len(test_data)}, Val: {len(val_data)}")

    # Setup tokenizer and dataloaders
    tokenizer = tiktoken.get_encoding("gpt2")
    customized_collate_fn = partial(custom_collate_fn, allowed_max_length=1024)

    torch.manual_seed(123)

    train_dataset = InstructionDataset(train_data, tokenizer)
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        collate_fn=customized_collate_fn,
        shuffle=True,
        drop_last=True,
        num_workers=0
    )

    val_dataset = InstructionDataset(val_data, tokenizer)
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        collate_fn=customized_collate_fn,
        shuffle=False,
        drop_last=False,
        num_workers=0
    )

    # Load base model
    print("Loading base GPT-2 Medium (355M) model...")
    BASE_GPT_CONFIG.update(GPT_MODEL_CONFIGS["gpt2-medium (355M)"])
    gpt = GPTModel(BASE_GPT_CONFIG)
    gpt.load_state_dict(torch.load(GPT_355M_FILE, weights_only=True))
    gpt.eval()

    # Prepare model based on type
    if args.model_type == "lora":
        print(f"Preparing LoRA model (rank={args.lora_rank}, alpha={args.lora_alpha})...")
        model = deepcopy(gpt)

        # Freeze all parameters
        for param in model.parameters():
            param.requires_grad = False

        # Add LoRA layers
        replace_linear_with_lora(model, rank=args.lora_rank, alpha=args.lora_alpha)

        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        total_params = sum(p.numel() for p in model.parameters())
        print(f"Trainable parameters: {trainable_params:,} / {total_params:,} ({100*trainable_params/total_params:.2f}%)")

        # Build model name with non-default parameters
        model_name = f"gpt2-medium-355M-lora-{args.dataset}"
        if args.lora_rank != 16:
            model_name += f"-r{args.lora_rank}"
        if args.lora_alpha != 16:
            model_name += f"-a{args.lora_alpha}"
        if args.lr != 0.00005:
            model_name += f"-lr{args.lr}"
        if args.batch_size != 8:
            model_name += f"-bs{args.batch_size}"
        if args.epochs != 5:
            model_name += f"-e{args.epochs}"
    else:
        print("Preparing full model for fine-tuning...")
        model = gpt
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"Trainable parameters: {trainable_params:,}")

        # Build model name with non-default parameters
        model_name = f"gpt2-medium-355M-sft-{args.dataset}"
        if args.lr != 0.00005:
            model_name += f"-lr{args.lr}"
        if args.batch_size != 8:
            model_name += f"-bs{args.batch_size}"
        if args.epochs != 5:
            model_name += f"-e{args.epochs}"

    # Setup optimizer
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=0.1
    )

    # Train model
    print(f"\nStarting training for {args.epochs} epochs...")
    start_time = time.time()

    train_losses, val_losses, tokens_seen = train_model_simple(
        model,
        train_loader,
        val_loader,
        optimizer,
        device=args.device,
        num_epochs=args.epochs,
        eval_freq=5,
        eval_iter=5,
        start_context=format_input(val_data[0]),
        tokenizer=tokenizer
    )

    end_time = time.time()
    execution_time_minutes = (end_time - start_time) / 60
    print(f"\nTraining completed in {execution_time_minutes:.2f} minutes.")

    # Save model
    model_file = f"{PATH_PREFIX}{model_name}.pth"
    torch.save(model.state_dict(), model_file)
    print(f"Model saved as {model_file}")

    # Evaluate on validation sample
    print("\nEvaluating model on sample validation data...")
    model.eval()

    sample_idx = 20 if len(val_data) > 20 else 0
    input_txt = format_input(val_data[sample_idx])

    generated_text = generate(
        model=model,
        start_context=input_txt,
        max_new_tokens=50,
        context_size=1024,
        eos_id=50256,
    )

    response_text = (
        generated_text[len(input_txt):]
        .replace("### Response:", "")
        .strip()
    )

    print(f"\n{'='*60}")
    print("EVALUATION SAMPLE")
    print(f"{'='*60}")
    print(f"Instruction: {val_data[sample_idx]['instruction']}")
    if val_data[sample_idx]['input']:
        print(f"Input: {val_data[sample_idx]['input']}")
    print(f"Expected: {val_data[sample_idx]['output']}")
    print(f"Model Response: {response_text}")
    print(f"{'='*60}")

    # Save training stats
    stats = {
        "model_type": args.model_type,
        "model_name": model_name,
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "learning_rate": args.lr,
        "training_time_minutes": execution_time_minutes,
        "final_train_loss": train_losses[-1] if train_losses else None,
        "final_val_loss": val_losses[-1] if val_losses else None,
        "tokens_seen": tokens_seen,
    }

    if args.model_type == "lora":
        stats["lora_rank"] = args.lora_rank
        stats["lora_alpha"] = args.lora_alpha
        stats["trainable_params"] = trainable_params

    stats_file = f"{PATH_PREFIX}{model_name}_stats.json"
    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=4)
    print(f"\nTraining stats saved to {stats_file}")

    # Generate responses for test data
    print(f"\n{'='*60}")
    print("GENERATING TEST DATA RESPONSES")
    print(f"{'='*60}")
    print(f"Generating responses for {len(test_data)} test examples...")

    test_responses_file = generate_and_save_responses(
        model=model,
        test_data=test_data,
        model_name=model_name,
        max_new_tokens=250
    )

    _ = generate_and_save_responses(
        model=model,
        test_data=val_data,
        model_name=f"{model_name}_val",
        max_new_tokens=250
    )
    _ = generate_and_save_responses(
        model=model,
        test_data=train_data[:100],
        model_name=f"{model_name}_train_100",
        max_new_tokens=250
    )
    
    print(f"Test responses saved to {test_responses_file}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
