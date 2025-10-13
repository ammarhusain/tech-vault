---
aliases: [structure and interpretation of computer programs, sicp]
created: 2022-09-06-Tuesday 20:19
modified: 2023-03-10-Friday 23:15
tags: 
---


---

**Instructors**: Gerald Jay Sussman, Hal Abelson
**Lectures**: [YouTube lecture videos](https://www.youtube.com/playlist?list=PLE18841CABEA24090)
[[courses/MIT 6.001 Structure and Interpretation of Computer Programs, 1986/attachments/sicp.pdf|SICP book]]

[Scheme Online Compiler & Interpreter - Replit](https://repl.it/languages/scheme)

# Lectures
- Imperative knowledge: “How to” do something vs Declarative knowledge: something that is true such as sqrt(y) = x if x*x = y & x>0
- Key aspects of a programming language: 1) Primitive elements, 2) Means of combination, 3) Means of abstraction
- Lambda is Lisp way of saying “make a procedure”
- If <predicate> do <consequent> otherwise do <alternative> : <> are names of expressions.
- Linear iteration: time O(n), space O(1) .... linear recursion: time O(n), space O(n)
- In iteration all the state is in explicit variables
- Herrons method for finding square roots: To find square root of x, start with some guess y and then keep computing: (y + (x/y))/2 until it converges.
	 - This is essentially taking the average of y + (x/y)
	 - It boils down to computing the fixed point of some function, ie f(sqrt_x) = (y + (x/y))/2 and if you sub y = sqrt_x you get f(sqrt_x)=sqrt_x which means its a fixed point
- Newtons method to find the roots/zeros of functions f(y) = 0
	 - y_n+1 = y_n - (f(y_n) / (df/dy | evaluated at y_n)
	 - To find square root of x use function f( x - squared(y))
- In order to make a system robust, for small changes in the problem there needs to be only a small change in the solution. With having a descriptive, continuous & rich language you attain that flexibility compared with splitting the problem into tasks & subtasks. It almost feels like in ML or Deep learning (specifically) that is not the case. Minor changes can cause dramatic solution differences. I wonder if it is missing this language of synthesis that Harold described for pictures to combline & close them in beautiful ways.
- Derivatives are easier because they are reductionist, whereas integrals are more complicated searches ie can have multiple possible solutions when trying to compute from a derivative
- Algebraic simplifications code are a huge complicated mess
- Quotations in code: Having the ability to talk about expressions that the expressions of the language can talk about. Thies gives you the ability to embed a language within the language that your core language can then evaluate (or interpet). This invented language can possibly look very different from the core language. Kind of reminds of template metaprogramming.
- There are either bound variables or free variables. Bound variables are passed into the procedure while free variables come from the environment
- Sussman inspires having assignment operators/ state in your program by the need to use random numbers. PRNG needs to maintain a state of the random engine and it is cleaner if it can maintain state on its own using assignment rather than leaking its state into my program of computing probabilities for some event. If it is leaked that means I will have to keep on passing the state of the PRNG within my internal loop rather than making a procedure call to the PRNG object
- State/Assignment operators must be used very very judiciously and not out of laziness. Lambdas are the glue. You piece them together to build more & more complex systems
- Language needs: Primitives, Means of combination & Means of abstraction.
- Look up message passing online. I think it means passing procedures around as messages

---

- Typed Data, Dispatch on Type: Is simply a pair with the car being some symbol of type, ie “Rectangular”, “Polar” and cdr being the contents in this case 2 numbers. There is a manager that looks at the “type” (car) of the object and dispatches to the appropriate function. This enables you to provide generic operators.
	 - This system is basically implemented by the compiler (template) /C++ runtime in C++ by name mangling etc.
	 - Interesting to look at the origin of “type safe” or “statically typed” languages.
- Functional version has no state or assignment vs Imperative version
- Substiution model: when there is no state and everything is computed functionally. As compared with Environment model where there are state variables in the environment that the computation is done on.
- Defining CONS, CAR & CDR purely functionally by Alonzo Church (lambda calculus):
	 - (DEFINE (CONS X Y)

LAMBDA (M) (M X Y)))

- (DEFINE (CAR X Y)

(X (LAMBDA (A D) A)))

- (DEFINE (CDR X Y)

(X (LAMBDA (A D) D)))

- Map, Filter & Accumulate are the 3 most common subroutines you’d need.
- Streams: A signal processing way of computing something ... Enumerate->Filter->Map etc. However all the computation does not take place one after the other but by tugging at every step with “Pending computation” objects.
- Dynamic Binding: Variables in a procedure are bound not within the procedure itself but somewhere within its chain of callers. "Famous bug" ... Very similar to having global variables
- Ability to treat Procedures as objects or values makes them first class citizens in a language.
- Prolog most popular logic programming language. Logic programmers say: "You use logic to express what is true, to check whether something is true and to find out whats true."
- Logic Programming: (Primitives - Query); (Means of combination - NOT, AND, OR etc.); (Means of abstraction - Rules) ... Feels very much like SQL or regex
- Devious subtlety in logic programming compared to real logic is the order of the expression matter ie (A & B) is not the always same as (B & A) and thats because these operations are implemented as streams + filtering. So if the A stream didnt produce results theres nothing for B stream to consume & filter. While inversely B stream could have produced a lot more results then passed into A.
- Closed world assumption: There is a big difference between “Not True” and “Not deducible from Database”. the presumption that a statement that is true is also known to be true. Therefore, conversely, what is not currently known to be true, is false. (Kind of like the question of free, unoccupied & unknown in an occupancy grid)

Lecture 10A

- Interpreter is a general purpose simulator, while the compiler just transforms the given source code into some register machine language. So it does not have to worry about simulating every possible LISP expression.
