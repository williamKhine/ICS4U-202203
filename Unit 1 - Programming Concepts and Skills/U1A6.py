# ================================================= #
# Unit 1 - Activity 6 - Array Reading and Worksheet #
# ================================================= #

# Q1) Write an Algorithm to insert and delete array elements


def insertIntegers(arr):
    """
    The function `insertIntegers` takes an array as an argument and appends integers to the array until
    the user enters 'q' to quit

    :param arr: The array to insert integers into
    """
    while True:
        x = input("Enter an integer (r to remove): ")
        if x == 'r':
            break
        try:
            arr.append(int(x))
        except ValueError:
            print("ValueError. Enter an integer (r to remove): ")

    print(f"{arr} <== Inserted array elements")


def deleteIntegers(arr):
    """
    The function takes in an array and allows the user to remove elements from the array until the array
    is empty

    :param arr: an array of integers
    """

    while len(arr) != 0:
        y = input("Enter the index you want to remove (q to quit): ")
        if y == 'q':
            break
        try:
            arr.pop(int(y))
        except IndexError:
            print("IndexError. Enter a valid index number.")
        except ValueError:
            print("ValueError. Enter the index you want to remove (q to quit): ")
        else:
            print(arr)
    print("Array is empty. No more elements to remove.")


def insertDeleteIntegers():
    """
    This function will insert integers into an array and then delete integers from the array.
    """
    arr = []  # Declaring a blank array

    insertIntegers(arr)
    deleteIntegers(arr)

# Q2) Create linear and binary search algorithm to find data in an array


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


def detectBounds(uniqueSortedList):

    highestValue = uniqueSortedList[len(uniqueSortedList) - 1]
    lowestValue = uniqueSortedList[0]
    middleIndex = len(uniqueSortedList) // 2

# ============= #
# Binary Search #
# ============= #


def binarySearch():

    uniqueSortedList = makeUniqueList()
    searchValue = getSearchValue()
    detectBounds(uniqueSortedList)

    # if searchValue == uniqueSortedList:
    # print(f"The value that you are searching for is at index {middleIndex}.")

# ============= #
# Linear Search #
# ============= #


def linearSearch():
    """
    The function linearSearch() takes a list of unique numbers and a search value, and returns the index
    of the search value if it is in the list, and returns a message if the search value is not in the
    list.
    """

    uniqueList = makeUniqueList()
    searchValue = getSearchValue()

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


# Q3) create sorting algorithm using bubble, insertion, selection to sort data in an array
def makeRandomList():
    """
    It creates a list of 30 random integers between 0 and 99
    :return: A list of 30 random integers between 0 and 99.
    """
    import random
    highestInteger = 99
    lowestInteger = 0

    randomList = []

    for i in range(30):
        randomList.append(random.randint(lowestInteger, highestInteger))


    print(f"\n{randomList} <== Random list.\n")

    return(randomList)

# Bubble Sort algorithm
def bubbleSort():
    """
    The function makes a random list, then iterates through the list, comparing each element to the next
    element, and if the first element is greater than the second element, the two elements are swapped
    """
    import time

    randomList = makeRandomList()
    time.sleep(2)
    l = len(randomList)

# Iterating through the list and comparing each element to the next element, and if the first element
# is greater than the second element, the two elements are swapped.
    print("Starting Bubble Sort")
    for i in range(l):
        for j in range(l):
            k = j + 1
            try:
                if randomList[j] > randomList[k]:
                    randomList[j], randomList[k] = randomList[k], randomList[j]
                    print(randomList)
                    time.sleep(0.05)
            except IndexError:
                break
# Printing the sorted array.
    print(f"\n{randomList} <== Sorted array")


# Insertion Sort algorithm
def insertionSort():
    """
    For each element in the list, if the element is less than the element before it, swap the two
    elements
    """
    import time

    randomList = makeRandomList()
    time.sleep(2)
    l = len(randomList)

# Iterating through the list and comparing each element to the element before it, and if the
# element is less than the element before it, the two elements are swapped.
    print("Starting Insertion Sort")
    for h in range(l):
        for i in range(1, l):
            j = i - 1

            if randomList[i] < randomList[j]:
                randomList[i], randomList[j] = randomList[j], randomList[i]
                print(randomList)
                time.sleep(0.05)


# Selection Sort algorithm

def selectionSort():

    import time
    randomList = makeRandomList()
    l = len(randomList)

    lowestVal = randomList[0]
    for i in range(1, l):






# Q4) Create a recursive algorithm to calculate a factorial
def factorial():
    """
    This function takes an integer from the user and prints the factorial of that integer
    """
# Trying to get an integer from the user and if the user enters a non-integer, it will print an error
# message.
    try:
        x = int(input("Enter an integer for factorial: "))
    except ValueError:
        print("ValueError. Enter an integer for factorial")

# A while loop that is multiplying the factorial by the integer and then subtracting 1 from the
# integer until the integer is 0.
    factorial = 1

    while x != 0:
        factorial *= x
        x -= 1
    print(f"Factorial of your integer is: {factorial}")


# ================= #
# Calling Functions #
# ================= #
# insertDeleteIntegers()
# binarySearch()
# linearSearch()
# bubbleSort()
# insertionSort()
selectionSort()
# factorial()
