---
aliases: 
created: 2023-01-04-Wednesday 11:27
modified: 2024-04-19-Friday 13:36
related:
  - "[[*shiny-fm-diffusion]]"
  - "[[*shiny-fm-llm]]"
  - "[[*shiny-fm-reasoning]]"
---
# Models
## Saycan

[[SayCan paper.pdf |Paper]]
Highlights: [[2-Focus-Areas/Readwise/Articles/Do As I Can, Not As I Say Grounding Language in Robotic Affordances]]
![[Pasted image 20230104164546.png|500]]
They use a set of primitive skills that grounds the robot in terms of the actions it can perform. The skills are language conditioned in that it uses a text embedding (output of the [[large language model|LLM]]) to figure out which skill/policy to run.
The primitive skills are conditioned on language or video and are simple behavior cloning policies [[2-Focus-Areas/Readwise/Articles/Can Robots Follow Instructions for New Tasks]] (aka BC-Z). The value function comes from MT-Opt since BC-Z is simple imitation learning and not [[reinforcement learning]]]
![[Pasted image 20230104192857.png]]
![[Pasted image 20230104192917.png]]

## Inner Monologue

Highlights: [[2-Focus-Areas/Readwise/Articles/Inner Monologue Embodied Reasoning through Planning with Language Models]]

![[Pasted image 20230104184605.png]]
![[Pasted image 20230104185109.png]]
![[Pasted image 20230104185708.png]]

The skills used here are the same as the SayCan paper in the real-world kitchen setting.
![[Pasted image 20230104190945.png|600]]
Interesting that the object feedback to the system was from a human and not from ViLD or other open vocabulary detectors. Seems like that doesn't work well yet.
![[Pasted image 20230104191747.png|700]]
Hindsight model is run only if the probability from the foresight model is above a certain threshold.
![[Pasted image 20230104191954.png|800]]
![[Pasted image 20230104192013.png|550]]
The BC-Z policies are perhaps text conditioned on the set of objects above for the "pick" skill

## RT-1: Robotics Transformer

[[2-Focus-Areas/Readwise/Articles/RT-1 Robotics Transformer for Real-World Control at Scale]]
[RT-1: Robotics Transformer](https://robotics-transformer.github.io/)

## Socratic Models

[Socratic Models: Composing Zero-Shot Multimodal Reasoning with Language](https://socraticmodels.github.io/)
Framework that uses structured dialogue between pre-existing foundation models, each of which can exhibit unique (but complementary) capabilities

## Interactive Language

[Talking to Robots in Real Time – Google AI Blog](https://ai.googleblog.com/2022/12/talking-to-robots-in-real-time.html)
![[Pasted image 20230118123739.png]]
![[Pasted image 20230118134338.png]]
We define five simulated evaluation task families (spanning 696 unique task conditions) in Language-Table, each with a hand-defined success criterion:

- block2block: Push a block to another block. Success is thresholded distance between source and target block.
- block2abs: Push a block to an absolute location on the board: top left, top center, top right, center left, center, center right, bottom left, bottom center, bottom right. Success is thresholded distance between block and target location.
- block2rel: Push a block to a relative offset location: left, right, up, down, up and left, up and right, down and left, down and right. Success is the thresholded distance between the block and the invisible target offset location.
- block2blockrel: Push a block to a relative offset location of another block: left side, right side, top side, bottom side, top left side, top right side, bottom left side, bottom right side. Success is the thresholded distance between the source block and the invisible target offset location of the target block.
- separate: Separate two blocks. Success is the thresholded distance between the two blocks.

## Bc-z

Imitiation Learning policies
[[2-Focus-Areas/Readwise/Articles/BC-Z Zero-Shot Task Generalization with Robotic Imitation Learning]]
Key contributions:

- Interactive Language framework for training language conditioned behavior cloning / imitation learning policies (LAVA architecture)
- Hindsight relabeling: way of annotating robot actions with language strings by breaking down video sequence into constituent tasks.
- Language-Table: a suite of human-collected datasets and a multi-task continuous control benchmark for open vocabulary visuolinguomotor learning.

![[Pasted image 20230110151920.png]]
![[Pasted image 20230118125643.png]]

The policy architecture is divided into an encoder q(z|w), which processes the command w into an embedding z ∈ Z, and a control layer π, which processes (s, z) to produce the action a,

It turns out that simply encoding the video and training the policy with the encoded embedding tends to overfit. Therefore they add another term to the objective that computes the distance between encoded video embedding + a language embedding that the video encoder tries to predict. Adding the cosine distance between the two forces the video and language embeddings to be closer together and generalizes the behavior cloning policy better.
![[Pasted image 20230110154125.png]]
Overall conditioning the task on language works a lot better than conditioning it on a human demonstration video. The main bottleneck for language conditioning is the control layer (aka imitation learning) policy itself.

## Transport-nets

[[2-Focus-Areas/Readwise/Articles/Transporter Networks Rearranging the Visual World for Robotic Manipulation]]
![[Pasted image 20230110164903.png]]
Simply put - its a network that tries to transport (in vision space that can be parameterized into actions) how an object looks/is at the moment to how to reconfigure/move it into another configuration. Eg: align red object with white line on table etc. Its a hallucinating network that imagines how the final position should be and then samples all the intermediate actions to transport the input observation to this output/desired observation. It does all of this without detecting key-points, segmenting objects etc. "No objectiness"
![[Pasted image 20230110171351.png]]

## Cliport

[[2-Focus-Areas/Readwise/Articles/CLIPORT What and Where Pathways for Robotic Manipulation]]
we present [CLIPORT](https://cliport.github.io/), a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of [[*shiny-fm-datasets#CLIP : Connecting Text & Images|CLIP]]
with the spatial precision (where) of [[#Transport-Nets]].
![[Pasted image 20230111114732.png]]
CLIPort extends [[*shiny-fm-robotics#Transport-Nets]] with language conditioned tasks. With Transporters they were simply condition on the image with white lines indicating goal positions.
TransporterNets takes an [action-centric approach](https://en.wikipedia.org/wiki/Ecological_psychology) to perception where the objective is to *detect actions* rather than *detect objects* and then learn a policy. Keeping the action-space grounded in the perceptual input allows us to exploit geometric symmetries for efficient representation learning. When combined with CLIP's pre-trained representations, this enables the learning of reusable manipulation skills without any "objectness" assumptions.

## Alfred

[[2-Focus-Areas/Readwise/Articles/ALFRED A Benchmark for Interpreting Grounded Instructions for Everyday Tasks]]
[ALFRED](https://askforalfred.com/) consists of expert demonstrations in interactive visual environments for 25k natural language directives. These directives contain both high-level goals like “Rinse off a mug and place it in the coffee maker.” and low-level language instructions like “Walk to the coffee maker on the right.” ALFRED tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets.
![[Pasted image 20230111162813.png]]
ALFRED evaluation metrics:
Episodes that exceed 1000 steps or cause more than 10 failed actions are terminated.
ALFRED allows us to evaluate both full task and task goal-condition completion. In navigation-only tasks, one can only measure how far the agent is from the goal. In ALFRED, we can also evaluate whether task goal-conditions have been completed, for example that a potato has been sliced. For all of our experiments, we report both Task Success and Goal-Condition Success. Each Goal-Condition relies on multiple instructions, for example navigating to an object and then slicing it.

- Task Success is deﬁned as 1 if the object positions and state changes correspond correctly to the task goal-conditions at the end of the action sequence, and 0 otherwise.
- The goal-condition success of a model is the ratio of goal-conditions completed at the end of an episode to those necessary to have finished a task. For example, in the previous Heat & Place example, there are four goal-conditions. First, a potato must be sliced. Second, a potato slice should become heated. Third, a potato slice should come to rest on a counter top. Fourth, the same potato slice that is heated should be on the counter top.
	- *this could also be used in "skills" benchmarking - did the arm reach a graspable pose?, did the gripper open?, did it pick object up?, was it vertical? --- though it might be more beneficial at the "task" level*
	- On average, tasks in ALFRED have 2.55 goal conditions. The ﬁnal score is calculated as the average goal-condition success of each episode. Task success is 1 only if goal-condition success is 1.

## Behavior Benchmark

[[2-Focus-Areas/Readwise/Articles/BEHAVIOR Benchmark for Everyday Household Activities in Virtual, Interactive, and Ecological Environments]]
![[Pasted image 20230111173433.png]]
Compared with ALFRED it does not contain language but rather this BDDL definition of instructions.

## Rearrangement - Challenge

[[2-Focus-Areas/Readwise/Articles/Rearrangement A Challenge for Embodied AI]]
![[Pasted image 20230112115817.png]]
Interesting set of goal state specifications for every task:

- Geometric goal, image goal, language goal, experience goal, predicate goal
*Some of these might be useful for [[archive/edr/capabilities benchmarking]], ie how do we specify when the skill or task is done*
	- *Predicates goal is similar to your thoughts having read the ALFRED paper - breakdown of skill or task*

## Meta-world

[[Meta-World A Benchmark and Evaluation forMulti-Task and Meta Reinforcement Learning]]
![[Pasted image 20230112134642.png]]
![[Pasted image 20230112142321.png]]
![[Pasted image 20230112155659.png]]
*Some examples of tasks that might be relevant for developing the set of skills/tasks for [[archive/edr/capabilities benchmarking]] as well*

## Benchmarking in Manipulation Research Using the YALE–CMU–BERKELEY Object and Model Set

[[2-Focus-Areas/Readwise/Articles/Benchmarking in Manipulation Research Using the Yale–CMU–Berkeley Object and Model Set]]
Has a good section on other benchmarking object dataset: Columbia grasp dataset, Princeton, Amazon Picking challenge, OpenGRASP etc. Check out their Table 1 for pointers.
[[Pasted image 20230113160617.png|Set of objects & properties]]
[[Pasted image 20230113160728.png|Manipulation Tasks]]
The manipulation protocols described in this paper are very relevant to the way [[archive/edr/capabilities benchmarking]] needs to get setup as well. More specifically - Task Description, Setup description (), Execution Constraints (this is where the constraints you have are introduced)
	[YCB Object and Model Set Homepage](http://www.ycbbenchmarks.org/) - check out some of the example protocols here. Could be useful in specifying setup description for [[archive/edr/capabilities benchmarking]]

## Rlbench: the Robot Learning Benchmark & Learning Environment

[[RLBench_ The Robot Learning Benchmark & Learning Environment]]
[RLBench](https://sites.google.com/corp/view/rlbench)
100 tasks in simulation
Requirements for benchmarking:

- Diversity Reproducibility
- Scale
- Extensibility
- Tiered Difficulty
3 key terms: Tasks, Variations and Episodes
	- Across variations target objects could change while across episodes target locations could change

## Vima: General Robot Manipulation with Multimodal Prompts

[VIMA | General Robot Manipulation with Multimodal Prompts](https://vimalabs.github.io/)
![[Pasted image 20230119135239.png]]
We start with the observation that many robot manipulation tasks can be formulated by multimodal prompts that interleave language and images or video frames (denoted by “{image}” in Fig. 1). For example, [[*shiny-fm-robotics#Rearrangement]], a type of Visual Goal, can be formulated as “Please rearrange objects to match this {scene image}”; Novel Concept Grounding looks like “This is a dax {new object_1} and this is a blicket {new object_2}. Put two metal dax on the marble blicket.”; Few-shot Imitation can embed video snippet in the prompt “Follow this motion trajectory for the wooden cube: {frame1}, {frame2}, {frame3}, {frame4}”; and expressing Visual Constraint is as simple as adding the clause “without touching {safety boundary}”.
	- *This is very similar to how [[*shiny-fm-datasets#Flamingo]] prompts are as well*
We propose VIMA, an embodied agent capable of processing mulitimodal prompts (left) and controlling a robot arm to solve the task (right).
VIMA encodes an input sequence of interleaving textual and visual
prompt tokens with a pretrained language model (Tsimpoukelli et al., 2021), and decodes robot control actions autoregressively for each environment interaction step. The transformer decoder is conditioned on the prompt via cross-attention layers that alternate with the usual causal self-attention. Instead of operating on raw pixels, VIMA adopts an object-centric approach. We parse all images in the prompt or observation into objects by off-the-shelf detectors (He et al., 2017), and flatten them into sequences of object tokens.
Propose VIMA-BENCH built on the Ravens simulator
	- *I think Transporter Nets also created their benchmark on Ravens*
VIMA-BENCH supports extensible collections of objects and textures to compose multimodal prompts and procedurally generate a large number of tasks. Specifically, we provide 17 meta-tasks with multimodal prompt templates, which can be instantiated into 1000s of individual tasks. Each meta-task belongs to one or more of 6 task specification methods mentioned above. VIMA-BENCH can generate large quantities of imitation learning data via scripted oracle agents.
Our approach outperforms strong prior SOTA methods such as [[*shiny-fm-datasets#GATO - 1.2B parameters]], Decision Transformer, and [[*shiny-fm-datasets#Flamingo]] across all 4 levels of zero-shot generalization and all model capacities
We encode the prompt via a frozen pre-trained language model and decode the robot motor commands conditioned on the encoded prompt via cross-attention layers.
There are 3 formats of raw input in the prompt — text, image of a single object, and image of a full tabletop scene (e.g., for Rearrangement or imitation from video frames). For text inputs, we use pre-trained T5 tokenizer and word embedding to obtain word tokens. For images of full scenes, we first extract individual objects using off-the-shelf Mask R-CNN. Each object is represented as a bounding box and a cropped image. We then compute object tokens by encoding them with a bounding box encoder and a ViT, respectively. For images of single objects, we obtain tokens in the same way except with a dummy bounding box.
![[Pasted image 20230119150359.png]]
Trained via behavior cloning
Flamingo is trained to output a language sequence. In order to baseline it for VIMA the authors replace the output layer with robot action heads.
Related work section in the end is quite comprehensive
Appendix has good detail for various tasks that they benchmarked : relevant for [[archive/edr/capabilities benchmarking]]

## [Stacking our way to more general robots](https://www.deepmind.com/blog/stacking-our-way-to-more-general-robots)

Interesting approach where they essentially train a base policy with ground truth state. Then use that base policy to act as a teacher for the second policy that uses realistic observations (and extracts state from that), providing the learning agent with corrections. Then they train a third policy that using offline RL that takes the state transitions from the previous realistic policy by learning a Q function from the good transitions.
	![[Pasted image 20230118141514.png]]![[Pasted image 20230118142016.png]]![[Pasted image 20230118142022.png]]

## RT-2

[[2023-07-28-Friday]]
main novelty of RT-2 compared with RT-1 is the add-on of a VLM while most of the robot training dataset stayed the same. So they had pretty much juiced out the manipulation/action task performance given the dataset already and the biggest gains were in the visuo-linguistic domain rather than purely in the action domain per se. So an EfficientNet architecture was replaced by a much beefier Palm-E & PaLI-X VLM.

## Diffusion Policy

[[2023-09-21-Thursday]]
[2303.04137.pdf](https://arxiv.org/pdf/2303.04137.pdf)
Trained a [[diffusion model]] to produce robot actions. Can be a CNN based diffuser or a Time-series Transformer based one. The latter is similar to [[#RT-2]] but does a denoising on a sequence of actions rather than just producing the next token.
TRI used it for some impressive demos - [Toyota Research Institute Unveils Breakthrough in Teaching Robots New Behaviors | Toyota Research Institute](https://www.tri.global/news/toyota-research-institute-unveils-breakthrough-teaching-robots-new-behaviors)
![[shiny-fm-robotics-2023-09-21.png]]

## RT-1

[[2023-10-03-Tuesday]]
[Scaling up learning across many different robot types](https://www.deepmind.com/blog/scaling-up-learning-across-many-different-robot-types)
Introduces Open X-Embodiment dataset
In this work, we show training a single model on data from multiple embodiments leads to significantly better performance across many robots than those trained on data from individual embodiments.
To investigate the transfer of knowledge across robots, we conduct experiments with our helper robot on tasks that involve objects and skills that are not present in the RT-2 dataset but exist in another dataset for a different robot. Specifically, RT-2-X was three times as successful as our previous best model, RT-2, for emergent skills.
Our results suggest that co-training with data from other platforms imbues RT-2-X with additional skills that were not present in the original dataset, enabling it to perform novel tasks.

## RoboCat

[[2023-10-03-Tuesday]]
[RoboCat: A self-improving robotic agent](https://www.deepmind.com/blog/robocat-a-self-improving-robotic-agent)
RoboCat is based on our multimodal model Gato (Spanish for “cat”), which can process language, images, and actions in both simulated and physical environments. We combined Gato’s architecture with a large training dataset of sequences of images and actions of various robot arms solving hundreds of different tasks.

After this first round of training, we launched RoboCat into a “self-improvement” training cycle with a set of previously unseen tasks.
![[shiny-fm-robotics-2023-10-03.png]]
The combination of all this training means the latest RoboCat is based on a dataset of millions of trajectories, from both real and simulated robotic arms, including self-generated data. We used four different types of robots and many robotic arms to collect vision-based data representing the tasks RoboCat would be trained to perform.

## LINGO-1

[LINGO-1: Exploring Natural Language for Autonomous Driving - Wayve](https://wayve.ai/thinking/lingo-natural-language-autonomous-driving/)
LINGO-1, our open-loop driving commentator, offers an essential first step for enhancing the learning and explainability of our foundation driving models using natural language.
LINGO-1 can provide a description of the driving actions and reasoning.
VLAMs open up the possibility of interacting with driving models through dialogue, where users can ask autonomous vehicles what they are doing and why.
A key feature in the development of LINGO-1 is our creation of a scalable and diverse dataset that incorporates image, language and action data gathered from our expert drivers commentating as they drive around the UK. The commentary technique is reminiscent of roadcraft used by professional driving instructors in their lessons: instructors say interesting aspects of the scene aloud and justify their driving actions using short phrases, helping their students learn by example
When these phrases are temporally synchronised with sensory images and low-level driving actions, we obtain a rich vision-language-action dataset to train models for diverse tasks.
The lack of explainability in machine learning models is a common concern, as the decision-making process often seems like a black box. However, by leveraging language, we can shed light on how AI systems make decisions.

Creating natural language interfaces could allow users to engage in meaningful conversations with AI models, enabling them to question choices and gain insight into scene understanding and decision-making.
The lack of explainability in machine learning models is a common concern, as the decision-making process often seems like a black box. However, by leveraging language, we can shed light on how AI systems make decisions.

Creating natural language interfaces could allow users to engage in meaningful conversations with AI models, enabling them to question choices and gain insight into scene understanding and decision-making.
![[shiny-fm-robotics-2023-10-06.png]]

## VoxPoser

[[2024-04-15-Monday-W16|2024-04-19-Friday]] - [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://huggingface.co/papers/2307.05973)

- In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations
- How can we leverage the wealth of internalized knowledge of LLMs at the even fine-grained action level for robots, without requiring laborious data collection or manual designs for each individual primitive?
	- In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by high-frequency control signals in high-dimensional space. However, we find that LLMs excel at inferring language-conditioned affordances and constraints, and by leveraging their code-writing capabilities, they can compose dense 3D voxel maps that ground them in the visual space by orchestrating perception calls
- By generating Python code to invoke perception APIs, LLMs can obtain spatial-geometric information of relevant objects or parts and then manipulate the 3D voxels to prescribe reward or cost at relevant locations in observation space
- Finally, the composed value maps can serve as objective functions for motion planners to directly synthesize robot trajectories that achieve the given instruction, without requiring additional training data for each task or for the LLM

![[shiny-fm-robotics-2024-04-19.png]]
Overview of VOXPOSER. Given the RGB-D observation of the environment and a language instruction, LLMs generate code, which interacts with VLMs, to produce a sequence of 3D affordance maps and constraint maps (collectively referred to as value maps) grounded in the observation space of the robot (a). The composed value maps then serve as objective functions for motion planners to synthesize trajectories for robot manipulation (b). The entire process does not involve any additional training.

## Pi-0
- [[2024-11-05-Tuesday]] - [Our First Generalist Policy](https://www.physicalintelligence.company/blog/pi0)
	- [pi0.pdf](https://www.physicalintelligence.company/download/pi0.pdf)
	-  in order to make it possible to perform highly dexterous and intricate physical tasks, we use an action chunking architecture with flow matching (a variant of diffusion) to represent complex continuous action distributions. This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding. To combine flow matching with VLMs, we use a novel action expert that augments the standard VLM with flow-based outputs.
	- We further augment this VLM backbone with robotics-specific inputs and outputs — namely, proprioceptive state and robot actions. π0 uses conditional flow matching to model the continuous distribution of actions. Flow matching provides our model with high precision and multimodal modeling capability, making it especially well suited to high-frequency dexterous tasks. Our architecture is inspired by Transfusion, which trains a single transformer using multiple objectives, with tokens1 corresponding to continuous outputs supervised via a flow matching loss and tokens corresponding to discrete outputs supervised via a cross-entropy loss.
	- Since the model generates an entire H-step action chunk at once, we can execute up to H actions before we need to run inference again.
	- ![[pi_0 architecture.png]]
	- *They also mentione pretraining a Robot model and then finetuning it on various different tasks like (laundry folding etc) - kinda similar to instruction finetuning of language models*
	- Uses this VLM - [google/paligemma-3b-pt-896 · Hugging Face](https://huggingface.co/google/paligemma-3b-pt-896) 

## Helix
[Helix: A Vision-Language-Action Model for Generalist Humanoid Control](https://www.figure.ai/news/helix)
![[shiny-fm-robotics-2025-03-04.png]]
Prior approaches face a fundamental tradeoff: VLM backbones are general, but not fast, and robot visuomotor policies are fast but not general. Helix resolves this tradeoff through two complementary systems, trained end-to-end to communicate:
- System 2 (S2): An onboard internet-pretrained VLM operating at 7-9 Hz for scene understanding and language comprehension, enabling broad generalization across objects and contexts.
- System 1 (S1): A fast reactive visuomotor policy that translates the latent semantic representations produced by S2 into precise continuous robot actions at 200 Hz.

S2 is built on a 7B-parameter open-source, open-weight VLM pretrained on internet-scale data. It processes monocular robot images and robot state information (consisting of wrist pose and finger positions) after projecting them into vision-language embedding space. Combined with natural language commands specifying desired behaviors, S2 distills all semantic task-relevant information into a single continuous latent vector, passed to S1 to condition its low-level actions.

S1, an 80M parameter cross-attention encoder-decoder transformer, handles low-level control. It relies on a fully convolutional, multi-scale vision backbone for visual processing, initialized from pretraining done entirely in simulation. While S1 receives the same image and state inputs as S2, it processes them at a higher frequency to enable more responsive closed-loop control. The latent vector from S2 is projected into S1's token space and concatenated with visual features from S1's vision backbone along the sequence dimension, providing task conditioning.
S1 outputs full upper body humanoid control at 200hz, including desired wrist poses, finger flexion and abduction control, and torso and head orientation targets. We append to the action space a synthetic "percentage task completion" action, allowing Helix to predict its own termination condition, which makes it easier to sequence multiple learned behaviors.

Helix is trained fully end-to-end, mapping from raw pixels and text commands to continuous actions with a standard regression loss. Gradients are backpropagated from S1 into S2 via the latent communication vector used to condition S1's behavior, allowing joint optimization of both components.

During training, we add a temporal offset between S1 and S2 inputs. This offset is calibrated to match the gap between S1 and S2's deployed inference latency, ensuring that the real-time control requirements during deployment are accurately reflected in training.

*Trained with ~500 hours of high quality supervised data in total*

## Gemini Robotics
[Gemini Robotics brings AI into the physical world - Google DeepMind](https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/) --- [My Goodnotes markup](https://share.goodnotes.com/s/AlWPWEDRfdcFRQvd79LN4z)
Core contributions:
1. ERQA: An open-source benchmark specifically designed to evaluate embodied reasoning ca-
pabilities of multimodal models, addressing the lack of benchmarks that go beyond assessing
atomic capabilities and facilitating standardized assessment and future research.
2. Gemini Robotics-ER: A VLM demonstrating enhanced embodied reasoning capabilities.
3. Gemini Robotics: A VLA model resulting from the integration of robot action data, enabling
high-frequency dexterous control, robust generalization and fast adaptation across diverse
robotic tasks and embodiments.

Gemini 2.0 Flash and its ER enhanced variant, Gemini Robotics-ER, can be used directly to control robots, as a perception module (e.g., object detection), a planning module (e.g., trajectory generation), and/or to orchestrate robot movements by generating and executing code.

Grasp Prediction: This is a new feature introduced in Gemini Robotics-ER. It extends Gemini 2.0’s pointing capabilities to predict top-down grasps.
![[shiny-fm-robotics-2025-03-19.png]]
*Gemini Robotics-ER is just a variant of Gemini 2.0 that also has grasp prediction as an output. Seems like an incremental update to the already very beefy Gemini 2.0 model. Interesting to see that such a generalist models ability to do basic perception and high level planning (assuming a low level robot control API) already solves so many tasks.*

![[shiny-fm-robotics-2025-03-19-1.png]]
The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms. The on-robot Gemini Robotics decoder compensates for the latency of the backbone. When the backbone and local decoder are combined, the end-to-end latency from raw observations to low-level action chunks is approximately 250ms. With multiple actions in the chunk, the effective control frequency is 50Hz.  
[[#Pi-0]] has a PaliGemma backbone which is an inferior VLM to the Gemini 2.0 used in this work

When we directly train the Gemini Robotics specialist model from scratch using the specialization datasets, we find that it is unable to solve any of these tasks (0% success rates across the board), suggesting that in addition to the high-capacity model architecture, the representation, or the physical common sense, learned from diverse robot action datasets  is another key component for the model to specialize in challenging long-horizon tasks that require a high level of dexterity.

## [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t)
![[shiny-fm-robotics-2025-03-19-2.png]]

# World Model

## Genie-2
Genie 2 is an autoregressive [latent diffusion model](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html), trained on a large video dataset. After passing through an [autoencoder](https://arxiv.org/abs/1312.6114), latent frames from the video are passed to a large [transformer](https://openreview.net/forum?id=YicbFdNTTy) dynamics model, trained with a causal mask similar to that used by large language models.
At inference time, Genie 2 can be sampled in an autoregressive fashion, taking individual actions and past latent frames on a frame-by-frame basis. We use [classifier-free guidance](https://arxiv.org/abs/2207.12598) to improve action controllability.
![[shiny-fm-robotics-2024-12-05.png]]

## NVIDIA Cosmos
[NVIDIA Cosmos | Physical AI Development with World Foundation Models (WFM)](https://www.nvidia.com/en-in/ai/cosmos/)

# Interesting Papers


- [Beyond Predefined Actions: Integrating Behavior Trees and Dynamic Movement Primitives for Robot Learning from Demonstration](https://arxiv.org/html/2505.08625v1)
	- Josh W shared this : BT + DMP with LfD
	- BTs require expert-crafted low-level actions, while DMPs lack high-level task logic.
	- We introduce a new approach for learning both the high-level task structure and associated low-level actions from demonstrations, employing BTs as a compositional structure and DMPs for low-level motion generation. We encapsulate each DMP within a BT action node, leveraging the pre- and post-conditions of the BT nodes to supervise execution.
	- Dynamic Movement Primitives (DMPs) are a flexible framework for learning trajectories from demonstration, representing both periodic and discrete movements.
	- DMPs model the forcing term to generalize trajectories to new start/goal positions while preserving their learned shape.
	- ![[*shiny-fm-robotics-2025-05-20.png]]
	- One trade-off we did not explore in detail in this paper stems from the granularity of learned actions. While the proposed approach produces competent BTs, it does not necessarily optimize the number of action nodes used —a factor that can enhance efficiency and interpretability
	- scalability becomes a concern as tasks grow in complexity, requiring careful design to balance efficiency, reactivity, and system simplicity.

- [State of the art in LLMs + Robotics - 2023 - hlfshell](https://hlfshell.ai/posts/llms-and-robotics-papers-2023/)
- [Benchmarking Augmentation Methods for Learning Robust Navigation Agents: The Winning Entry of the 2021 iGibson Challenge | Readwise](https://embodied-ai.org/papers/2022/10.pdf)
	Nothing too novel other than injecting moving obstacles in the scene for training agents static visual navigation

- [The ThreeDWorld Transport Challenge: A Visually Guided Task-and-Motion Planning Benchmark for Physically Realistic Embodied AI](https://arxiv.org/pdf/2103.14025.pdf)
	We introduce a visually-guided and physics-driven task-and-motion planning benchmark, which we call the ThreeDWorld Transport Challenge. In this challenge, an embodied agent equipped with two 9-DOF articulated arms is spawned randomly in a simulated physical home environment. The agent is required to ﬁnd a small set of objects scattered around the house, pick them up, and transport them to a desired ﬁnal location. We also position containers around the house that can be used as tools to assist with transporting objects efﬁciently.

- [JRDB: A Dataset and Benchmark of Egocentric Robot Visual Perception of Humans in Built Environments](https://arxiv.org/pdf/1910.11792.pdf)
	JackRabbot Dataset and Benchmark (JRDB), a novel dataset and several visual benchmarks associated to it. Our dataset contains 64 minutes of sensor data acquired from our mobile robot JackRabbot2 comprising 54 sequences indoors and outdoors in a university campus environment.
	Based on this annotations, we provide a uniﬁed and standardized benchmark for 2D-3D person detection and tracking. Our 2D-3D person detection and tracking benchmark supports the evaluation of computer vision algorithms for object detection, 3D orientation estimation, and multi-object tracking.
	Most of the benchmark metrics are pretty standard vision ones: IoU, mAP, MOTA/MOTP(multiple object tracking accuracy / precision) etc.

- [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/pdf/2011.07215.pdf)
	we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and a Python interface for creating new environments.
	Robotic manipulation of deformable objects has wide application both in our daily lives, such as folding laundry and making food, and in industrial applications, such as packaging or handling cables. However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation and complex dynamics
	For deformable object manipulation, the robot must operate directly on its observations, which can include camera images and other sensors.
	SoftGym includes 10 challenging environments involving manipulation of rope, cloth and ﬂuid of variable properties, with different options for the state and action spaces.
	![[Pasted image 20230112164157.png]]
	![[Pasted image 20230112164025.png]]

- [Interactive Gibson Benchmark](https://sites.google.com/corp/view/interactivegibsonenv) - navigation focussed
	Interactive Gibson Benchmark, the ﬁrst comprehensive benchmark for training and evaluating Interactive Navigation solutions. Interactive Navigation tasks are robot navigation problems where physical interaction with objects (e.g. pushing) is allowed and even encouraged to reach the goal.
	![[Pasted image 20230112170706.png]]

- [CausalAgents: A Robustness Benchmark for Motion Forecasting](https://arxiv.org/pdf/2207.03586.pdf)
	we conduct an extensive labeling eﬀort to identify causal agents, or agents whose presence inﬂuences human drivers’ behavior in any format, in the Waymo Open Motion Dataset (WOMD), and we use these labels to perturb the data by deleting non-causal agents from the scene.
	We release the causal agent labels from human labelers as additional attributes to WOMD so that researchers can utilize the causal relationships between the agents for robustness evaluation and for other tasks such as agents relevance or ranking
	*They have interesting reasons in the Discussions section on why models fail due to perturbations. Big reasons are: i) overfitting - they latch onto spurious features in the scene or overrely on weird features in the scene.
	ii) distribution shift - removing the number of agents from the scene causes the model to freak out because the training data contained more agents.
	I guess this is expected of end-to-end trained blackboz models that dont have interpretability

- [Diffuser: Reinforcement Learning with Diffusion Models](https://diffusion-planning.github.io/)
	Interesting approach in using generative modeling in place of traditional robotics planning algorithms.
