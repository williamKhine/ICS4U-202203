# Q1) 2) One Dimensional Array

arr = [1, 2, 3, 4]

print(arr[0])

# Q1) 3) Encapsulation

class Student:
    def __init__(self, name, grade, age) -> None:
        self.name = name # Public
        self._grade = grade # Protected
        self.__age = age # Private

aaron = Student("Aaron", 12, 19)
print(aaron.name)
print(aaron._grade)
# print(aaron.__age)

# Q1) 4) Polymorphism

class Computer:
    def __init__(self) -> None:
        print("This is a Computer.")

class AdvancedComputer(Computer):
    def __init__(self, processor, memory) -> None:
        print(f"This is a computer with {processor} processor and {memory} memory.")

asus = Computer()
dell = AdvancedComputer("Intel", "32GB")

# Q2a) 

def stringToInt(string):
    x = int(string)
    return(x)
    
string = input("Enter a number: ")
integer = stringToInt(string)
print(integer, type(integer))

# Q2b)
# Method 1
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)

# Method 2
arr = [1, 2, 3, 4, 5]
print(arr[::-1])

# Method 3
arr = [1, 2, 3, 4, 5]
revArr = []
for i in range(len(arr) - 1, -1, -1):
    revArr.append(arr[i])

print(revArr)

# Q3)
# In the file person.py
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def move(self):
        print("Person moving.")

# In the file main.py
# import person
class RunningPerson(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def move(self):
        print(f"{self.name} running.")

john = Person("John")
jess = RunningPerson("Jess")

john.move()
jess.move()

# Q4a)

class Human:
    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender

    def showSpecs(self):
        print(f"My name is {self.name}. I am {self.gender}.")

albert = Human("Albert", "Male")
albert.showSpecs()

# Q4b)

def nameCount(name):
    ln = len(name)
    print(ln)

name = input("What's your first name?: ")
nameCount(name)