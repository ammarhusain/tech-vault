---
created: 2023-03-22-Wednesday 17:29
modified: 2023-03-24-Friday 07:51
---

# Ammar Husain

**Location:** San Francisco, CA ; **Email:** [self@ammarh.io](mailto:self@ammarh.io) ; **Cell#:** (217) 819-9101
**Website:** [www.ammarh.io](http://www.ammarh.io) ; **Digital-Brain:** https://notes.ammarh.io ; 
[**Resume**](https://notes.ammarh.io/resume) ; [**LinkedIn**](https://www.linkedin.com/in/husainammar/) ; [**GitHub**](https://github.com/ammarhusain)

Experienced technology lead, software engineer, and tinkerer with deep expertise in embodied and general AI/ML. I thrive in roles that involve developing state of the art technology and are at the intersection of applied research with a product focus.

## Selected Projects
### Search Engine - Digital Brain
[Live Demo](https://second-brain-web-search.herokuapp.com/), [Code](https://github.com/ammarhusain/second-brain-web-search) 
- Built a search engine for my [publicly shared notes](https://publish.obsidian.md/ammar/public-command-center) in [Obsidian](https://obsidian.md/) . In an effort to work with the "garage door open" I host my technical notes on all topics online.
- Created an embedding data store on [Pinecone](https://www.pinecone.io/) by parsing the relevant text chunks from notes and creating their vector embeddings - using the OpenAI API. Embeddings with their relevant metadata are refreshed by a cron job every morning with latest batch of notes.
- Developed a Flask app to query embeddings database for the most semantically relevant notes for the users searched text.
- Incorporated the [GPT-4](https://platform.openai.com/docs/models/gpt-4) completions API with a prompt engineered context to provide a succinct answer based only on the retrieved notes. This search works great and has become my primary workflow to search semantically in my knowledge store compared to the keyword based search Obsidian provides.

### ChatBot
[Live Demo](https://ammarh-ai-playground.herokuapp.com/), [Code](https://github.com/ammarhusain/ai-playground), [Blog](https://medium.com/@mrahusain/fine-tuning-gpt-3-to-talk-like-you-c9bad43eb20)
- [Fine-tuned](https://platform.openai.com/docs/guides/fine-tuning) a OpenAI GPT-3 base model with prompt and completions from my chat history to build an interactive chatbot that generated text akin to the internet slang I used in my teenage years. This pre-dated ChatGPT.
- Parsed several chat json files from Google Takeout, prompt engineered them with relevant context and conversational history. 
- Developed a Flask app to integrate the fine-tuned model API call with a user friendly front end.

## Professional Experience
### Google - [Everyday Robot Project ](https://everydayrobots.com/)@ X
**Jan 2019 - March 2023**
#### Tech Lead / DRI - Humans-in-the-loop 
- Created the HitL vision along with a decomposed technical paradigm of awareness, assistance and learning for robots to seek help, get assistance and learn from failure.
- Led a cross functional team to build a tool, framework and analytics for measuring requested and unrequested robot interventions.
- Explored open vocabulary detectors and fine-tuned visual-language models to query for environmental anomalies.
- Filed 7 [[my-patents]].
#### Tech Lead / DRI - Navigation Perception 
- Drove the execution, implementation & deployment of AutoLook, a feature that enables the robot to actively perceive the environment via moving its head to explore areas of interest. Augmented this active perception module to periodically collect data for annotation.
- Demonstrated initiative and provided technical leadership, from conception to production, for a framework for triaging field issues by robot operators. This enabled massively scaling operations and has grown into a self-sustained & growing team of > 8 people, analysing > 100 reported issues per day.
- Fully owned & implemented a library for synchronising messages of differing frequencies given various criteria. This removed boiler plate synchronisation logic and encapsulated it within a library thereby reducing bug likelihood, improving code readability and performance. Added extensive unit test coverage for not only the runtime checks but also compile test assertions of the library.

### Stealth Startup
#### Technology Advisor
**February 2023 - Ongoing**
- Provide guidance and prototyping using Generative AI techniques such as diffusion models for sample efficient synthetic data generation in the wearables domain.

### [Marble](https://www.nasdaq.com/articles/caterpillar-acquires-marble-robot-advances-automation-strategy-2020-06-25)
#### Founding Engineer & TLM -  Robot Perception
**June 2017 - November 2018**
- Led the overall design & architecture of the robot perception system. 
- Drafted feature lists & product roadmaps and managed work of several SWEs.
- Set software engineering principles like C++ standards, git version control workflow etc.

### Apple
#### Senior Software Engineer, SPG 
**Jan 2015 - June 2017**
- Given the nature of the project, most of my specific work at Apple is highly confidential. More broadly though:
	- Member of the systems architecture and core algorithms group
	- Developed software libraries (in C & C++) for algorithms in AI/ML, computer vision, computational geometry etc. Even though product has not yet been launched my code is still integral within the system.

### Robotics Institute, Carnegie Mellon University
#### Software Engineer 
**Jan 2013 - Dec 2014**
- Developed algorithms to enable off road mobility systems for several DARPA, DoD and NASA grants. Sample projects:
	- Built [high definition maps](https://www.ri.cmu.edu/publications/mapping-planetary-caves-with-an-autonomous-heterogeneous-robot-team/) of a super secret nuclear facility.
	- Perceptual Boosting: Developed algorithms to correlate vehicle slip with perceptual cues.
- Robot platforms included [LAGR](https://en.wikipedia.org/wiki/DARPA_LAGR_Program), [Pioneer](https://robots.ros.org/pioneer-3-dx/), Clearpath [Husky](https://clearpathrobotics.com/husky-unmanned-ground-vehicle-robot) and other [custom platforms](https://www.nrec.ri.cmu.edu/solutions/index.html).

## Software Engineering Internships
- **Merrill Lynch - Derivatives Trading Group** : Summer 2010
- **General Electric - Healthcare** : Summer 2009
- **Caterpillar Inc - CAT Simulation Center** : Spring 2008
- **America Reads Program - Urbana Elementary School** : (Part-time 2006-2007)

# Education
## Carnegie Mellon University
### MS in Robotic Systems Development - School of Computer Science 
**Graduated: May 2013**
**Research Topic:** Autonomous aerial search and rescue on a quadrotor.

## University of Illinois at Urbana Champaign
### BS in General Engineering (Dean's List) 
**Graduated: May 2011**

## Stanford University
### Continuing Education
#### Certificate - Artificial Intelligence Professional Program 
**Obtained: August 2021**
Natural Language Processing with Deep Learning : [XCS224N](https://publish.obsidian.md/ammar/3+-+Resources/courses/xcs224n+-+natural+language+processing/xcs224n+-+natural+language+processing) ; Natural Language Understanding : [XCS224U](https://publish.obsidian.md/ammar/3+-+Resources/courses/xcs224u+-+natural+language+understanding/xcs224u+-+natural+language+understanding) ; Machine Learning : [XCS229](https://publish.obsidian.md/ammar/3+-+Resources/courses/xcs229ii+-+machine+learning/xcs229ii+-+machine+learning) ; Reinforcement Learning : [XCS234](https://publish.obsidian.md/ammar/3+-+Resources/courses/xcs234+-+reinforcement+learning/xcs234+-+reinforcement+learning) 

#### Certificate - Product Management Professional Program 
**Obtained: August 2022**
Product Management: Transforming Opportunities into Great Products : [XPROD110](https://publish.obsidian.md/ammar/3+-+Resources/courses/xprod110+-+product+management/xprod110+-+product+management) ; Mastering Product Management: Building Your Strategy : [XPROD210](https://publish.obsidian.md/ammar/3+-+Resources/courses/xprod210+-+mastering+product+management/xprod210+-+mastering+product+management) ; Product Costing : [XPROD120](https://publish.obsidian.md/ammar/3+-+Resources/courses/xprod120+-+product+costing/xprod120+-+product+costing) ; User Research : [XPROD115](https://publish.obsidian.md/ammar/3+-+Resources/courses/xprod115+-+user+research/xprod115+-+user+research) ; Product Marketing : [XPROD154](https://publish.obsidian.md/ammar/3+-+Resources/courses/xprod154+-+product+marketing/xprod154+-+product+marketing)

## Princess Sumaya University of Technology - Amman, Jordan
### Undergraduate Exchange Program 
**Summer 2008**

# Skills
#### Adept
Python, Pytorch, Jupyter, C++, C, Linux, Git, Emacs, VS Code, Obsidian, OpenAI API, Huggingface API
#### Proficient
Heroku, Flask, Pinecone, MATLAB, Latex, Bash, Robot OS (ROS), Point Cloud Library (PCL), CGAL, Boost, Cmake, Qt, Mercurial, Gdb, Sql, Lisp, 
#### Familiar
Java, Html, Opengl, WxPython, Dreamweaver, Amazon Web Services EC2, GCP, Django, Netbeans
