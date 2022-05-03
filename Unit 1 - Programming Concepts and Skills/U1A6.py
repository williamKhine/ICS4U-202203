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
        print(arr)
    print("Array is empty. No more elements to remove.")
    
def insertDeleteIntegers():
    """
    This function will insert integers into an array and then delete integers from the array.
    """
    arr = [] # Declaring a blank array

    insertIntegers(arr)
    deleteIntegers(arr)

# Q2) Create linear and binary search algorithm to find data in an array

# Binary Search #

def makeUniqueSortedList():
    import random

    highestInteger = 99
    lowestInteger = 0

    unsortedList = []
    sortedList = []

    for i in range(30):
        unsortedList.append(random.randint(lowestInteger, highestInteger))

    uniqueSortedList = list(set(unsortedList))

    print(f"\n{unsortedList} <== unsorted list.\n")
    print(f"{uniqueSortedList} <== unique sorted list.\n")

    return(uniqueSortedList)


def getSearchValue():

    while True:
        try:
            searchValue = int(input(f"Which integer do you want to search? (0 to 99): "))
        except ValueError:
            print("ValueError. Please enter an integer.")
        else:
            break
    
    return(searchValue)


def detectBounds(uniqueSortedList):

    highestValue = uniqueSortedList[len(uniqueSortedList) - 1]
    lowestValue = uniqueSortedList[0]
    middleIndex = len(uniqueSortedList) // 2


def binarySearch():

    uniqueSortedList =  makeUniqueSortedList()
    searchValue = getSearchValue()
    detectBounds(uniqueSortedList)

    # if searchValue == uniqueSortedList:
        # print(f"The value that you are searching for is at index {middleIndex}.")

# Linear Search #
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
    


def linearSearch():
    """
    The function linearSearch() takes a list of unique numbers and a search value, and returns the index
    of the search value if it is in the list, and returns a message if the search value is not in the
    list.
    """

    uniqueList = makeUniqueList()
    searchValue = getSearchValue()

    for i in range(len(uniqueList) - 1):
        if searchValue == uniqueList[i]:
            print(f"The value that you are searching for is at index {i}.")
            break
    else:
        print(f"The value that you are searching for is not in the list: \n{uniqueList}")




# Q3) create sorting algorithm using bubble, insertion, selection to sort data in an array

# Bubble Sort algorithm

# Insertion Sort algorithm

# Selection Sort algorithm

# Q4) Create a recursive algorithm to calculate a factorial





# ================= #
# Calling Functions #
# ================= #
insertDeleteIntegers()
# binarySearch()
# linearSearch()
