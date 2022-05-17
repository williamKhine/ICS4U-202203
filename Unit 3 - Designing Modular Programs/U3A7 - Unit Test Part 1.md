# ICS4U Unit 3 Activity 7 - Unit Test Part 1

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
14th May 2022

#### Knowledge/Understanding/Communication 
##### Q1) Define, using examples where appropriate, the following computer terms:
1) Unified Modeling Language
Unified Modeling Language (UML) is a standardization of maodelling languages created to help visualize a system or a program with the use of disgrams. This language is not a language per se, but a set of rules guiding to draw the diagrams in the standardized way.

2) Inheritance
Inheritance, like in the real world, allows a class to inherit all the attributes of the parent class such as the class-methods, private variables and the blueprint. After the class has inherited the attributes from the parent class, it (the child class) can then override and overload the methods to suit their specific needs.

```python
class LivingThing: # Parent Class

	def eat(self):
		print("Eating")
		
	def sleep(self):
		print("Sleeping")
		
	def die(self):
		print("Dead")

class Human(LivingThing): # Child Class

	def eat(self, food): # Method Overloading
		print(f"Human eating {food}")

	def sleep(self): # Method Overriding
		print("Human sleeping")
```
Even when the function `die()` is not defined in the `Human` class, it can still be called since `Human` class inherits all the attributes from the parent class (`LivingThing`). Every `LivingThing` will die someday. Unless `Human` class overrides the `die()` method and calls the `immortal()` method.

3) Modules


4) Object Oriented Programming



##### Thinking/Inquiry
##### Q2)  Compute a program to show use of classes or methods in program.


#### Application
##### Q3) Demonstrate the evidence to design sub program in any programming language.


#### Communication
##### Q4)  Clarify and explain the following terms with examples.
Abstract Data Types

Stack

Queue

Dictionary