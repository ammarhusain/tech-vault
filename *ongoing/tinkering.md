---
created: 2022-10-16-Sunday 21:26
modified: 2024-03-19-Tuesday 11:19
---

%% Begin Waypoint %%
- **[tinkering](*ongoing/tinkering.md)**
	- **attachments**
		- **nanoGPT-code**

		- **picoGPT**
			- **__pycache__**
			- **models**
				- **124M**
			- [[ai-ml/code-junkyard/mcp-weather/README]]

%% End Waypoint %%

- [ ] [[#Raspberry Pi-5]]
- [ ] #goal #_2024 Go through this hacking book: [Ethical Hacking: A Hands-on Introduction to Breaking In: Graham, Daniel G.: 9781718501874: Amazon.com: Books](https://www.amazon.com/Ethical-Hacking-Hands-Introduction-Breaking/dp/1718501870)

# Raspberry Pi-5
[GitHub - rhasspy/piper: A fast, local neural text to speech system](https://github.com/rhasspy/piper)
- Could also use ElevenLabs to train a TTS model on my own voice - subscription is a bit expensive but could be a cool gadget ($5/mo)
- [ ] #tinker #goal #_2024 - Build an arduino + raspberry pi based system where the arduino is hooked on to an LED display matrix + microphone while the raspberry pi runs an llama model + a diffusion model + a whisper model for speech transcription.
## Tasks
- [ ] setup whisper notebook where you can also speak to record audio
	- [A Weekend AI Project: Running Speech Recognition and a LLaMA-2 GPT on a Raspberry Pi | by Dmitrii Eliuseev | Jan, 2024 | Towards Data Science](https://towardsdatascience.com/a-weekend-ai-project-running-speech-recognition-and-a-llama-2-gpt-on-a-raspberry-pi-5298d6edf812)

- [x] setup ddns client on rpi5 - dynu (has custom dns) or duckdns ✅ 2023-12-15
	- This [ChatGPT session](https://chat.openai.com/c/5ea1a336-1c9a-43f6-a085-1c1b0b4646d7) has all the steps - pretty easy to do. Used duckdns just easy that way
- [x] install cooling case on rpi5 ✅ 2024-01-21

[[2023-12-19-Tuesday]]
Installed cooling case in the office. Simple command to run a model from ~/llama.cpp directory: `./main -m models/openorca-platypus2-13b.Q4_K_M.gguf -p "how many planets are there?"`
[[2023-12-10-Sunday]]
Setting up device:[Raspberry Pi Documentation - Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html#install-an-operating-system)

- [x] should i run DDNS client on RPi5 to make it accessible over the internet? Woould be an interesting exercise in playing with network setting - use dynu.com ✅ 2023-12-15

[[2023-11-17-Friday]]
	- [Difference between Microprocessor and Microcontroller - YouTube](https://www.youtube.com/watch?v=dcNk0urQsQM)
		- ![[2023-11-17-Friday-2023-11-17.png]]

# Ideas
- [x] [lit-llama](https://github.com/Lightning-AI/lit-llama) or [lit-gpt](https://github.com/Lightning-AI/lit-gpt) ✅ 2024-03-15
- [ ] [[#Raspberry Pi-5]]
- [ ] #tinker_short [Tutorials | Metaculus](https://www.metaculus.com/tutorials/): Forecasting and predictions walkthroughs

## Old Stuff
- [ ] #tinker_old WearScapeAI - Figure out how to generate 3D meshes using diffusion models. Also ties in with [[#Diffusion Models|3D printing]] of text generated objects.
	- Could use prompt interpolation to generate a set of static images -> then generate video

- [ ] #tinker_old Synthetic data generation - diffusion models on custom datasets. Train a [[diffusion model]] with [[hugging face]] on some interesting dataset ([[diffusion model#Training Diffusers]]). Similar to the ideas you had about GANs, CycleGANs etc. (may be wildlife or your photos from photoshoot?)
	- [[2023-04-07-Friday]] :What if we trained a diffusion model on the Waymo driving dataset and then produced custom images with different text prompts to generate synthetic data for model training. Its a bit like the Sim2Real work for DeepRL using CycleGANs except here we leverage diffusion models.
		- Would be interesting to try on a small dataset, train a model - then generate a whole bunch of synthetic data using diffusion and retrain the perception model as a POC.
	- [[2023-04-24-Monday]] - Finetuning example here - [Lambda labs pokemon](https://github.com/LambdaLabsML/examples/blob/main/stable-diffusion-finetuning/pokemon_finetune.ipynb)
	- [[2023-04-27-Thursday]]- [[2304.08466] Synthetic Data from Diffusion Models Improves ImageNet Classification](https://arxiv.org/abs/2304.08466?utm_source=substack&utm_medium=email)

- [ ] #tinker_old A news aggregator plugin that scrapes the news sites of the world and gives you a summarized version of the news of the day from the sources, topics, interests that you picked.
		---
	- [Top 10 Best News APIs ( in 2023) [60+ Reviewed]](https://rapidapi.com/blog/rapidapi-featured-news-apis/)
	- [News API](https://newscatcherapi.com/news-api#news-api-pricing): NewsAPI is a popular and affordable news API that offers both free and paid plans. The free plan provides up to 500 requests per day, while the paid plans start at $7.50 per month and provide additional features such as real-time news updates and custom sources.
	1. RapidAPI News: RapidAPI is a platform that provides access to various APIs, including news APIs. The RapidAPI News API provides access to news articles from various sources, including CNN, BBC, and more. The pricing starts at $1.49 per month for up to 500 requests.
	2. GNews API: GNews API is a fast and reliable news API that provides access to news articles from around the world. It offers a free plan with up to 100 requests per day and paid plans starting at $9.99 per month.
	3. Contextual Web Search API: The Contextual Web Search API is a search engine API that provides access to news articles from various sources. It offers a free plan with up to 5,000 requests per month and paid plans starting at $9.99 per month.
	4. Newscatcher API - super expensive $399/mo
		---

	For video generation : [The 9 Best AI Video Generators (Text-to-Video)](https://www.makeuseof.com/best-ai-video-generators-text-to-video/)

#goal Can anything be launched on ProductHunt? - [What to know before you launch | Product Hunt](https://www.producthunt.com/launch/how-product-hunt-works)

# Diffusion Models
- [ ] #tinker_old Use a generative AI to create 3D model (diffuse3d, nvidia get3d etc.) and then 3D print it
	- [Ender 3 (V2/Pro) Wi-Fi Support: How to Upgrade | All3DP](https://all3dp.com/2/ender-3-v2-wifi-pro-connect-to-wifi/)
		-[[44855521_sept18_hero16_047a_DSLR_photo_of_an_eggshell_broken_in_two_with_an_adorable_chick_standing_next_to_it_1step.glb|example glb file]]
		- [DreamFusion: Text-to-3D using 2D Diffusion](https://dreamfusion3d.github.io/)
		- Methods results were compared to in the Point-E paper - DreamFields, CLIP-Mesh & DreamFusion

~~- [ ] [Gradio](https://www.gradio.app/) - build & host a Diffusion or Transformer model from HuggingFace in a web app~~
~~- [ ] #goal #tinker [Practical Deep Learning for Coders - Part 2 overview](https://course.fast.ai/Lessons/part2.html)~~

# Prompt Engineering with Rl

[Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910?utm_source=substack&utm_medium=email)

Prompt to create a unit test

```mermaid
graph LR
A[Prompt] -->|Encode| B[Embedding]
B --> |Decode |C[New_prompt]
C --> |Codex | D[Code]
D --> E[Unit Test]
E --> |Reward | F[RL Agent]
F --> B
```

Can't really implement this since the sentence decoding doesn't quite exist, ie cannot take an embedding and produce a new prompt. Also the embedding space is large and [[reinforcement learning]] algorithms dont really work well in large action spaces since the policy network has to output a high dimensional vector so a very very large space to explore.
[[2023-04-05-Wednesday]] - It is possible to create natural language text from an embedding vector - just asked ChatGPT!

[[2022-12-19-Monday]] : Actually may be this is possible using RLHF ([[reinforcement learning|RL]] with human feedback). Great article that described this approach - [[2-Focus-Areas/Readwise/Articles/Illustrating Reinforcement Learning From Human Feedback]]

- [ ] #tinker Use [GitHub - lvwerra/trl: Train transformer language models with reinforcement learning.](https://github.com/lvwerra/trl) library (works well with Hugging Face) to create a simple piece of code. Then use the unit test for that code to evaluate whether the LM generates the right output or not.
	- Could also use some robotic task for which the LM is producing the code. Perhaps similar to [[2-Focus-Areas/Readwise/Articles/Robots That Write Their Own Code]] - Code as Policies work from Google NYC

Another interesting paper that uses [[reinforcement learning]] for prompt tuning - [[2210.03821] In-Context Policy Iteration](https://arxiv.org/abs/2210.03821)

# Crypto

[Quickstart — web3.py 6.5.0 documentation](https://web3py.readthedocs.io/en/stable/quickstart.html#)
[Quickstart — py-evm 0.7.0-alpha.3 documentation](https://py-evm.readthedocs.io/en/latest/guides/quickstart.html)

# Past Projects

## Second Brain search

[[second-brain-web-search]]

## Openai Gpt-3 Chatbot

[[ammar-chatbot.zip]]

## Tab Maker Chrome Extension

[Tab Maker](https://tabmaker.withgoogle.com/#howto)
[[ammars-first-tab-maker.zip]]
[[picture-tab-generator.zip]]

## Arduino + 3D Printing

[[2022-05-30-Monday]]
[[2022-05-29-Sunday]]
[[2022-01-06-Thursday]] - bunch of models here
Models on GDrive here: [Google Drive: Sign-in](https://drive.google.com/open?id=1h_FOZ62lSYgC9aKznnWvMBsjAn1O2y6C&authuser=mrahusain%40gmail.com&usp=drive_fs)
[ELEGOO The Super Starter Kit](https://drive.google.com/open?id=1hb-cyYXGWnvqpDkbKmWpivY3ryAwrl0q&authuser=mrahusain%40gmail.com&usp=drive_fs) for UNO V2.0.2021.03.31
[[Arduino.zip]]
