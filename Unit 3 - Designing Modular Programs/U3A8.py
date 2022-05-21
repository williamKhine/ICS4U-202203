# Q1) 2) Recursive Functions

def function1():
    print('calling function2')
    function2()

def function2():
    print("calling function1")
    function1()

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

# Iterating through the list and checking if the search value is equal to the value in the list.
# If it is, it prints the index of the value in the list.
    for i in range(len(uniqueList) - 1):
        if searchValue == uniqueList[i]:
            print(f"The value that you are searching for is at index {i}.")
            break
# Checking if the search value is not in the list.
    else:
        print(
            f"The value that you are searching for is not in the list: \n{uniqueList}")

def binarySearch(uniqueList, searchValue):
    pass



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