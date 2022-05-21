# ICS4U Unit 3 Activity 8 - Unit Test Part 2

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
14th May 2022

#### Knowledge/Understanding/Communication 
##### Q1) Define, using examples where appropriate, the following computer terms:
1) Algorithm

2) Computational complexity analysis

3) Recursive function

4) Loop

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
    n = int(input("How many sequences of the fibonacci do you want?: ")) - 2

    fibonacci = [1, 2]
    for i in range(n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

fibonacci()
```
```txt
How many sequences of the fibonacci do you want?: 10
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

#### Communication
##### Q4)  Write a program to make circle and then color it.
```python

```