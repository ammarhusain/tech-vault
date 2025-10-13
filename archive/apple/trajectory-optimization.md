### [Trajectory Optimization](http://www.matthewpeterkelly.com/tutorials/trajectoryOptimization/index.html) - Matthew Kelly
Good set of slides - [cartPoleCollocation.svg](http://www.matthewpeterkelly.com/tutorials/trajectoryOptimization/cartPoleCollocation.svg)
Method to define desired behavior of a dynamical system

![[archive/apple/attachments/trajectory-optimization-2023-07-07.png]]
In general trajectory optimization methods are trying to find `u(t)`
![[archive/apple/attachments/trajectory-optimization-2023-07-07-1.png]]
When you have global knowledge for closed loop solutions control `u` is computed as a function of state `x` whereas in the open loop trajectory optimization world control `u`  is computed as a function of time `t`

![[archive/apple/attachments/trajectory-optimization-2023-07-07-2.png]]

![[archive/apple/attachments/trajectory-optimization-2023-07-07-3.png]]
boundary objective basically says how good or bad is it for a trajectory to be on a certain starting or ending location
integral objective term describes some quantity along the trajectory - eg: minimize motor torque, minimize jerk etc

![[archive/apple/attachments/trajectory-optimization-2023-07-07-4.png]]

Transcription helps frame the problem in a way that makes it easier to solve with a lot of known methods

![[archive/apple/attachments/trajectory-optimization-2023-07-07-6.png]]
Collocation methods are common to use in robotics & manipulation

![[archive/apple/attachments/trajectory-optimization-2023-07-07-5.png]]
$\ddot{q1}$ & $\ddot{q2}$ are derived by working through the mechanics of the system and define its dynamics, ie how it moves over time given some control input $u$ and its state. This can also be assumed to be provided to you and is plug and play for trajectory optimization.

![[archive/apple/attachments/trajectory-optimization-2023-07-07-7.png]]


collocation constraints are simply constraints computed at discrete grid points instead of the continuous function representation that the true optimization system is defined using.



### [RI Seminar: Stefan Schaal : From Movement Primitives to Associative Skill Memories - YouTube](https://www.youtube.com/watch?v=ViN87GTew1Y)
![[archive/apple/attachments/trajectory-optimization-2023-07-07-8.png]]
DMPs in very simple terms seem like these attractor functions that given a goal state can reach it by following many different trajectories. The first term in the first equation is a simple spring dampener that pushes the state towards the goal. The second term $f(x)$ is an arbitrary function that deviates the trajectory in different ways around the landscape. This $f(x)$ can be learned via simple function approximation. For j595 maybe we can create this function by bundling together many different animations that it still reaches the same goals but projecting different types of motions/emotions.
The second equation is a simple placeholder for time. $C$ terms are coupling terms which mean they can couple perceptual information for example.
![[archive/apple/attachments/trajectory-optimization-2023-07-07-9.png]]
![[archive/apple/attachments/trajectory-optimization-2023-07-07-10.png]]
Trajectory based RL is a way to get away from doing RL in a very high dimensional state space (which can be intractable) and just start with a spaghetti like trajectory and then figure out how you can make it better. It is a locally optimal solution but cant explore the space of all possible trajectories.
  ![[archive/apple/attachments/trajectory-optimization-2023-07-07-11.png]]
  ![[archive/apple/attachments/trajectory-optimization-2023-07-07-12.png]]
  The red term $\theta_i$ in the equation is one set of canned/learned motion and then you can apply or combine multiple of these together to create a motion trajectory.
  Dynamic time warping - how do you morph one trajectory in to another trajectory
  