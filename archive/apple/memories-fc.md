---
publish: 
created: 2024-10-18-Friday 11:54
modified: 2024-10-18-Friday 11:56
---

### Resources

![[archive/apple/attachments/memories-fc M0-S2 plans.png]]

- HI Golden conversation [doc](https://quip-apple.com/xtbxACycAM81)
- To run memories in the OpenAI console: [openai-realtime-console](file:///Users/ammarh/j595/openai-realtime-console)
	- `npm start` on one terminal; `npm run relay` on another 
- Built from scratch using OpenAI relatime API: [openai-api-node-demo](file:///Users/ammarh/j595/openai-api-node-demo)
	- Tutorial: https://www.datacamp.com/tutorial/realtime-api-openai
	- Working with WebSockets requires us to program in an event-driven way. Messages are sent back and forth on the communication channel, and we cannot control when these messages will be delivered or received.
- Sri's docs on memories:
	- [Conversational Memory Problem](https://quip-apple.com/TsuzALrQaC8z)
	- [Approaches to conversational memory](https://quip-apple.com/RQFbAbuXrN0n)
### Artifacts
[[2025-08-12-Tuesday]] - [[attachments/Deep Lunching - eval this.key]]
[[2024-10-24-Thursday]] [[archive/apple/attachments/oai realtime console - memories prototype oct 24.mp4]] - good video!
[[2024-10-17-Thursday]] - [[oai realtime console - memories prototype oct 17.mov]] ([memories - oai realtime console prototype.mp4](file:///Users/ammarh/Library/Mobile%20Documents/com~apple~icloud~applecorporate/Documents/j595-docs/memory/memories%20-%20oai%20realtime%20console%20prototype.mp4)) - no audio :(

### Logs
- [[2025-06-27-Friday]] - Chaitanya & Sri: scenario planner outputs the conversation goals + expected conversation. Its like an encoder that has the full persona, history etc while the conversation simulator is more like a decoder - its auto regressive: tries to just pull in whatever is in the context and makes a decision. 
- [[2025-06-25-Wednesday]] Chat with Sri & Ben on memory metrics
	- [Quip](https://quip-apple.com/Z12aAfbSeb3y)
	- 2D plot (heatmap) of time vs saliency - you should remember highly salient and/or more recent events

```dataviewjs 
let pages_foo = dv.pages('"Daily"').sort(p => p.file.name, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#j595/memories"))))
}
```
