# Q2)
arr = [1, 2, 3, 4, 5]
product = 1
sum = 0

for i in arr:
    sum += i

print("Sum of array =", sum)

for i in arr:
    product *= i

print("Product of array =", product)

# Q4)
arr = [1, 2, 3, 4], [4, 3, 2, 1]

def matrix(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

matrix(arr)