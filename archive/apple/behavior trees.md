## GDC
[AI Arborist: Proper Cultivation and Care for Your Behavior Trees - YouTube](https://www.youtube.com/watch?v=Qq_xX1JCreI)

## Petter Ogren
### [5 minute Behavior Tree tutorial - YouTube](https://www.youtube.com/watch?v=KeShMInMjro&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg)
Key problem to solve - what to do next?
One way is to use FSM to code up transitions for all actions. Each action needs to know what to do next:
![[archive/apple/attachments/behavior trees-2023-07-19.png]]
In a behavior tree each action just needs to know whether it succeeded or failed. Parent of an action sends a tick and the action just returns success or failure.
Who decides what to do next? - Its the ancestors
![[archive/apple/attachments/behavior trees-2023-07-19-2.png]]

In the classical formulation, there exist four categories of control flow nodes (Sequence, Fallback, Parallel, and Decorator) and two categories of execution nodes (Action and Condition).
The Decorator node is a control flow node with a single child that manipulates the return status of its child according to a user-defined rule and also selectively ticks the child according to some predefined rule. For example, an invert decorator inverts the Success/Failure status of the child; a max-N-tries decorator only lets its child fail N times, then always returns Failure without ticking the child; a max-T- sec decorator lets the child run for T seconds then, if the child is still Running, the Decorator returns Failure without ticking the child. The symbol of the Decorator is a rhombus

### [What is a Behavior Tree and How do they work? (BT intro part 1) - YouTube](https://www.youtube.com/watch?v=DCZJUvTQV5Q&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=2)
Better alternatives to FSMs
![[archive/apple/attachments/behavior trees-2023-07-19-3.png]]

Advantages of Behavior Trees BTs:
- Modularity - few dependencies between components
- Built in hierarchical structure - actions exist on many levels of detail
- Graphical representation 
- Explicit handling of - sequences, fallbacks & interruptions

How do we decide when to switch task?
- Success - continue a sequence
- Failure - invoke a fallback
- Interrupted by more important task - do more important stuff
![[archive/apple/attachments/behavior trees-2023-07-19-5.png]]

For more complex behaviors or modifying them - subtrees can be added or removed at any of the nodes without worrying about dependencies
![[archive/apple/attachments/behavior trees-2023-07-19-6.png]]

Also behaviors can be collapsed into action by encapsulated all actions within one subtree - this lends to a natural hierarchical representation.

Conditions are Actions that- a) never return Running and b) do not change the world


### [How to create Behavior Trees using Backward Chaining (BT intro part 2) - YouTube](https://www.youtube.com/watch?v=dB7ZSz890cw&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=3)
What is Backward Chaining?
- Solving an AI Planning Problem by working backwards from the goal

BTs can do actions reactively - built in fallbacks when something does not work

Key idea is to chain these subgoals recursively
![[archive/apple/attachments/behavior trees-2023-07-19-9.png]]

![[archive/apple/attachments/behavior trees-2023-07-19-10.png]]

![[archive/apple/attachments/behavior trees-2023-07-19-11.png]]

Backward Chaining is simply the concept that - Each condition can get recursively connected to achieve a subgoal

Key idea: Replace conditions with BT that achieve them.

#### [Creating Behavior Trees using Decision Tree design (BT intro part 3) - YouTube](https://www.youtube.com/watch?v=L9KTzZO3C8s&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=4)
Behavior Trees generalize Decision Trees
	- every DT can be written in the form of a BT
If a DT design is appropriate - we can easily transfer it into a BT
But since DTs do not allow return status from Actions/Subtrees we assume that all "leaves" of the the DT always return "Running"

Mapping DT to BT:
![[archive/apple/attachments/behavior trees-2023-07-19-13.png]]

 Take home message:
 - If action choices can be broken down into Yes/No cases - Use DT design
 - If you want a deliberative system that pursues sub-goals - Use Backward chaining designs
 - Combine as needed

#### [Behavior Trees vs Finite State Machines (BT intro part 4) - YouTube](https://www.youtube.com/watch?v=gXrKGTPwfO8&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=5)
Both FSMs and BTs answer the basic question - what action to take next?
![[archive/apple/attachments/behavior trees-2023-07-19-14.png]]
 ![[archive/apple/attachments/behavior trees-2023-07-19-15.png]]

State transitions structure are same for all FSMs and depend only on the state of the world and not what action is currently being taken.
![[archive/apple/attachments/behavior trees-2023-07-19-16.png]]

#### [Behavior Trees that avoid checking All conditions All the time (BT intro part 5A) - YouTube](https://www.youtube.com/watch?v=UHUBYFal0DM&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=6)
Use a bit vector to separate computing your beliefs from checking your beliefs - this would be super fast 
![[archive/apple/attachments/behavior trees-2023-07-19-17.png]]

![[archive/apple/attachments/behavior trees-2023-07-19-18.png]]


#### [Behavior Trees and Reinforcement Learning (intro to BTs part 14) - YouTube](https://www.youtube.com/watch?v=y-0fXTmg9fk&list=PLFQdM4LOGDr_vYJuo8YTRcmv3FrwczdKg&index=15)

![[archive/apple/attachments/behavior trees-2023-07-19-20.png]]

![[archive/apple/attachments/behavior trees-2023-07-19-21.png]]

![[archive/apple/attachments/behavior trees-2023-07-19-23.png]]
![[archive/apple/attachments/behavior trees-2023-07-19-24.png]]
 ![[archive/apple/attachments/behavior trees-2023-07-19-25.png]]

# Book
[[archive/apple/attachments/Behavior Trees in Robotics and AI - An Introduction.pdf]]