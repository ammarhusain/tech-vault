---
aliases: []
created: 2023-01-03-Tuesday 10:54
modified: 2023-03-10-Friday 23:15
tags: 
---


**Linked by:**

**Related To:**

---

- [x] Get a handle on policy papers: Transporter-Nets, BC-Z, CLIPPort ✅ 2023-01-11
- [x] Get a handle on the Benchmark papers: ALFRED, BEHAVIOR, Raven (from transporter & CLIPPort paper) ✅ 2023-01-11
  - [x] Discovered 7 other benchmark papers - skim through them ✅ 2023-01-12
  - [x] 4 more papers: GLUE, RLBench, CausalAgents & one from sidd srinivasa et al on benchmarking (old one) ✅ 2023-01-18
	- [x] Finished RLBench, CausalAgents & Yale-CMU paper. GLUE left. ✅ 2023-01-13
- [ ] Update capabilities benchmarking deck with refreshed definitions
- [ ] Update illustrations of capabilities benchmarking deck -> This should probably be re-worded to "skills" real-world/sim benchmarking (even the note)
	- Need to balance hardcoding/constraining it too much or leaving it too open ended (like test within service)
- [ ] Look at the language in the Ravens benchmark from [[*shiny-fm-robotics#Transport-Nets]] paper (sec 6.3) to come up with benchmark language. [Reader](https://read.readwise.io/archive/read/01gpf39cwhbwmgdtahc0d363fk), also section A of [[*shiny-fm-robotics#CLIPort]] - [Reader](https://read.readwise.io/new/read/01gpf2t566zncvs29cvgs159wm)
	- ![[Pasted image 20230111120025.png]]
	- Above ^ is the table for tasks from the Ravens benchmark ([[*shiny-fm-robotics#Transport-Nets]] paper). We could envision creating something like this for [[archive/edr/capabilities benchmarking]] - pick-small-objects-seen, pick-small-objects-unseen where the small objects fit within a certain min & max size.

[[2023-01-13-Friday]]
Distill out the key components:

1. Task description (pick a small object, pick small object from enclosed space etc),
2. Setup description (10-15 initial configurations of objects in the scene etc)
3. Execution constraints (workspace, size etc),
4. Task/skill predicates - breakdown into component pieces to measure success (arm reached object? - see comment on [[*shiny-fm-robotics#ALFRED]] )
5. Metrics / scoring

Pick & place should perhaps be combined into one task? what about carrying an object as a skill

Use the term "variation" (from RLBench) for distinguishing "pick a coke can" vs "pick a pepsi can":
	- Tasks, Variations & Episodes

[[2023-01-12-Thursday]] - Reading through [[*shiny-fm-robotics#Meta-World]] it seems to me that we should have both skills level benchmarks (pick, push, place etc) and task level benchmarks (wipe, stock etc) -> task level more closely tied with current services ofc.

[[2023-01-11-Wednesday]]
Benchmarks : [[*shiny-fm-robotics#ALFRED]] has examples more akin to "Tasks" while Raven (from Transporter Nets) are more akin to "Skills"
[[*shiny-fm-robotics#ALFRED]] has useful task success and goal conditioned success metrics to leverage per skill.

Both [[*shiny-fm-robotics#ALFRED]] & [[*shiny-fm-robotics#BEHAVIOR]] are benchmarks in simulation. We need something like that in the real world. Thats probably what MkBot does.

[[2023-01-10-Tuesday]] Reading through [[*shiny-fm-robotics#BC-Z]] perhaps we could call Imitation Learning as a capability and "pick & place" as a skill.

Some thoughts that Srikanth had put towards capabilities & autonomy: [Autonomy Framework v2](https://docs.google.com/presentation/d/1SlP9k6leDT9padh4ilNuPOtk64I_8HUmOMvkDV_wIZo/edit?resourcekey=0-Ahvz1jul0VTq6XlItLrcUA#slide=id.gd01b71d4cc_0_0)

# Google Brain

## Apprenticebots

[ApprenticeBots moonshot proposal - Google Docs](https://docs.google.com/document/d/1diwC5oDz7UdSoDAmYTsWnTUYlSiVakM0wPoeYtlr1c4/edit?resourcekey=0-8e6BTyiqAwAAVVu3rAVWRQ#)
![[Pasted image 20230104121212.png]]
The core of our approach – i) leveraging existing foundation models for effectively teaching robotics (High-level Planning), ii) leveraging the data from teaching to develop a robotics foundation model (Low-level Control)

[Benchmark Definition: ApprenticeMeta - Google Slides](https://docs.google.com/presentation/d/1xU3aUvmlGXAsSPO2mwLkyNmMuTMNqDc6d2KasndZVdg/edit?resourcekey=0-LL-BNunMfyZENjow-nhiUQ#slide=id.g16639a92ac5_0_26)
Similar to our last benchmark, we would like to measure a number of quantitative metrics such as completion time, task reward, total number of successfully completed tasks, as well as total number of successfully completed long-horizon tasks. In addition, we will measure qualitative metrics such as Likert ratings of questions about perceived usefulness of the robot, robot’s intent, capabilities, and human-robot trust. We will average these metrics over 10 trials.
[Benchmark Definition: ApprenticeMeta - Google Slides](https://docs.google.com/presentation/d/1xU3aUvmlGXAsSPO2mwLkyNmMuTMNqDc6d2KasndZVdg/edit?resourcekey=0-LL-BNunMfyZENjow-nhiUQ#slide=id.g16639a92ac5_0_96)
[Locomotion North Star: Assistive Dog Benchmark - Google Slides](https://docs.google.com/presentation/d/1iSrqz5e7lIvHyOuXOlSNTC54t_DIN1jPl-lQtFornmI/edit#slide=id.g15fe14b88c0_0_1742)
[HostBot Proposal - Google Slides](https://docs.google.com/presentation/d/1bByaAXvHBP6ta7Mqzuy9NLIQtsgsISPUlo1z6q18vyE/edit?resourcekey=0-SRPdFMnIDg_c6KrKNYM3NQ#slide=id.g18731a4afc_0_0)

[What is benchmarking? - YouTube](https://www.youtube.com/watch?v=AkGwJSlkpfY)
Making meaningful comparisons to others (usually "best in class" or reference points), and identifying opportunities to improve.

[The Difference Between KPIs And Benchmarking - YouTube](https://www.youtube.com/watch?v=qo1R_HEnGp8)
Benchmarking compare your own performance against others
KPI is a metric that helps you track your progress against your own strategic goals (inward focus)
	How well are we grasping? how fast are we navigating? system latencies etc
Benchmarking can help define the right targets for your KPIs. whats the current benchmark or best practice for your industry? this can help inform targets
If you have KPIs that you want to track, then you should try benchmark those as well.
10 Mistakes with KPIs:

1. KPIs aren't linked to strategy.
2. Executives aren't involved with KPI creation to answer their Key Performance Questions. 3
3. . KPIs measure only easy metrics but not important ones.
4. Measure everything. Important KPIs are not prioritized.
5. Strategic and Operational Metrics are mixed in the same dashboard.
6. External metrics are mixed as well. Even if company has no control over them.
7. KPIs are not turned into targets.
8. Not analyzing KPIs.
9. Not updating KPIs.
10. Not acting on the indicators.

**From Josh:**
[Robot Platform Capabilities - 2022 & Beyond - EDR - Google Sheets](https://docs.google.com/spreadsheets/d/1HHGj89_OSRGJssHFsfAm6U0S-xfXVrmrRx1NbBGfk0g/edit#gid=0)

**Zoo stuff that Ben has been working on**
[go/state-of-the-zoo](https://edr.viapeople.net/via/servlet/vp?app=info&reqapp=security_report&cmd=link_redirect&orgId=177&url=http%3A%2F%2Fgoto.google.com%2Fstate-of-the-zoo), [go/edr-zoo-v3](https://edr.viapeople.net/via/servlet/vp?app=info&reqapp=security_report&cmd=link_redirect&orgId=177&url=http%3A%2F%2Fgoto.google.com%2Fedr-zoo-v3), [go/edr-zoo-v3-slides](https://edr.viapeople.net/via/servlet/vp?app=info&reqapp=security_report&cmd=link_redirect&orgId=177&url=http%3A%2F%2Fgoto.google.com%2Fedr-zoo-v3-slides), [go/edr-zoo-v3-taskflow](https://edr.viapeople.net/via/servlet/vp?app=info&reqapp=security_report&cmd=link_redirect&orgId=177&url=http%3A%2F%2Fgoto.google.com%2Fedr-zoo-v3-taskflow)
