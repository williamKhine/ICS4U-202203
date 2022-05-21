# ICS4U Unit 3 Activity 8 - Unit Test Part 2

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
14th May 2022

#### Knowledge/Understanding/Communication 
##### Q1) Define, using examples where appropriate, the following computer terms:
1) Algorithm
Algorithm is a set of rules and or instructions which is needed to be followed to accomplish something especially in a computer program. Even a recipe can be said to be an algorithm but the term "Algorithm" is mostly used in Computer Science. Algorithms do not necessarily have to be codes, they can also be written in simple plain English or even Pseudo code.

Algorithm for Binary Search (Array needs to be a sorted array)
```
1. Ask for the value that the user wants to search.
2. Access the value in the middle index of the array.
3. If the middle value matches the search value, return the middle index. If the values do not match, continue.
4. If the search value is less than the middle value, discard the right side of the array. If the value is greater than the middle value, discard the left side of the array.
5. Repeat step number 2 till the search value is found.
	1. If the value is not found till the last element to be searched, return "not found".
```

2) Computational complexity analysis
Computational Complexity Analysis measures how wfficient an algorithm is and what resources are required to run the algorithm. It measures the time needed to run all the nested loops along with the whole program.
3) Recursive function
Recursive Functions are functions that has a recursive loop inside it and in that loop calls the function that initiates the loop itself.
```python

```
4) Loop
Loops are like recursive functions but without the function. This loops a section or a block of code until a condition is met.
```python
x = 10

while x != 0:
	print(x)
	x -= 1
```
Output
```txt
10
9
8
7
6
5
4
3
2
1
```

#### Thinking/Inquiry
##### Q2)  Compute a program to compare linear search and binary search.
```python

```

#### Application
##### Q3) Create an algorithm and the program for Fibonacci numbers.
```txt
1. Get Numbber of sequences the user wants and subtract two.
2. Make a list containing these two elements [1, 2]
3. Sum the last two indexes and append them at the end of the list above.
4. Repeat recursively for the number calculated in Step 1.
```
```python
def fibonacci():
    n = int(input("How many sequences of the fibonacci do you want?: "))

    if n == 1:
        print([1])
    elif n == 2:
        print([1, 2])
    else:
        n -= 2

        fibonacci = [1, 2]
        for i in range(n):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print(fibonacci)

fibonacci()
```
Output
```txt
How many sequences of the fibonacci do you want?: 10
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

#### Communication
##### Q4)  Write a program to make circle and then color it.
```python
import turtle as t

t.speed(1)
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()
```
![[Pasted image 20220522023916.png]]