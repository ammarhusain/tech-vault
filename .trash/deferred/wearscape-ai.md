---
created: 2023-04-24-Monday 07:58
modified: 2023-05-03-Wednesday 12:36
publish: 
---

**Working [Doc](https://docs.google.com/document/d/1fdUZrABzHO9-UGp9nsltoyrDG3jPwA_lalI6Occ6eBY/edit#heading=h.6tdzvra15rr9)**

---

Sandbox notebook - [[wearscape-ai-sandbox-2023-05-03.ipynb]]

[[2023-08-02-Wednesday]]
Taichi NerF - Library for 3D rendering and Python GPU kernels

[[2023-06-08-Thursday]]
Met with Nishanth - [Drive link](https://drive.google.com/drive/folders/1my9DuFvMHVJOsyO1yHTtW4wMqCKtLCc8)

[[2023-05-26-Friday]]
Met with Nishanth - chatted a bunch on building faithful mesh representations for gestures. 

[[2023-05-22-Monday]]
[GitHub - openai/shap-e: Generate 3D objects conditioned on text or images](https://github.com/openai/shap-e)

[[2023-05-16-Tuesday]]
Could this be relevant for hand image generation - [GitHub - deep-floyd/IF](https://github.com/deep-floyd/IF)

[[2023-05-04-Thursday]] Met up with Nishanth today - discussed MANO hand mesh model from Max Plank Inst.
Was also interested in conventiontional tracking methods - this might be useful : [GitHub - gaomingqi/Track-Anything: Track-Anything is a flexible and interactive tool for video object tracking and segmentation, based on Segment Anything, XMem, and E2FGVI.](https://github.com/gaomingqi/Track-Anything)

[[2023-05-03-Wednesday]]
Read [[*shiny-fm-datasets#Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models - NVIDIA]] - not sure if it is helpful atm : results look meh and also model is not available open source


- [x] subscribe to colab pro ✅ 2023-05-03
- [x] run chinese modelscape video LDM ✅ 2023-05-03
Playing around with: [damo-vilab/text-to-video-ms-1.7b · Hugging Face](https://huggingface.co/damo-vilab/text-to-video-ms-1.7b)
![[wearscape-ai-2023-05-03.mp4]]

- [x] read the 3DFuse website and try their demo in colab ✅ 2023-05-03
	- [ ] HuggingFace demo does not work, emailed author to find out about colab
- [ ] This approach looks interesting - [GitHub - lzzcd001/MeshDiffusion: Official implementation of "MeshDiffusion: Score-based Generative 3D Mesh Modeling" (ICLR 2023 Spotlight)](https://github.com/lzzcd001/MeshDiffusion)

Steps to take:

- Generate video sequence of pinch or other hand gestures
- Segment out hand using SAM or SEEM
- How do you generate mesh?
	- Could you create a NerF first and then meshify? - [[*shiny-fm-datasets#3DFuse]]
		- #sandbox [3DFuse - a Hugging Face Space by jyseo](https://huggingface.co/spaces/jyseo/3DFuse)

[[2023-04-28-Friday]] - met up with Nishanth ^9588e2

[[2023-04-24-Monday]]- Use SAM to segment out the hand in video. How can we produce a mesh from this video?
We could use DINO v2 for depth estimation of the hand. Stitching multiple together might be able to produce a mesh.
There is also NVIDIAs research for video generation - [Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models](https://research.nvidia.com/labs/toronto-ai/VideoLDM/?utm_source=substack&utm_medium=email)

[[2023-04-21-Friday]] - [[2-Focus-Areas/Readwise/Articles/Neural Radiance Field (NeRF) A Gentle Introduction]] is not really the best representation because it is more for view synthesis


# Legal stuff
[[Wearscape, Inc. - RSP Agreement (Umri LLC)-4150-0936-7367-v1.docx.pdf]]
[[wearscape-ai-2023-05-22.pdf]]
[[Certificate CS-3 for Umri LLC.pdf]]
[[Wearscape, Inc. - 2023 Stock Plan.pdf]]
[[RSP Agreement (Umri LLC) - 2023.05.20.pdf]]