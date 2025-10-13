---
created: 2023-09-17-Sunday 19:05
modified: 2023-09-17-Sunday 19:05
publish: 
---
[[2024-03-20-Wednesday]]
Found he video that inspired HI - could also be useful for [[archive/apple/attentionkit-fc]]
[TikTok - Make Your Day](https://www.tiktok.com/@la_rushka/video/7049770979953839361)

[[2023-11-07-Tuesday]]
Mark Pauley Lit review: ![[archive/apple/attachments/LLM-CharacterInteraction-Photographer.key]]

[[2023-11-03-Friday]]
A more updated synthetic dataset from Xin
![[archive/apple/attachments/vicuna-13b-v1.5-16k-multi-scenario_a.json]]
Data format described in this [quip](https://quip-apple.com/kaObAaCFJIDi)

[[2023-10-20-Friday]]
Some simple dummy datasets for photographer [[*shiny-fm-datasets#Dummy Datasets]]
![[archive/apple/attachments/photo_train.json]]
![[archive/apple/attachments/photo_val.json]]
![[archive/apple/attachments/photographer-structured.json]]

[[2023-10-02-Monday]]
For Kevin demo: commands to run on superserver
ssh -L 8080:localhost:8080 local@superserver.corp.apple.com

cd ~/EmbodiedReasoning/VLMs/SceneUnderstanding
conda activate vlm
uvicorn photographer-websocket:app --reload --host 0.0.0.0 --port 8080

[[2023-09-13-Wednesday]]
From Floris Chabert
Offline tooling: idprint - [https://github.pie.apple.com/siml-hour/idprint](https://github.pie.apple.com/siml-hour/idprint)  
VisualUnderstanding framework - [https://github.pie.apple.com/siml-hour/VisualUnderstanding](https://github.pie.apple.com/siml-hour/VisualUnderstanding)
VU docs: [http://at.apple.com/vu](http://at.apple.com/vu)
![[archive/apple/attachments/_Identity._004.jpeg]]![[archive/apple/attachments/_Identity._003.jpeg]]
![[archive/apple/attachments/_Identity._002.jpeg]]![[archive/apple/attachments/_Identity._001.jpeg]]
From Abhishek Singh:
For gaze models, please see: [https://github.pie.apple.com/dangdang-shao/scenegaze-runner](https://github.pie.apple.com/dangdang-shao/scenegaze-runner)  
In the build, you can try out VNDetectFaceGazeRequest on a recent DawnBurst build
# Reference Links
[Core Image | Apple Developer Documentation](https://developer.apple.com/documentation/coreimage)
