---
created: 2023-06-26-Monday 16:28
modified: 2023-10-05-Thursday 11:11
---
[[j595-overview.canvas|j595-overview]]
[[j595-tasks]]

## #meditations
- Be aware of out of scope workstreams popping up
- Design docs & agreed upon documentation does not matter - they might just change scope anyway
- Dont need to take charge if it is not appreciated - just provide technical leadership
- FC1:
	- Be very very very clear of the deliverable.
	- Make sure you understand exactly how this system you are building fits into the larger system.
	- Be assertive about dependencies that others need to deliver - be trigger happy filing radars.
	- Learned a lot about open-set vision detectors DETR style, SAM and vision to text adapters (Video-Llama lit review)

```tasks
tags include #j595/meditation 
```

## Log
```dataviewjs 
let pages = dv.pages('"Daily"').sort(p => p.file.name, "desc");
for (let p of pages) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#j595"))))
}
```

### [[2023-10-05-Thursday]]

MLR Workshop:

- Large Langauge Model for Reinforcement Policies - LLaRP
- Language Rearrangement benchmark
- LLM as generalizable policies for embodied tasks
- RL with limited data - what if actions & rewards are sparse. Use diffusion models to predict next set of states (something like that)
- Multimodal FM model encoders (eg CLIP) are more robust to data distribution shifts
- MLX - ML Framework for Apple Silicon; MLX is as efficient as llama.cpp for inference on apple silicon; Has numpy like API - [MLX — MLX 0.0.0 documentation](https://pages.github.pie.apple.com/ml-explore/framework002/build/html/index.html)
- Vision Foundation Models -> Small-task specific models: Task oriented transfer works better and distills the model to a smaller size to run on device

SW meeting:
- Saari wants to start building muscles around finetuning and distilling models
- LoRa adapters may not be the way to go either (for whatever reason)

### [[2023-10-04-Wednesday]]

Model eval chat with the LLM 3 musketeers - they are pretty lost on the ML basics
Working through papers in reader
Worked through [[LoRA#[Fine-tune LLama2 w/ PEFT, LoRA, 4bit, TRL, SFT code llama2 - YouTube](https //www.youtube.com/watch?v=zcMQXID447s)]]
Its a good video with a practical notebook to follow along : ![[gpt_llm_trainer.ipynb]]

### [[2023-10-03-Tuesday]]

Another slow'ish day. Just did a bit of reading

### [[2023-09-25-Monday]]

Demo'ed to Kevin at 12.30pm - should have introduced myself first. #perf 
Super slow day - couldn't focus on getting anything done
Initial FC2 planning

### [[2023-09-29-Friday]]

Worked on polishing photographer-scene app for Kevin demo

### [[2023-09-28-Thursday]]

Present SayCan at literature review - [[J595 Literature Review - SayCan.key]]
Quickly hacked together a demo for a possible Kevin demo:
To figure out which Pebble Mode I am running `nvram -p`
`nvram PebbleMode=2` to get full screen display on device (from Josh)

### [[2023-09-27-Wednesday]]

Interesting code completion framework that plugs in many different model endpoints - [Visual Studio Code | Tabby](https://tabby.tabbyml.com/docs/extensions/vscode/)

Different ways of running inference on Llama models:

- Llama-cpp
- The FastChat framework supports the Vicuna LLM, along with several others: [https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat)
- The Oobabooga web interface aims to become the standard interface for chat models: [https://github.com/oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui)

### [[2023-09-26-Tuesday]]

[Amazon Alexa is evolving into a chatbot for your home](https://www.engadget.com/amazon-alexa-is-evolving-into-a-chatbot-for-your-home-152654742.html) - looks very similar to J595 vision of building character & personality for the home
[Testing Out Llama Cpp Grammar Constraint-based Sampling | by Paolo Rechia | Aug, 2023 | Better Programming](https://betterprogramming.pub/testing-out-llama-cpp-grammar-constraint-based-sampling-f154e48e6028) - interesting walkthrough on trying out llama-cpp grammar
GGML has been superseded by GGUF in llama-cpp
OASST is the OpenAssistant model standard - [TheBloke/Llama2-13B-MegaCode2-OASST-GGML · Hugging Face](https://huggingface.co/TheBloke/Llama2-13B-MegaCode2-OASST-GGML)
[ChatGPT can now see, hear, and speak](https://openai.com/blog/chatgpt-can-now-see-hear-and-speak)
		- The new voice capability is powered by a new text-to-speech model, capable of generating human-like audio from just text and a few seconds of sample speech.
		- We also use Whisper, our open-source speech recognition system, to transcribe your spoken words into text.

Reading through [[shiny-fm-llm#FLAN]] paper I wonder if we could have "Planner" as a task type that we can instruction fine tune for and evaluate
![[flan-2.png]]

Very good discussion with Yi & Xin on Q-Lora, Platypus etc - check Slack for understanding recap
	So just to firm up my grasp on this - the benefit of these approaches is that in the future we can fit 4-bit quantized model in memory on device (say 3B) and dynamically load different smaller task specific adapters. This is not computationally better per se but it all fits in memory. Quantization leads to accuracy loss but task specific adapter should hopefully compensate for it.
	The more computationally prudent version would be to just run the merged 8 (or bf16) bit base model + adapter but this takes more memory and might not fit on apple devices - since these are what cuda/ nvidia gpus are optimized for. May be in the future they will release 4-bit optimized operations.
	As for the adapter we can chose between various QKV projection matrices that get finetuned
Apparently AjaxGPT has similar architecture to Llama - thats the whole discussion about using AFM with Llama.cpp

### [[2023-09-25-Monday]]

Uneventful day - mostly caught up with emails and took stock of various tasks

### [[2023-09-22-Friday]]

Day off - Moved back to [[home#117 Topaz Way, Sf, Ca - 94131]]

### [[2023-09-21-Thursday]]

Motif/Pipeline/PipelineManager.swift is where the sigmon pipeline can be defined to subscribe to Motif channels - example
All the motif proto definitions are defined here - MotifProtos/Definitions/
Swift code that populated motif is here - MotifCore/Observations/
Extracts signals and fuses them from VU, NatVoc etc

BAckground selection could be a tool or a phase.
The device scans the background. Picks a few options and then

Talk to Photos team and get a simple background model. Look at Camera APIs for exposure.

FC1 - we do scoring
FC2 - add motion to photographer that scans background
Motion is all tracking based right now - it does not go to global ego pose

### [[2023-09-20-Wednesday]]

MLPT expo:
	tamm can help with finetuning model
LLM meeting:
	- Andreas claims that we use a lot of llama-cpp features taht may not be available with AJAX
		- Reverse prompt - when teh model detects a certain string "User: " it pops back out to hand interactive control back to user
		- Prompt caching
		- Grammars

### [[2023-09-19-Tuesday]]

Coffee with Elaheh
Dialed into MLPT expo for a bit
Figured out web socket dropped packets issue - my server was sending back 2 responses per image but I was just registering one handler in the app. So the handlers were getting wasted in the string responses.
Long chat with Anton about what Reza's task for memory should be

### [[2023-09-18-Monday]]

Spent a bunch of time merging in Sylvains changes and using his gazing signal. Got the merged patch working after running into some issues with 22V79 -> reverted to 22V77

### [[2023-09-15-Friday]]

Showed off simple photographer background app in the standup
For some reason websocket only returns 2 masked images back when i initiate a connection once for all images rather than initiating a connection everytime. Not sure why that is.
	![[j595-daily-2023-09-15.jpg]]

### [[2023-09-14-Thursday]]

Got app and websocket to superserver connection working
Refactored app with Sylvain to send 4 images at a time when capture is pressed
Need to get masked image back and display it.

- what does siri use?

database and object store are two key components for w&b
![[j595-daily-2023-09-14.png]]
Handful of SPG Dev-ops have access to MySQL where the data is stored
No W&B folks have access
Getting more interest from Siri - talking with Jimmy Hley
SPG has access to more seats

### [[2023-09-13-Wednesday]]

Chat with Mark Pauley on how to do websockets:
Basically:

```
import Foundation
...
let urlsession = URLSession()
let wsTask = urlsession.webSocketTask(with: "[ws://host](ws://host/):port/path")
wsTask.send(.string(...)) { error in ... }
wsTask.receive { result in … } (edited) 

where result is `Result<URLSessionWebSocketTask.Message, Error>`
```

Sends a WebSocket message, receiving the result in a completion handler. 

[Websocket - send](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/3281790-send)
[Websocket - receive](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/3281789-receive)

Command to connect device to a network: `mobilewifitool -- join -i en0 --ssid=ABeautifulPlace --password=WaffleIr0n ; mobilewifitool -- autojoin add --ssid=ABeautifulPlace`

### [[2023-09-12-Tuesday]]

Omar Khattab talk on [[shiny-fm-datasets#DEMONSTRATE–SEARCH–PREDICT Composing retrieval and language models for knowledge-intensive NLP]]
Apple launch event
Abhishek - gaze & attention
![[Gaze_and_attention.key]]
Floris - recognition stack; face & torso
Capabilities to get signals iOS & python repos
Far field models:

- CamGaze - are they looking at the camera?
- SceneGaze - where in the scene are they looking?
Near field models
- DeviceGaze
- ScreenGaze
Shipping usecase:
- CenterStage with CamGaze
- SceneGaze

SceneGaze & ScreenGaze are available as APIs in the VisionFramework
Model inferences are real time

![[j595-daily-2023-09-12.png]]

Some commands for Photographer:
`streamlit run photographer-background.py`

### [[2023-09-11-Monday]]

Sylvain, Pauley, Kyle helping debug the simple photo capturing app - mostly Sylvain trying to get it work for me.
Got model groundedsam hosted and working through streamlit app on superserver

### [[2023-09-08-Friday]]

Tried to setup iphone app that captures camera picture
Photographer standup update
Met with Sylvain & Paul to figure out how to get app to access camera

### [[2023-09-07-Thursday]]

Got websocket app working by factoring out grounded sam portion from the streamlit frontend.
Now I have a websocket backend that can be called to segment the image out and return a background answer. Just need to implement it with multiple images and pick the largest mask size as answer.
Meeting with Camera/Video analysis team:
Meeting with Abhishek & Vinay:

- Recognizing who is in the FOV of device - where they are looking at? isGazing like features.
- Martin & Chris have spoken to these guys before
- presence, identity, attention, gesture etc
- Working on human-object interaction - where the user is pointing at? visual grounding element
- Gaze understanding
- NatVoc is doing multi-modal - promising direction
- Visual Understanding (VU) framework encapsulates that
- [ ] Need to set up follow on meetings with some eng on Abhisheks team & Motif peeps
### [[2023-09-06-Wednesday]]

[How to Make an App in 8 Days (2023) - Full Walkthrough - YouTube](https://www.youtube.com/watch?v=K0t-RCSlasE&list=RDCMUC2D6eRvCeMtcF5OGHf1-trw&start_radio=1&rv=K0t-RCSlasE&t=23)
	![[j595-daily-2023-09-06.png]]
	[SF Symbols - Apple Developer](https://developer.apple.com/sf-symbols/)

### [[2023-09-05-Tuesday]]

Chat with Mark Pauley about streaming images from device:

- BackgroundCameraModel - fgrab the jpeg blob in there
- Create another app within Thursday to isolate the image. upload to superserver. - makes it more tractable
- [Core Image | Apple Developer Documentation](https://developer.apple.com/documentation/coreimage)
- `pkill -9 CoreDeviceService` if device not found
- Cmd+Shift+2 to look for devices
-     `snapshottool golive 2` to.make system partition read-write on device

### [[2023-09-01-Friday]]

Meeting with Vision Foundation model team - [[MFM for SPG v2 - no VCG.pdf]]

### [[2023-08-31-Thursday]]

VectorDB is coming soon - should be available with Foundation Models SDK (like SQLLite)
KnowledgeGraph Query is what Megadome is used for (KGQ)
Megadome is not the best for unstructured content

Spotlight index - use for unstructured content

### [[2023-08-30-Wednesday]]

Showed my streamlit app with GroundedSAM to the LLM standup group

### [[2023-08-29-Tuesday]]

Photographer standup - broke down tasks for my pieces in the numbers doc that Marios sent out. Nobody else seems to have anything there but they dont want to build off on my breakdown either - mostly all just talk
![[PHOTO- Umbrella Radar Creation.numbers]]
Got the GroundingSAM demo working with streamlit. Just need to add a bit more logic to look through different mask types and pick best background mask.

### [[2023-08-28-Monday]]

Focused on getting GroundingSAM up & running.
Read through [[shiny-fm-datasets#Grounding DINO Marrying DINO with Grounded Pre-Training for Open-Set Object Detection|GroundingDINO]] , [[shiny-fm-datasets#DETR - End-to-End Object Detection with Transformers|DETR]] and a couple other papers.
Sat in on a Memories meeting that was not super relevant for me

### [[2023-08-27-Sunday]]

Quite a pain to get SEEM running on mac OS - even after trying cpu instead of mps
Keep running into this error even though I make sure to convert attention_mask dtype to float16 or bool. Query dtype is getting changed somewhere in the depths of pytorch to BFloat16
`RuntimeError: Expected attn_mask dtype to be bool or to match query dtype, but got attn_mask.dtype: float and  query.dtype: c10::BFloat16 instead.`

Figuring out the size of these various models that we are trying to run:
seem_focall_v1 : model params - 341,181,177
seem_focalt_v2 : model params - 164,619,249

If I am getting 5-8 secs inference on a few object classes with grounded SAM - might as well run that and forget the other models for now. Build everything around that.

### [[2023-08-25-Friday]]

Read some papers on VLMs [[shiny-fm-datasets#X-Decoder]], [[shiny-fm-datasets#Semantic-SAM]] etc

Trying to get SEEM working but it is littered with cuda calls everywhere so not sure if it is worth getting running on M2 Ultra - [GitHub - UX-Decoder/Segment-Everything-Everywhere-All-At-Once at 6129006c46d9cfbf13a841c149134ea2c507f562](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once/tree/6129006c46d9cfbf13a841c149134ea2c507f562)
	- Stored in j595/VLMs/ directory

### [[2023-08-24-Thursday]]

Finished reading the Generative Agents paper - attended Joon Park talk at 11am
Suncore is an assortment of services for J595 that provides client daemon like utilities

It might be better to just use GroundedSAM & SEEM. SemanticSAM might not do what I want.

### [[2023-08-23-Wednesday]]

First LLM eng focussed standup
Tried to run GroundingDINO + SAM gradio demo to get inference numbers on M2 ultra.

### [[2023-08-22-Tuesday]]

AppIntents meeting:

- How do we create grounded affordances for these intents? ie SayCan like value functions. What is the expected reward for the device to run this AppIntent? does it make sense to run this AppIntent now and in this order?
- Meeting kind of went south
- These guys want to see "Next action prediction" using an LLM inside an inner loop of a behavior tree - for example use an LLM to frame a person for a picture.

W&B Product demo:

- Focus on tools related to prompt tracking & management.
- How to store & host models? How to link against stored models?

Extracting Statee from Device - chatted with Paul

- UUID needs to call to Suncore
- EntityKit publishes our current state of the world

Llama2 13B at 4bit quantization -> 6.8GB [[shiny-fm-datasets#Llama-v2]]

### [[2023-08-21-Monday]]

Slow morning - browsing painters & handymen on Thumbtack
Impromptu meeting with HI on Photographer - showed off a simple version of GroundedSAM to team
Generative canvas meeting

### [[2023-08-18-Friday]]

This paper might be relevant in us trying to create an instruction finetuning dataset for Photographer behavior generation - [[2308.06259] Self-Alignment with Instruction Backtranslation](https://arxiv.org/abs/2308.06259)
Mostly cleared out emails at Neighbor cafe in the morning
Meeting with Daniel Hsu from AppIntents team - definitely the way to go to define the behavior catalog

### [[2023-08-17-Thursday]]

Started reading Generative Agents paper ; resurrected pinecone index, backed second brain to git
Tried out W&B for LLMs with MLR instance
Found out about Sage which is an LLM based way of creating Apple shortcuts
1-1 with Martin and then met with Marios to decide project management for AIML group.
Sage +LLMs API calls meeting

- Sage can potentially replace Weaver
- It can take a user string and create various API calls for the different apps that are on the system - Like Apple Shortcuts (its the same team)
- Their system allows us to arbitrarily register new intents
- 2 questions: what granularity of intents does sage provide? and do they allow finetuning if we want a photographer specific experience?
- AppIntents:
	- (Intro) [https://developer.apple.com/wwdc22/10170](https://developer.apple.com/wwdc22/10170)
	- (Deeper Dive) [https://developer.apple.com/wwdc22/10032](https://developer.apple.com/wwdc22/10032)
	- (2023 Enhancements) [https://developer.apple.com/wwdc23/10103](https://developer.apple.com/wwdc23/10103)
- Sage:
	- I think this is the one that the Sage team is basing their work on: [https://arxiv.org/pdf/2303.09014.pdf](https://arxiv.org/pdf/2303.09014.pdf)
	- That links to this: [https://arxiv.org/pdf/2201.11903.pdf](https://arxiv.org/pdf/2201.11903.pdf)
- Action items:
	- [x] Ammar - set up a breakout session for granual photographer specific behavior nodes ✅ 2023-08-17
	- [x] Mark - Setup meeting with Sage to see if they are ready for us to plug in our behaviors as App Intents into their system ✅ 2023-08-17

### [[2023-08-16-Wednesday]]

Got SAM working this morning - at least on CPU (takes a bit long 1-2 mins)
Also found this interesting `supervision` package - [GitHub - roboflow/supervision at blog.roboflow.com](https://github.com/roboflow/supervision?ref=blog.roboflow.com) . Would help prototype a lot of comp vision stuff.

Trying to get GroundedSAM working on mac hardware - [GitHub - IDEA-Research/Grounded-Segment-Anything: Grounded-SAM: Marrying Grounding DINO with Segment Anything & Stable Diffusion & Recognize Anything - Automatically Detect , Segment and Generate Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything)
Running into tensor broadcast issues converting models to 16 bit. There are like 4 models involved - SAM, GroundingDINO, BLIP for img captioning, diffusers

Chatted with Amael for a while - he is working on monocular depth estimation now - would be interesting to sync him up with Paul & motif team.

Having fun going into the weeds of the GroundingSAM model - it uses SAM, GroundingDINO, BERT, StableDiffusers & BLIP
I am running SAM on MPS and GroundingDINO on CPU for now - the cumsum operation is missing on my current pytorch install. Will need to upgrade to nightly to get that.
I should just swap out the raw model loading in favor of [[hugging face]] ones for both SAM & Grounding DINO - its a lot easier to deal with.
Need to port this over to Mac Studio now

### [[2023-08-15-Tuesday]]

Yi waats to evaluate AjaxGPT with the Llama model that we have

- could help create a benchmark dataset with sequence planning experiences that Andreas has shown with Llama 70B
- Once we have that instruction tuning & benchmark dataset - we could evaluate AJAX with Llama and that also helps us in general for finetuning whichever LM we'd like to go with.
- [ ] May be setup a meeting with Yi, Andreas, Xin & Josh to chat about this benchmark creation
Long chat with Anubhav on memory profiling - basically they dont know how to handle LLMs
Drove back early with Victor
Started thread with HI to get inputs on how to bake in heuristics for "Photo Picker"
Started looking at setting up Llava to run locally
Looking into experimenting with SAM for background selection -> I could extract all the surfaces from the scene then surfaces that are above a certain pixel size could get passed to a LLM in order to suggest where to stand for the best picture.
Questions to ask the Camera/ Photos team:
- What are the primitives you can give us - isSmiling, isGazing etc?
- Do you have any photo composition quality measures?
- Do you have anything equivalent of Meta's Segment Anything model?

From Xin for runnign vision language models on Apple silicon:
`conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly; pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu`

### [[2023-08-14-Monday]]

Victor gave a DMP talk with some initial results - [DMPs](https://www.icloud.com/keynote/07aBUD7sasfEgPPWyn0HHSbRQ#DMPs)
Dug deeper into [[LoRA]] & [[LoRA#[Understanding 4bit Quantization QLoRA explained (w/ Colab) - YouTube](https //www.youtube.com/watch?v=TPcXVJ1VSRI)|QLoRA]]

### [[2023-08-11-Friday]]

Sent out W&B slack msg. Tried using it
Read up a bit on LoRA (just simple stuff)
Left for Soda Springs camping

### [[2023-08-10-Thursday]]

Got invited to a bunch of meeting with design & HI for photographer, & memories
We need to know what the camera & photos API provides in terms of primitives - isSmiling, isGazing, face & body bounding boxes etc.

### [[2023-08-09-Wednesday]]

From the generative canvas & memories meeting:

- There 5 major eng workstreams that are popping out:
	- Recognizing entities for generative canvas - [Quip brainstorm doc](https://quip-apple.com/10puAPz5ur5P) (Xin or Reza perhaps?)
	- How do we make the LLM maintain state such that entity extraction is real time & we are no re tokenizing the full prompt? (Ammar)
	- Storing full user transcripts and EntityKit outputs on device (Anton)
	- Extracting salient entities to commit to memory (related to 1 but slightly different - Xin or Reza perhaps?)
	- Memory architecture - is it one or more vector stores that we use - how does retrieval work? (TBD)
- For all of these need HI to provide interaction scripts:
	- How does the user play with generative canvas - what apps, what are important entities to extract?
	- What is the duration of memory? what should the device try to remember?
- Action items:
	- [x] Anton to create flow diagram for greeting with memory ✅ 2023-10-09
	- [x] Andreas to create flow diagram for generative canvas ✅ 2023-10-09
	- [x] Ammar to start a design doc for tech deep diving - need to figure out which part? ✅ 2023-10-09

### [[2023-08-08-Tuesday]]

W&B meeting with Yi & Craig:

- Yi - W&B dont have access other than certain disclosed vendors
- Only admins within apple have access - Yi is admin and has access
- We can create dedicated instance for J595 (dedicated hardware & storageneed to disclose Yi & Brandon
- [ ] Need to setup AppleConnect on local machine
- [ ] Yi can help setup instances
- [ ] Need to get license from W&B

Accessign image frames:

- Its pretty easy to access the camera API
- Transport can be websocket (what Andres built) or sigmond (what Jacob built) - recommends using websocket

### [[2023-08-04-Friday]]

Morning meeting with Andres, Saari, Martin, Xin, Josh on specing out hardware
	- I need to profile the VLM stuff
Lots of discussions around using W&B and what to go with - MLR or SPG instance

- David Koski pointed me to this [Quip doc](https://quip-apple.com/oAOoAZ8XCKTW). Hopefully we can use W&B that Yi & Cheng setup for T172
Have Turi setup now for J595

Prompthub:

- Like a Github for prompts; want to be more non-developer focused compared with W&B
- Here's your access code:zZ7gz1
- You can sign up here: https://app.prompthub.us/registration-access

### [[2023-08-03-Thursday]]

Presented Lit Review on Video Llama - ![[J595 Literature Review 1 - VideoLlama.key]]
Lots of excitement around grammar in Llama-cpp
We need tools for prompt management
1-1 with Martin:

- Its ok to run Photographer stuff on laptop

### [[2023-08-02-Wednesday]]

Photographer Fluidity Flow meeting

- Register gaze signals with user transcripts. Need to remove Regexs from
- Gaze is calculated single frame
- Vision framework (probably NatVox) supplies the gaze - can get angle of eyeball at close range, can get angle of shoulder
	- Should ask Martin & team whats available
- Two main actions triggered by Regex - TakePhoto, PickPhoto
- Three steps:
	- swap Regex filter with an LLM (with same string)
	- Capture more context (always listening) and then pass that to LLM
	- Add gaze & engagement signals to the LLM
	- Create new more complex behaviors (like wait for acknowledgement)

Photographer Design doc meeting with HI:

- Feels more like chatting with ChatGPT - need to incorporate more of the device perception
- Candid photos - party mode
- "In the style of" - not just style projection but helps with framing, how to pose etc.
	- where do we draw that boundary - there is a lot of nuance to photos
- It should nail group or individual portraits
- Need to incorporate motion piece -
- "Hey we are ready next to the Christmas Tree"
- Should be more conversational than fully instructional - think about how to make it more grounded in its current environment
- Head could move slow until the user interacts with it and says "Stop"
- Professional photographer - rule of thirds etc should be default when unspecified
- User should be able to cancel behavior / interrupt the robot / re route behavior - Kevins idea of relational computing
- Priority of having a fluid conversation is more important than an open ended goal - shouldnt have to say key words
- Device asking
- Conversational is very important and must be on the rails
- Agatha to provide:
	- Heuristics of types of photos
	- Scripts of fluid interaction
	- Highlight certain scenarios for motion

### [[2023-07-25-Tuesday]]

Prepared Lit review slides
Went for a stroll to Convict Lake
Ended early to drive back to SF

### [[2023-07-31-Monday]]

Responded to comments on my design doc for [Photographer Experience with V/LMs](https://quip-apple.com/b4EOAkR9Tgar)
Started prepping for lit review - Video Llama
Looking through Photographer & Friday codebase
Long ass meeting on Memory for FC1 - not very productive for me

### [[2023-07-28-Friday]]

Slow day again - was out all morning
Skimmed through the RT-2 blog post & paper - responded to some Slack msgs on it
Tried to get Locomotion YAMS package PR build working - build file got botched - will probably need help from Pauley to sort it out.

### [[2023-07-27-Thursday]]

Pretty slow day. FC0 retrospective meeting. Got new laptop so spent a bit of time trying to set it up

### [[2023-07-26-Wednesday]]

Surveyed more papers to get a high level understanding of vision to language adapters [[shiny-fm-datasets]]
Wrapped up design doc for [Photographer Experience with V/LMs](https://quip-apple.com/b4EOAkR9Tgar) #perf
[[photographer-fc1-design-doc-diagram.key]]

### [[2023-07-25-Tuesday]]

Bit of a slow day yesterday.

- Went to Apple Park for the first time
- Reviewed some LLM & VLM papers

### [[2023-07-24-Monday]]

Mostly working on design doc for [Photograoher experience with V/LLMs - Quip](https://quip-apple.com/b4EOAkR9Tgar)
FC1 planning meeting

### [[2023-07-21-Friday]]

FC0 LLM retrospective meeting

- Siri100 is doing LLM based work for fluid domain switching
- Sorcery2 is also competing with Siri100 but trying to do a better job of going into domain but getting back out
- Chris Saari says we should stay aligned with Siri100 for our flow switching work. We have Siri10 in the short term
- Short term goal is to put Weaver in to Siri10?
- Jason Siri Williams is a good guy to talk to about the Siri experience
- Chris - focus on the photographer usecase - system right now is super brittle. LLMs are used in a very hardcoded way. Have no regexes in FC1
- **LLM should just spit root notes for a behavior tree
- Investigate working memory - so maintain the conversational state**
- Siri100 is working on building memory for MegaDome
- Demo scripts:
- "Take a photo of the group"
- Figure out how many people, where to take the photo?, get rid of regexes - click the picture now, which photo to pick
- Stylize photo, click pano
- Non goal - finetune for on device
- Action items:
- [ ] Ammar to start photographer design doc
- [ ] Chris to walk through aspiration deck for Siri100, Sorcery

Asked a dumb question to Xi - why cant we just buy a desktop with A100? Turns out the chip is built for datacenters and have specific cooling requirements.

### [[2023-07-20-Thursday]]

How do we represent the onboard perception input to the LLM - Motif + Image captioning ?

- From Chris Saari - Weaver would be an impactful usecase

Read the following papers:

- [LLM-BRAIn: AI-driven Fast Generation of Robot Behaviour Tree based on Large Language Model](https://arxiv.org/pdf/2305.19352.pdf)
- [Robot Behavior-Tree-Based Task Generation with Large Language Models](https://arxiv.org/pdf/2302.12927.pdf)

The big question is how do we describe the scene to the LLM? ie introduce state information.

### [[2023-07-19-Wednesday]]

Watching YT videos on [[behavior trees]] that Hans recommended

- [ ] #j595/someday    [https://www.youtube.com/watch?v=xbvMnpwXNPk&t=1538s](https://www.youtube.com/watch?v=xbvMnpwXNPk&t=1538s) - from Hans (also watch GDC behavior tree arborist - video games)
From Afshin RoomPlan meeting:
- 4M is an internal multi modal foundation model that these guys are working on

### [[2023-07-18-Tuesday]]
- [x]  Try running Llama2 locally - [https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML) ✅ 2023-07-18
Tried the [[turi]] [Bolt](https://bolt.apple.com/docs/task-basics.html) & [Hub](https://turihub.apple.com/docs/workflows/quickstart/getting-started/) docs.

### [[2023-07-17-Monday]]

Tried to fix the Locomotion build on BI servers. Command to run buildit locally is below (its still does not replicate exact build in BI)
`sudo xbs buildit -project Locomotion -update CurrentSapphirePebble .`
Lots of chatting around HI animation scripts and behavior planning based on that

### [[2023-07-14-Friday]]

Xin got Video-LLama and Otter working
Setup TuriHub project - gonna try and use it for compute
Imported YAMS parsing library and got the basic parsing working by making everything Codable
Productive chat with HI - Marisa, Agatha & Greg

### [[2023-07-13-Thursday]]

From Hans:
	Behavior / decorators
	look up blackboard
	for each behavior there is a vocabulary.
	Behavior -> Interaction -> Experience

### [[2023-07-12-Wednesday]]

Meeting with Xin & Yi:
	QLora AJAX GPT is under torch in foundation models repo
	HuggingFace format of AJAXGPT is the pytorch format
	convert_hf_checkpoint.py use to convert Tensor
	`convert-pth-to-ggml` from ggeranov/llama.cpp repo to convert pytorch checkpoint to ggml
	klogin.apple.com - for single GPU provisioning
	Turi Bolt - cluster compute

From Hans:

- Here are the 3 core projects to check out:
	- Representing people and their state - [https://github.pie.apple.com/heavenly/EntityKit](https://github.pie.apple.com/heavenly/EntityKit)
	- Behavior tree implementation - [https://github.pie.apple.com/heavenly/BehaviorKit](https://github.pie.apple.com/heavenly/BehaviorKit)
	- Character, interactions (Conversation, ambient motion, etc) and behavior building blocks (Say, track, animate, wait, express, …) [https://github.pie.apple.com/heavenly/CharacterInteractionKit](https://github.pie.apple.com/heavenly/CharacterInteractionKit)
	- Quip doc for [Attention & Engagement](https://quip-apple.com/poUMA6BPW3uu)

### [[2023-07-11-Tuesday]]

Andreas presents his work using Gen AI & LLM in FC0 - [Quip doc](https://quip-apple.com/vkSoApAhbtq0)
StoryTime .swift (something like that) has the prompts and story flow etc

- [x] Look up Vicuna ✅ 2023-07-12

Ambient behavior planning - where should we look? what expression to make?

- These behaviors are defined in a framework - ask Victor where they area

LLM should express the concept of behavior tree - or surrogate of that. Goal of the model is to output behavior tree actions

- [ ] Walk through EntityKit, BehaviorKit - go through prompts

CharacterAnimationKit handles the faces & expressions on the device.
MotionKit handles the 3DOF motion animation
BehaviorKit takes EntityKit and a few other stuff as input - it outputs to CharacterAnimationKit & MotionKit

ssh local@superserver.corp.apple.com - PW: ireallylikerobot
Run this command from the llama.cpp directory after compiling it
`./main  --temp 0.65 --top-p 0.5 -c 2048 -m models/13B_vicuna_new/ggml-vic13b-q4_0.bin --mlock  -p "Act in the role of a famous author. Given a basic story please create a witty title of what can happen in the story, be concise.`

- [x] Get llama-cpp working locally (through python wrapper in afm3 conda env) ✅ 2023-07-11

### [[2023-07-10-Monday]]

Chat with Mark Pauley about Sigmon middleware stuff
	Channel.swift - main IPC stuff
	PassThroughTests.swift - good to look at for API
	switchboard - routes produces to consumers; serializes msgs etc
Chat with Victor about canned animations and how to apply LLMs for motion
	LaunchApp com.apple.internal.SunGlasses - Use this on device to run and visualize different HI animations that Huli put together
	sessionParameters.swift - This is the file where the animations are listed out; look here to find how they are defined

Played around with setting up code embeddings using AJAX & LangChain

### [[2023-07-07-Friday]]

Read through trajectory optimization tutorial from Matt Kelly [[trajectory-optimization]]
Wrapped up & submitted my first PR for plumbing through movement tracking mode
Watched [[trajectory-optimization#[RI Seminar Stefan Schaal From Movement Primitives to Associative Skill Memories - YouTube](https //www.youtube.com/watch?v=ViN87GTew1Y)]]

### [[2023-07-06-Thursday]]

Sigmon and locomotion - stay on ToT
After device update run this code from Quip doc:
	```

```
# Enable simulator motion
	login -f mobile defaults write com.apple.t686.actuationd mcu_type eve  
	killall -9 actuationd  
	login -f mobile defaults write com.apple.motif UseJointFK -bool true  
# Disable Motif's visual pipeline, causing it to switch to using Everest
	login -f mobile defaults write com.apple.motif VisualPipelineEnabled -bool false  
# Reload peopleawarenessd
	launchctl unload -w /System/Library/LaunchDaemons/com.apple.peopleawarenessd.plist  
	launchctl load -w /System/Library/LaunchDaemons/com.apple.peopleawarenessd.plist  
# Add personas so we can know people's names
	sunctl importStaticPersonas

```

To inspect logs: osatool legacy <ips_log_name> | less

To list all devices connected to Macbook : `devicectl list devices`
To list : `sigmonctl list`
To start broadcasting sigmon channels for Foxglove : `sigmonctl glove --port 8765`
Connect Foxglove to : ws://Bedroom.coredevice.local:8765

Some short terms tasks:

- Track & move in multi person tracking
- config file to move params of motionquality params into a proto text
- eval stuff - set it up locally

Trajectory optimization [writeup](http://underactuated.mit.edu/trajopt.html) from Russ Tedrake

### [[2023-07-05-Wednesday]]

From Victor on Slack - the simplest thing is to add which "movement tracking mode" we're in to the protobuf. relevant snippets are:multipersontracking.swift:15 (where we choose what mode to be in)
optimizerInterfaces.swift:81-ish (where message packing happens)
planningProblem.proto. so just adding an extra field to the PlanningCycle message (or more likely, one of its submessages) that's an enum on what mode we're in
For testing - everest + the raw message panel in foxglove (basically `rostopic echo`)
oh one more relevant script: `(base) ➜ LocomotionKit git:(victor/individual_costs) ✗ sh Scripts/CompileProtobufs.sh "../TrajectoryOptimizer/Protobuf/Definitions" "../TrajectoryOptimizer/Protobuf/Generated"`
cause xcode sucks so much, we have to manually compile the protos and check them in

Needed to manually install - ```brew install swift-protobuf``` for the proto generation script to work

To deploy to device - Use XCode2 : Product -> copy to device

`sigmonctl record` to record a log on device. SSH onto device from iOS ToolBox to run this. Can then copy logs using that same tool.

To get to robotics pieces - Character -> Behavior Building Blocks -> Track Multiple People etc.

check for process running: `pgrep peopleawarenessd` or `pgrep locomotiond`
when I flash my code from XCode - everything seems to crash on device

- [x]  make sure I am flashing code right ✅ 2023-07-06

### [[2023-07-03-Monday]]

Looking at using Github Copilot snd Copilot chat
Trying out using AJAX Plugin but running into access issues-
New [doc](https://github.pie.apple.com/foundation-models/plugin) , old agraves [doc](https://github.pie.apple.com/agravesfuenzalid/ajax-python)

### [[2023-06-30-Friday]]

BuildKite for database pipeline to host logs in the triage & eval pipeline
[Turi Assset store](https://asset-store-mlpt.corp.apple.com/docs/glossary.html#term-Atom) is potentially interesting - instead of Trove use some other DB for the dataset.
According to Antonio [Conductor](https://docs-data.aws.sea.g.apple.com/conductor/apis) is the new way to go since Turi asset store has trouble scaling - this is more a replacement for Blobby.

- [ ] #j595/someday try and create embeddings for all heavenly code files

### [[2023-06-29-Thursday]]

PurpleRestore3 from ultimate Xcode installer - for flashing SW on iPad
[Build SWE](https://builds.swe.apple.com)
iOS Toolbox App - to SSH to device
`stack` app to view devices
J595 device [Everest Setup quip doc](https://quip-apple.com/3brHALa8Z0rS)
Ultimate XCode installer has bunch of apps - iremotex etc
stack app to connect and manage packeges on device
check logs on device here -
`/var/mobile/Library/Logs/CrashReporter`

![[j595-daily-2023-09-13.png|350]]
ilqrReplayTool is Victor's log playback

### [[2023-06-28-Wednesday]]

[FM users - getting started guide](https://quip-apple.com/SgBQAWpb9Lm5)
Found:
- [GitHub - JinghaoZhao/GPT-Code-Learner: Learn A Repo Interactively with GPT](https://github.com/JinghaoZhao/GPT-Code-Learner)
- [Qdrant - Vector Database](https://qdrant.tech)

Tried to get starcoder from huggingface working - running out of mps memory
Found [CodeLM VS code plugin](https://github.pie.apple.com/AI-for-Devs-Community/CodeLM-VSCode-Extension) and a code AI community at Apple - [Usage examples](https://confluence.sd.apple.com/display/SDP/Usage+Examples) of CodeLM
Tried running - [ajax-python](https://github.pie.apple.com/agravesfuenzalid/ajax-python) LLM : running into access issues & still waiting
Working on XCode installer to work with Sapphire access

### [[2023-06-27-Tuesday]]

[Cassadi](https://web.casadi.org) - SimForce like system
Solve:
- Motion Track
- Move Track + Animation blending
- Trajopt.solve(move + animation)
	- Final trajectory
OptimizeInterface.swift (half the optimation code + other half in python with cassadi)

Coordinator.swift

Areas of exmploration :

- Nervousness problem - head moves fast
	- App reduces the number of targets to track
	- weighted blending of tracks
- Evaluation pipeline
	- metrics on trajectories: system & module level
- RLHF like reward model for motion trajectories

Possible onboarding tasks:

- Run simulator on device
- Motion parameters moved to a config file or iOS app

- Dynamic primitives (worth trying out) - [https://arxiv.org/pdf/2102.03861.pdf](https://arxiv.org/pdf/2102.03861.pdf)
- [ ] #j595/someday   Text to trajectories (diffusion model) - [Human Motion Diffusion Model](https://guytevet.github.io/mdm-page/)
- [ ] #j595/someday   Constrained optimizer tutorial (ILQR) - [https://bjack205.github.io/papers/AL\_iLQR\_Tutorial.pdf](https://bjack205.github.io/papers/AL_iLQR_Tutorial.pdf)
- [[dynamic-movement-primitives.pdf]]

### [[2023-06-26-Monday]] - Team introductions

Saw the Lotus prototype.
Interesting LLM + Diffusion model demo from Andres + Hans +...
Team history and org overview from Martin
Victor walked me through his motion primitives and trajectories that he is generating.
