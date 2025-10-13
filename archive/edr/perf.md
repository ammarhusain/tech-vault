---
aliases: []
created: 2022-10-03-Monday 19:12
modified: 2023-03-10-Friday 23:15
tags: 
---

# 2022

[[archive/edr/attachments/Husain, Ammar - 2023 Q1 Performance Evaluation - Employee View.pdf]]

## Snippets

[[ammarh] EDR Performance Evaluation Template (revised 12/21/2022) - Google Docs](https://docs.google.com/document/d/1PV2X8s1vO9zksl4NqJWr_ZQBc-78z6XB_8OE93ZAN-4/edit#)
[Engineering-Wide Leveling Guide (go/engleveling) - Google Docs](https://docs.google.com/document/d/1Z2MDAkANByIJNJcbn6frojCt0G766U1agRqtf__LeBk/preview)
[[career/management|Product Manager]] - [PM artifacts - ammarh@ - Google Docs](https://docs.google.com/document/d/14o0d74pKaNj6flfNGqilpw-2bDIdoM_njbM3hGzBJgg/edit?resourcekey=0-BbwWP5UIpZfo9xYQO2blQw#heading=h.9kxog64sha6)
[Autonomy, Reasoning & HiTL notes - Google Docs](https://docs.google.com/document/d/1Oo0DQiMzFqwxTOmauq5IXVJQXiVUAh_1EUeXI8dz10o/edit)

- [[2021-11-09-Tuesday]] : [TOCC presentation](https://docs.google.com/presentation/d/1SN-Q_vFxljeZaBdbn0h9JC8Zo-bePhXP4sAGl33SM5A/edit?resourcekey=0-sQKmZys866K_UZesIjk6xg#slide=id.gd5278b9f66_1_543) for calibration
- [[2021-11-16-Tuesday]] : [TOCC presentation](https://docs.google.com/presentation/d/1hHmiTTDsxS0yHtHp4yHX9qoDpZH-3JktwLQchec2Jgs/edit?resourcekey=0-1HaW4LYegFMmtiYFTj7wBA#slide=id.gd5278b9f66_1_543) for calibration impact on base planners
- [[2021-12-04-Saturday]] : Migrated [legacy snippets](https://docs.google.com/document/d/1wOq0TMNHIHntr91wCEPua7w_4cwhE6YefVliwIMdSV4/edit?resourcekey=0-VadqY9IBonLxOJyyulRHfg#) from before March 2021
- [[2022-02-23-Wednesday]] : Helped Guy and Maxim solve this P1: [b/216488914](https://b.corp.google.com/216488914), [b/204582120](http://b/204582120)

# 2021

[[archive/edr/attachments/2021_Q3_Performance_Evaluation_ammarh_Employee_View.pdf]]

## Snippets
- Successful delivery of [cafe dishcart towing (sim): okr q4'20](https://www.notion.so/cafe-dishcart-towing-sim-okr-q4-20-f9e153e45f084f67b2505375f02663be)
- Claim as big impact for setting the vision/requirements for ScaleAI and Viz mk2 integration: go/proxy-scaleai-vizmk2
- PR55 doorway navigation [highlight](https://docs.google.com/presentation/d/1se3ody5hlPZFjOWalg8DY8SSg1OUfrasq32oYUx8Up0/edit?resourcekey=0-2AVm7I1xtp3WZsTgpuVapA#slide=id.gd8a8d709f8_1_0)
- navigation perception user guide [highlight](https://docs.google.com/presentation/d/1se3ody5hlPZFjOWalg8DY8SSg1OUfrasq32oYUx8Up0/edit?resourcekey=0-2AVm7I1xtp3WZsTgpuVapA#slide=id.gdf9c1dfbe0_0_0)
- panoptic segmentation + hifi [highlight](https://docs.google.com/presentation/d/1se3ody5hlPZFjOWalg8DY8SSg1OUfrasq32oYUx8Up0/edit?resourcekey=0-2AVm7I1xtp3WZsTgpuVapA#slide=id.ge13418cb2e_1_0)
- [[2021-07-12-Monday]]: hifi cbr [highlight](https://docs.google.com/presentation/d/1w1DZy9BTK3CLjHJET4bMgZhy3jaOp25LC-SDP_ZZhik/edit?resourcekey=0-j6zNhtjzxor5ZU5ZmJmIIg#slide=id.ge400353f1f_2_0)
- [[2021-07-31-Saturday]] : [SW university course](https://drive.google.com/open?id=1e8x4dHUzdiWz65LEiYQ6v-AWpwQzfRQL&authuser=mrahusain%40gmail.com&usp=drive_fs) on navigation perception
- 3 Patent disclosures
- Perception points for navigation and sim datagen benchmark : [highlight](https://docs.google.com/presentation/d/1w1DZy9BTK3CLjHJET4bMgZhy3jaOp25LC-SDP_ZZhik/edit?resourcekey=0-j6zNhtjzxor5ZU5ZmJmIIg#slide=id.gead2e2bd76_0_9)
- hifi map + base planner ripper [highlight](https://docs.google.com/presentation/d/1w1DZy9BTK3CLjHJET4bMgZhy3jaOp25LC-SDP_ZZhik/edit?resourcekey=0-j6zNhtjzxor5ZU5ZmJmIIg#slide=id.geed48a14b3_4_0)
- proxy mapping limitations [highlight](https://docs.google.com/presentation/d/1w1DZy9BTK3CLjHJET4bMgZhy3jaOp25LC-SDP_ZZhik/edit?resourcekey=0-j6zNhtjzxor5ZU5ZmJmIIg#slide=id.geed48a14b3_4_64)
- b/173421389 : Stop sign freaks out the MetA robots in PR55
			  ![[archive/edr/attachments/Untitled.png|400]]

# 2020

[[archive/edr/attachments/2020_Q3_Perf_Eval_ammarh_Employee_Assessment_View.pdf|2020 - Q3]]

## Snippets
- Message Sync library implemented & in good use.
- Migrated several modules to use Message Sync. 2 rippers, nav_perception, auto_look, camera_stereo etc.
- Established a principles triage process for navigation bugs (Nav Field Triage Doctrine): Spun up Mitri, established reporting structure & bug taxonomy.
- Found a bug in single process (no ipc) log playback that was recursively calling callbacks. Added a delayed publishing into SendTransforms for TransformBroadcaster to fix that issue.
- Wrote a Proxy ToTW for transform publishing in tests to highlight bug fix above ^.
- Refactored scenario evaluator interface to a CRTP class design with variant to add more evaluation types. Added NavigationConditionEvaluator.
- Setting up process around scenario eval pipeline & automation (through Mitri, Olga, Gale).
- Dug into Grok builds and fixed XRefs in camera_stereo
- Submitted HDRNet + JPEG processing for WFOV camera.
	- ![[archive/edr/attachments/wfov-seg-1.png]]
	- ![[archive/edr/attachments/wfov-seg-2.png]]
	- ![[archive/edr/attachments/wfov-seg-3.png]]
- MessageSynchronizer TotW
- YAQS doc score: [](https://dashboards.corp.google.com/_6bfa8dd4_d516_4766_b0fc_e484eb1bd521)[https://dashboards.corp.google.com/_6bfa8dd4_d516_4766_b0fc_e484eb1bd521](https://dashboards.corp.google.com/_6bfa8dd4_d516_4766_b0fc_e484eb1bd521)
- [Proxy Townhall](https://docs.google.com/presentation/d/17AQpxOMJZC8jBmwnQdUTErZh-Zo96oIlBldaXz8mF2M/edit#slide=id.g90f60b34bf_1_33820) talk
- TOCC talk : [[2020-07-23-Thursday]]

# 2019

[[archive/edr/attachments/2019_Q3_Perf_Eval_ammarh_Employee_View.pdf|2019 - Q3]]
[[archive/edr/attachments/2019_Q1_Perf_Eval_ammarh_Employee_View.pdf|2019 - Q1]]

## Snippets
- Corrected a codelab sample & got CL approved from Titus for Dean#2
- Read up & learned the GJK collision check algorithm for code review
- Removed OpenCV dependency for image warping in nav-perception
- Due process on enabling ramps : 1pager -> implementation -> testing (local & REWS)
- Spent a bunch of time triaging when the camera_stereo bug was introduced at the same time as the ramps CL
- AutoLook: Design doc -> Design Review -> Implementation steps
- Came 2nd place in Proto-plasmic fixit week
- Migrated visualization colors & configs for navigation perception to easier modify color schemes. Will be used for triaging since camera, cbr & information & quasi_static grid points have different colors.
- AutoLook: Debug visualization markers & simple priority queue implementation.
- Hulls for: (i) CBr blindspot, (ii) Stereo blindspot (base), (iii) Stereo blindspot (arm)
- Found 2 bugs: Sim camera runs at 2Hz, Camera point cloud segmentation had points with z forward so the delta_z check in discontinuous points was failing.
- Filed 2 patent applications: [X-51285-00-US & X-51286-00-US](https://docs.google.com/spreadsheets/d/1ADulKrGxBKrh86rM2jWhqjjCRqaPho--ViipDyi5VpE/edit?usp=sharing)
- AutoLook released first phase

# Canonical Packages

[[archive/edr/attachments/X_Canonical_Packet_Example_(L5_-_L6)_-_Pavel_Vodenski_(2017_Q3).pdf]]
[[archive/edr/attachments/Yunfei Promo Packet L6-_L7 - Share.pdf]]

