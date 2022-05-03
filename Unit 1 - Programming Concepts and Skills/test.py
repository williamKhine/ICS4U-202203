# Python program for implementation of Bubble Sort
import time
 
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                print(i, j, n)
                time.sleep(0.05)
 
 
# Driver code to test above
arr = []

import random

for i in range(30):
    arr.append(random.randint(1, 99))
print(arr)
time.sleep(3)

 
bubbleSort(arr)
 
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")