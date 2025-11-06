#!/usr/bin/env python3
"""
Analyze model responses using LLM judge via Ollama.

Usage:
    python 7-generate_model_responses.py test_data_with_gpt2-medium-355M-lora-default_responses.json
    python 7-generate_model_responses.py test_data_with_gpt2-medium-355M-lora-default_responses.json --judge-model llama3:8b
"""

import argparse
import json
from pathlib import Path
from tqdm import tqdm

from llms_from_scratch_utils import (
    PATH_PREFIX,
    query_ollama,
)


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


def analyze_model_responses(json_data, judge_model="gpt-oss:20b", ollama_url="http://localhost:11434/api/chat"):
    """Analyze model responses using an LLM judge via Ollama."""
    scores = []
    detailed_results = []

    for entry in tqdm(json_data, desc="Analyzing responses"):
        prompt = (
            f"Given the input `{format_input(entry)}` "
            f"and correct output `{entry['output']}` "
            f"score the model's response `{entry['model_response']}` "
            f"on a scale of 0 to 100, where 0 is the worst and 100 is the best score. "
            f"Your output should be in the following format: Score: <integer> \nRationale: <explanation>"
        )

        try:
            judge_response = query_ollama(prompt, model=judge_model, url=ollama_url)

            # Extract score from response
            score_str = judge_response.split("Score: ")[1].split("Rationale:")[0].strip()
            # Handle various formats like "Score: 85" or "Score: 85."
            score = int(score_str.rstrip('.'))

            rationale = judge_response.split("Rationale:")[1].strip() if "Rationale:" in judge_response else ""

            scores.append(score)
            detailed_results.append({
                "instruction": entry["instruction"],
                "input": entry.get("input", ""),
                "expected_output": entry["output"],
                "model_response": entry["model_response"],
                "score": score,
                "rationale": rationale
            })

        except Exception as e:
            print(f"\nError parsing score for entry: {entry['instruction'][:50]}...")
            print(f"Judge response: {judge_response[:200]}...")
            print(f"Error: {e}")
            # Add a failure entry
            detailed_results.append({
                "instruction": entry["instruction"],
                "input": entry.get("input", ""),
                "expected_output": entry["output"],
                "model_response": entry["model_response"],
                "score": None,
                "rationale": f"Error: {str(e)}",
                "raw_judge_response": judge_response
            })

    return scores, detailed_results


def main():
    parser = argparse.ArgumentParser(
        description="Analyze model responses using LLM judge"
    )
    parser.add_argument(
        "json_filename",
        type=str,
        help="JSON filename with model responses (e.g., test_data_with_gpt2-medium-355M-lora-default_responses.json)"
    )
    parser.add_argument(
        "--judge-model",
        type=str,
        default="gpt-oss:20b",
        help="Ollama model to use as judge (default: gpt-oss:20b)"
    )
    parser.add_argument(
        "--ollama-url",
        type=str,
        default="http://localhost:11434/api/chat",
        help="Ollama API URL (default: http://localhost:11434/api/chat)"
    )

    args = parser.parse_args()

    # Construct full JSON path using PATH_PREFIX
    json_path = Path(PATH_PREFIX) / args.json_filename
    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}")
        print(f"Looking in directory: {PATH_PREFIX}")
        return

    print(f"{'='*60}")
    print(f"Analyzing Model Responses")
    print(f"{'='*60}")
    print(f"JSON file: {json_path.name}")
    print(f"Judge model: {args.judge_model}")
    print(f"Ollama URL: {args.ollama_url}")

    # Load JSON data with responses
    print(f"\nLoading data from {json_path}...")
    json_data = load_file(json_path)
    print(f"Total entries to analyze: {len(json_data)}")

    # Analyze responses
    print(f"\nAnalyzing responses using {args.judge_model}...")
    scores, detailed_results = analyze_model_responses(
        json_data,
        judge_model=args.judge_model,
        ollama_url=args.ollama_url
    )

    # Calculate statistics
    valid_scores = [s for s in scores if s is not None]
    if valid_scores:
        avg_score = sum(valid_scores) / len(valid_scores)
        min_score = min(valid_scores)
        max_score = max(valid_scores)
    else:
        avg_score = min_score = max_score = 0

    # Save detailed results
    json_name = json_path.stem
    output_file = f"{PATH_PREFIX}{json_name}_analysis.json"

    print(f"\nSaving analysis to {output_file}...")
    analysis_output = {
        "summary": {
            "total_entries": len(json_data),
            "successful_scores": len(valid_scores),
            "failed_scores": len(json_data) - len(valid_scores),
            "average_score": avg_score,
            "min_score": min_score,
            "max_score": max_score,
            "judge_model": args.judge_model
        },
        "detailed_results": detailed_results
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_output, f, indent=4, ensure_ascii=False)

    print(f"\n{'='*60}")
    print("Analysis Complete!")
    print(f"{'='*60}")
    print(f"Total entries analyzed: {len(json_data)}")
    print(f"Successful scores: {len(valid_scores)}")
    print(f"Failed scores: {len(json_data) - len(valid_scores)}")
    print(f"Average score: {avg_score:.2f}")
    print(f"Min score: {min_score}")
    print(f"Max score: {max_score}")
    print(f"\nDetailed results saved to: {output_file}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
