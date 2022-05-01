# ICS4U Unit 1 Activity 5 - Non-numeric Comparisions Worksheet

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
4th Feb 2022

##### Q1) Differentiate 1D array and 2D array by example.
An one-dimensional array is a single list of similar type elements stored in a computer's memory. But in Python, there can be arrays containing different types of elements.
Example of 1D array:

A two-dimensional array can represent two dimensions. 

##### Q2) Write a program to enter integer type data into array and print the values in reverse order.
```python
def enterIntegerAndReverse():
	arr = [] # Declaring a blank array
	
	# Getting user input with error handling
	while True:
		x = input("Enter an integer (q to quit): ")
		if x == 'q':
			break
		try:
			arr.append(int(x))
		except ValueError:
			print("ValueError. Enter an integer (q to quit): ")
		else:
			pass
			
	print(f"{arr} <== Original array.")
	arr.reverse()
	print(f"{arr} <== Reversed array.")
```
Output
```
Enter an integer (q to quit): 1
Enter an integer (q to quit): 2
Enter an integer (q to quit): 3
Enter an integer (q to quit): 4
Enter an integer (q to quit): 5
Enter an integer (q to quit): q
[1, 2, 3, 4, 5] <== Original array.
[5, 4, 3, 2, 1] <== Reversed array.
```
##### Q3) Write a program to sum array A elements and array B elements.
```python
def sumTwoArrays():
	# Declaring two arrays with data hard coded
	arrayA = [1, 2, 3, 4, 5]
	arrayB = [5, 4, 3, 2, 1]

	# Variable with value '0' inside to accomodate the sum of two arrays
	sumAB = 0

	for x in arrayA:
		sumAB += x
	for x in arrayB:
		sumAB += x
	print(f"{arrayA} <== Array 1.")
	print(f"{arrayB} <== Array 2.")
	print(f"{sumAB} <== Sum of Array 1 and Array 2.")
```
Output
```
[1, 2, 3, 4, 5] <== Array 1.
[5, 4, 3, 2, 1] <== Array 2.
30 <== Sum of Array 1 and Array 2.
```
##### Q4) Write a program that fills arrays P with 20 integers and then print the product of the elements of the array.
```python
def productOfTwoArrays():
	# Random module to fill the array with random integers 1 to 9 inclusive
	import random

	arrayP = []
	# Variable to hold product of the array. Value is '0' because of product.
	productP = 1

	for i in range(20):
		arrayP.append(random.randint(1, 9))

	print(f"{arrayP} <== Array P with 20 integers.")

	for i in arrayP:
		productP *= i

	print(f"{productP} <== Product of all the elements of Array P.")
```
Output
```
[2, 3, 8, 4, 2, 2, 9, 3, 1, 6, 6, 4, 3, 3, 6, 2, 8, 9, 6, 2] <== Array P with 20 integers.
278628139008 <== Product of all the elements of Array P.
```