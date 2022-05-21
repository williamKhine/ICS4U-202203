# Q1) 2) Recursive Functions

def recursiveFunction(num):
    if num != 0:
        print(num)
        recursiveFunction(num - 1)

recursiveFunction(5)

# function2()

# Q1) 3) Loops

x = 10

while x != 0:
    print(x)
    x -= 1

# Q2)

def getSearchValue():

    while True:
        try:
            searchValue = int(
                input(f"Which integer do you want to search? (0 to 99): "))
        except ValueError:
            print("ValueError. Please enter an integer.")
        else:
            break

    return(searchValue)

def makeUniqueList():
    """
    It creates a list of 30 random integers between 0 and 99, then it removes all duplicates from the
    list
    :return: A list of unique integers.
    """
    import random

    highestInteger = 99
    lowestInteger = 0

    nonUniqueList = []

    for i in range(30):
        nonUniqueList.append(random.randint(lowestInteger, highestInteger))

    uniqueList = list((set(nonUniqueList)))

    print(f"\n{nonUniqueList} <== list, probably not unique.\n")
    print(f"{uniqueList} <== truely unique list.\n")

    return(uniqueList)


def linearSearch(uniqueList, searchValue):
    count = 0
    for i in range(len(uniqueList) - 1):   
        count += 1 
        if searchValue == uniqueList[i]:
            print(f"The value that you are searching for is at index {i} (Linear Search).")
            break

    else:
        print(
            f"The value that you are searching for is not in the list: \n{uniqueList}")
    return(count)

def binarySearch(uniqueList, searchValue):
    
    start_index = 0
    end_index = len(uniqueList) - 1

    count = 0

    found = False

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        middle_value = uniqueList[middle_index]

        if middle_value == searchValue:
            print(f"The value that you are searching for is at index {middle_index} (Binary Search).")
            found = True
            count += 1
            break
        elif middle_value < searchValue:
            start_index = middle_index + 1
            count += 1
        else:
            end_index = middle_index - 1
            count += 1
            
    if found is False:
        print(f"The value that you are searching for is not in the list: \n{uniqueList}")

    return(count)


import time

uniqueList = makeUniqueList()
searchValue = int(input("What number are you searching for? (1 - 100): "))

start = time.time()
linearCount = linearSearch(uniqueList, searchValue)
end = time.time()
linearTime = end - start

start = time.time()
binaryCount = binarySearch(uniqueList, searchValue)
end = time.time()
binaryTime = (end - start)

print(f"Linear Search makes {linearCount} operation(s) and took {linearTime}")
print(f"Binary Search makes {binaryCount} operation(s) and took {binaryTime}")

# Q3)


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

# Q4)

import turtle as t

t.speed(1)
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()