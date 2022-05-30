# Q1) 2) Inheritance

class LivingThing:  # Parent Class
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    @staticmethod
    def die():
        print("Dead")


class Human(LivingThing):  # Child Class
    def eat(self, food):  # Method Overloading
        print(f"Human eating {food}")

    def sleep(self):  # Method Overriding
        print("Human sleeping")


deer = LivingThing()
david = Human()

deer.eat()
deer.sleep()
deer.die()

david.eat("deer meat")
david.sleep()
david.die()

# Q1) 3)


# in the file greeting.py
def greet(name):
    print(f"Hi, {name}")

# in the file main.py
import greeting
greeting.great("William") # calling a function inside another file.


greet("William")

# Q2)


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_profile(self):
        print(self.name, self.age, self.gender)


william = Student("William", 19, "Male")
william.print_profile()

# Q3)


def sub_program():
    print(0.1)
    print(0.2)
    print(0.3)


def main_program():
    print(1)
    print(2)
    sub_program()
    print(4)


main_program()

# Q4) Stack

stack = []


def stacking(item):
    stack.insert(0, item)
    print(stack)


stacking(1)
stacking(2)
stacking(3)

# Q4) Queue

queue = []


def queuing(item):
    queue.append(item)
    print(queue)


queuing(1)
queuing(2)
queuing(3)

# Q4) Dictionaries

wk = {"name": "William Khine", "age": 19}
print(wk["age"])
