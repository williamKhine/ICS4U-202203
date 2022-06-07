# ICS4U Final Exam

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
6th June 2022

#### Knowledge/Understanding
1. Given the following code segment:
```python
a = 0, b = 0
while (a < 10) :
	b += a
print (b)
```
Which output will be displayed?
a) 0
b) 10
c) 18
d) an infinite loop will occur

	d

2. Given the following code segment:
```python
for i in range (0,10):
	for j in range (0, 3):
	print (‘#’)
```
How many number signs will be displayed when the code segment is run?
a) 3
b) 4
c) 30
d) 300

	c

3. Suppose s1 = {1, 2, 4, 3} and s2 = {1, 5, 4, 13}, what is s1 | s2 ?
a) {1, 2, 4, 3, 1, 5, 4, 13}
b) {1, 2, 4, 3, 5, 13}
c) {1, 2, 4, 3}
d) {1, 5, 4, 13}

	b

4. Suppose x = 1, y = -1, and z = 1. What will be displayed by the following statement?
```python
if x > 0:
	if y> 0:
		print(“x > 0 and y > 0”)
elif z>0:
	print (“x < 0 and z > 0 ”)
```
a) x > 0 and y > 0
b) x < 0 and z > 0
c) x < 0 and z < 0
d) nothing displayed

	d

5. Analyze the following code:
```python
class A:
	def __init__ (self,s) :
		self.s = s
	def print(self):
		print (self.s)
a = A()
a.print( )
```
a) The program has an error because class A does not have a constructor.
b) The program has an error because s is not defines in print(s).
c) The program runs fine and prints nothing.
d) The program has an error because the constructor is invoked without an argument.

	d

6. Analyze the following code:
```python
class A:
	def __init__(self):
		self.x =1 self.__y = 1
	def getY(self):
		return self.__y
		
a = A()
a.x = 45
print(a.x)
```
a) The program has an error because x is private and cannot be accessed outside of the class.
b) The program has an error because y is private and cannot be access outside of the class.
c) The program runs fine and prints 1.
d) The program runs fine and prints 45.

	d

7. What is the value of times displayed?
```python
def main():
	myCount – Count()
	times = 0
	
for i in range(0, 100):
	increment(myCount, times)
	
print(“myCount.count =”’ myCount.count, “times =”, times)

def increment(c, times)
	c.count += 1
	times += 1
	
class Count:
	def __init__(self):
		self.count = 0

main()
```
a) count is 101 times is 0
b) count is 100 times is 0
c) count is 100 times is 100
d) count is 101 times is 101

	b

8. What will be displayed by the following code?
```python
class A:
	def __str__(self):
		return “A”
		
class B(A):
	def __init__(self):
		super().__init__()
		
class C(B):
	def __init__(self):
		super().__init__() def main():
		
b = B( )
a = A( )
c = C( )

print(a, b, c)

main()
```
a) C C C
b) A B C
c) A A A
d) B B B

	b

9. To check whether an object o is an instance of class A, use:
a) o.isinstance(A)
b) A.isinstance(o)
c) isinstance(o, A)
d) isinstance(A, o)

	c

10. What will be displayed by the following code?
```python
class Person:
	def getInfo(self):
		return “Person’s getInfo is called”
		
	def printPerson(self):
		print(self.getInfo(), end = ‘ ‘)
		
class Student(Person):
	def getInfo(self):
		return “Student’s getInfo is called”
		
def main():
	Person().printPerson()
	Student().printPerson()

main()
```
a) Person’s getInfo is called Person’s getInfo is called
b) Person’s getInfo is called Student’s getInfo is called
c) Student’s getInfo is called Person’s getInfo is called
d) Student’s getInfo is called Student’s getInfo is called

	b

11. What is displayed when the following program is run?
```python
try:
list = 10* [0]
x = list [9]
print (“Done”) except IndexError:
print (“Index out of bound”) else:
print(“Nothing is wrong”) finally:
print (“Finally we are here”)
```
a) “Done” followed by “Nothing is wrong”
b) “Done” followed by “Nothing is wrong” followed by “Finally we are here”
c) “Index out of bound” followed by “Nothing is wrong” followed by “Finally we are here”
d) “Nothing is wrong” followed by “Finally we are here”

	b

12. To read two characters from a file object infile, use:
a) infile.read(2)
b) infile.read()
c) infile.readline()
d) infile.readlines()

	a

13. The readlines() method returns a:
a) str
b) a list of lines
c) a list of single characters
d) a list of integers

	b

14. The time to merge two sorted lists of size n is:
a) O (1)
b) O (log n) c) O (n)
d) O (n log n) e) O(n * n)

	d

15. The worst-time complexity for quick sort is
a) O (1)
b) O (log n) c) O (n)
d) O (n log n) e) O (n * n)

	e

#### Thinking
16. Using class, write a program of Points and Circles
- A point in the plane is represented by the values for its coordinates, usually called x and y.
- The class Point has attributes x and y and a string representation which will return
the string representation of the point.
- A circle is determined by a center and radius.
- The class Circle will inherit from the class Point to represent its center. The radius of
the circle is an additional object data attribute. The function area is an additional
functional attribute.
- The class Circle will use the string representation of Point for its center and extend
the __str()__ function for its radius.
- (Polymorphism) Calling str() on x gives different strings, depending on whether x is
an instance of the class Point or Circle. Display the coordinates of point and center,
radius and area of circle.
- Derive a class Cylinder from the class Circle and print the area and volume of a
cylinder.
- Write comments for your codes.
- Give examples of outputs that you will get.
```python

```

Output
```txt

```

#### Communication

 17. Computer Technology has now allowed employees to work from home. (8 marks)
a) Give two advantages to employers of allowing employees to work from home.


a) Give two advantages to the employees of working from home.


b) Describe in details, two advances in computer technology which have allowed working from home to become possible.



18) a) State three ways of preventing hackers from committing computer crimes. (7 marks)


b) Describe how fingerprints systems can be used to help catch criminals.


#### Application
19. Write a Python program that declares a string and returns key-value pairs of the letters in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored.
Example: string1= ‘pineapple’
Output- {(a:1), (e:2), (i:1), (l:1), (n:1), (p:3)}
```python

```

20. Write a python program to store 10 students’ names and their age. If their age is less than 16 then they are not eligible to apply for driver’s licence or else they are. Your program will print the names and age of the two different groups.
```python

```