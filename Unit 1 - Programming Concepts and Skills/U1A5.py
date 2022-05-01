# ===================================== #
# Unit 1 - Activity 5 - Array Worksheet #
# ===================================== #


# Q2) Write a program to enter integer type data into array and print the values in reverse order.
def enterIntegerAndReverse():
	arr = []
	x = 0

	while True:
		x = input("Enter an integer (q to quit): ")
		if x == 'q':
			break
		x = int(x)
		arr.append(x)
		print(arr)

	arr.reverse()
	print(arr)

# Q3) Write a program to sum array A elements and array B elements.
def sumTwoArrays():
	arrayA = [1, 2, 3, 4, 5]
	arrayB = [5, 4, 3, 2, 1]

	sumAB = 0

	for x in arrayA:
		sumAB += x
	for x in arrayB:
		sumAB += x

	print(sumAB)

# Q4) Write a program that fills arrays P with 20 integers and then print the product of the elements of the array.
def productOfTwoArrays():
	import random

	arrayP = []
	productP = 1

	for i in range(10):
		arrayP.append(random.randint(1, 9))

	print(arrayP)

	for i in arrayP:
		productP *= i

	print(productP)

# ================= #
# Calling Functions #
# ================= #
enterIntegerAndReverse()
sumTwoArrays()
productOfTwoArrays()