# ================================================= #
# Unit 1 - Activity 6 - Array Reading and Worksheet #
# ================================================= #

# Binary Search


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


    if searchValue == uniqueSortedList[middleIndex]:
        print(f"The value that you are searching for is at index {middleIndex}.")



# Linear Search
def makeUniqueList():
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

    uniqueList = makeUniqueList()
    searchValue = getSearchValue()

    for i in range(len(uniqueList) - 1):
        if searchValue == uniqueList[i]:
            print(f"The value that you are searching for is at index {i}.")
            break
    else:
        print(f"The value that you are searching for is not in the list: \n{uniqueList}")




# ================= #
# Calling Functions #
# ================= #
binarySearch()
linearSearch()