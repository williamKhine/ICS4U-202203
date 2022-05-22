# ICS4U Unit 1 Activity 12 - Unit Test Part 2

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
14th March 2022

#### Knowledge/Understanding
##### Q1) Define the following terms with examples:
1) Algorithm
An algorithm is a set of rules usually written in code to perform a specific task. An algorithm can be optimized to perfrom the task more efficiently with the use of mathematics and extra resources such as more processing power and memory. Examples of algorithms are searching algorithms and sorting algorithms. Algorithms can be run in a computer to perform software tasks or can be a physical task as a cooking recipe.

2) Linear Search and Binary search
Linear Search and Binary Search are searching algorithms which checks a given value to a match in an array and returns where the value is in the form of an index number in the array. Linear Search is a method of finding an element in a list by comparing every element in that list to the given value. This algorithm goes through all the elements until the value is found. This algorithm is slow and would take more time since it is going through all the indexes and has a Big O' Notation of $O(n)$. Binary Search is different from the linear search. Binary search is a much fastaer searching algorithm but the array has to be sorted for the binary search to work. Binary search first compares the value of the middle element with the search value and then if that value of the middle element and then if the value is equal, it returns the index, but if not, checks if the middle value is less than or greater than the search value, and then discards the left side or the right side of the array respectfully. This continues till the search value is found.

3) Bubble sorting
Bubble sorting is a sorting algorithm which takes an unsorted list and sorts it according to the bubble algorithm. The algorithm compare two side by side elements and sorts them by swapping places, smaller to the left and the greater to the right. This makes it so that the largest number will rise to the right side of the array like a bubble and this repeats till all the elements in the array is sorted. This has a Big O' Notation of $O(n^2)$.

4)  User Manual
A User Manual is like the documentation of the program where it will be stated how a program is written and how it works. Also the instructions on how to use the program, maintain it or fix bugs.

#### Thinking/Inquiry
##### Q2) Compute the program with an algorithm to print sum and product of an array.
Algorithm
```
1. Create Array
2. Create variable for product of value 1
3. Create variable for sum of value 0
4. Loop to sum all elements
5. Add to sum variable
6. Print sum
7. Loop to multiply all elements
8. Multiply values to product variable
9. Print product
```
```python
arr = [1, 2, 3, 4, 5]
product = 1
sum = 0

for i in arr:
    sum += i

print("Sum of array =", sum)

for i in arr:
    product *= i

print("Product of array =", product)
```
Output
```txt
Sum of array = 15
Product of array = 120
```

#### Communication 
##### Q3) Explain what is software testing and basis of software testing? List different types of testing for software project to ensure program correctness.
Software Testing is the process of checking the program to see if the software meets the requirements that is aiming to meet. This will ensure that the end-product is good enough for production. A software tester will stress test the code to see of the code handles all the errors and that there will be no bugs. The types of software testing are functional testing, non-functional testing, performance testing and maintenance.

#### Application
##### Q4a) Create an Algorithm to translate numbers into word.
Making algorithm for all the numbers would take very long. Here's algorithm for numbers from 0 to 100.
```
1. Take user input.
2. If less than equal to 10, orint number word which coresponds to it.
3. If more than 10, and less than equal to 19, print word along with "teen". But if the number is 11, 12, or 13 then it will be eleven, twelve and thirteen.
4. If more than 20 and less than 100, check the first number and print corresponding to number like 30 = thirty, 40 = forty, along with the number in the ones place. If the number is in the ones place is 0, stop at the tens place.
5. If the number is 100, then print 100.
```

##### Q4b) Device the program to print 2D array in Matrix form.
```python
arr = [1, 2, 3, 4], [4, 3, 2, 1]

def matrix(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

matrix(arr)
```
Output
```txt
1 2 3 4 
4 3 2 1 
```