---
created: 2022-09-01-Thursday 17:22
modified: 2023-03-29-Wednesday 09:36
---
[Search Patents - Justia Patents Search](https://patents.justia.com/search?q=ammar+husain)
Google [Patents page](https://patents.google.com/?inventor=Ammar+Husain)
# Everyday Robots - Google X

# On-robot Data Collection

[[career/attachments/IDF-52505_X-52505-00-PR_MBHB_22-0900-US-PRO.pdf]]
[[career/attachments/Signed-Copy_X-52505-00-U.pdf]]
# Learning an Ego State Model through Perceptual Boosting

[[career/attachments/X-52506-00-PR (MBHB 22-0901-US-PRO) Draft Application - Learning an ego state model through perceptual boosting.pdf]]
[[career/attachments/X-52506-00-PR-US-PRO figures.vsd.pdf]]

# Learning from Demonstration for Determining Robot Perception Motion

[[career/attachments/21-0619-US-PRO Draft Specification - Google Docs.pdf]]
[[career/attachments/21-0619-US_Drawings_.pdf]]
[[career/attachments/21-0619-US_Specification.pdf]]
[[career/attachments/21-0619-US_Declarations_.pdf]]

## Provisional Filing

[[career/attachments/21-0619-US-PRO Draft Specification.pdf]]
[[career/attachments/21-0619-US-PRO_Figures.pdf]]
[[career/attachments/21-0619-US-PRO Disclosure Memo.pdf]]

**IDF-51836** - [[2021-09-21-Tuesday]]
[[career/attachments/IDF-51836_X-51836-00-PR_MBHB_21-0619-US-PRO.pdf]]

**Supplemental docs**
[[career/attachments/21-0619-US-PRO_Disclosure_Memo.pdf]]
[[career/attachments/Design_Doc__AutoLook_-_Google_Docs.pdf]]
[[career/attachments/Learning_from_demonstration_for_head_motion_-_Google_Docs.pdf]]

# Preventing Regressions in Navigation Determinations Using Logged Trajectories

## Provisional Filing

[[2021-09-24-Friday]]
[[career/attachments/21-0651-US-PRO Draft Specification.pdf]]
[[career/attachments/21-0651-US-PRO_Figures.pdf]]
[[career/attachments/21-0651-US-PRO Disclosure Memo.pdf]]
[[career/attachments/IDF-51977_X-51977-00-US_MBHB_21-0651-US_As.pdf]]
[[career/attachments/IDF-51977-May.07.2021_04-53_PM.pdf]]
**Rough Idea**
Semi automated tuning of navigation heuristics based on robot logs of perception & navigated trajectories

- We might tune some parameters for a new environment but it may cause regressions on our existing environments.
- However we can find these new heuristics by running through a testing framework that computes how many newly failed trajectories were caused.

# Joint Training of a Narrow Field of view Sensor with a Global Map for Broader Context

[[career/attachments/20-1942_Drawings.pdf]]
[[career/attachments/20-1942_Specification.pdf]]
IDF-51705

## Using Adjustable Vision Component for On-demand Vision Data Capture of Areas along a Predicted Trajectory of a Robot

US PTO link : [Just a moment...](https://uspto.report/patent/app/20210080970)

- IDF-51285 Active exploration of areas with perception uncertainty + Ego motion planning to minimize perception obstruction

## Generating AND/OR Using Training Instances that Include Previously Captured Robot Vision Data and Drivability Labels

[[career/attachments/X-51286-00-US_ApplicationDrawings.pdf]]

- IDF-51286 Learning drivable areas in images for indoor environments + Training data generation from previous mapped observations

[[2024-01-21-Sunday]]: Final patent issued - [[career/attachments/US Final Patent 11,741,336 B2.pdf]]
# Filing

[Patent harvest spreadsheet](https://docs.google.com/spreadsheets/d/1jDzf6Ql6Liz0CXcWYk14RLhlDQvbq07IkbhEmYYv2Q4/edit#gid=0)

May 4, 2021

**Use the track eraser for drivability estimation and false positive rejection**

- Just take the areas where the track eraser was applied and store it as a separate mask. This mask could be used in the future for rejecting false positives or help another robot with its drivability estimates. Let's say ramps are challenging. But we observe people walking on ramps.

---
