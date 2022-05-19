# Q1) 2) Inheritance

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

# Q1) 3)

# in the file greeting.py
def greet(name):
	print(f"Hi, {name}")

# in the file main.py
import greeting
greeting.great("William") # calling a function inside another file.

# Q2)

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printProfile(self):
        print(self.name, self.age, self.gender)

william = Student("William", 19, "Male")
william.printProfile()

# Q3)

def subProgram():
    print(0.1)
    print(0.2)
    print(0.3)

def mainProgram():
    print(1)
    print(2)
    subProgram()
    print(4)

mainProgram()

