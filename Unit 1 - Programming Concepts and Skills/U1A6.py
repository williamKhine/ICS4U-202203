# ================================================= #
# Unit 1 - Activity 6 - Array Reading and Worksheet #
# ================================================= #

# Q1) Write an Algorithm to insert and delete array elements

def insert_integers(arr):
    """
    The function `insert_integers` takes an array as an argument and appends integers to the array until
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


def delete_integers(arr):
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


def insert_delete_integers():
    """
    This function will insert integers into an array and then delete integers from the array.
    """
    arr = []  # Declaring a blank array

    insert_integers(arr)
    delete_integers(arr)


# Q2) Create linear and binary search algorithm to find data in an array


def make_unique_list():
    """
    It creates a list of 30 random integers between 0 and 99, then it removes all duplicates from the
    list
    :return: A list of unique integers.
    """
    import random

    highest_integer = 99
    lowest_integer = 0

    non_unique_list = []

    for i in range(30):
        non_unique_list.append(random.randint(lowest_integer, highest_integer))

    unique_list = list((set(non_unique_list)))

    print(f"\n{non_unique_list} <== list, probably not unique.\n")
    print(f"{unique_list} <== truly unique list.\n")

    return unique_list


def get_search_value():
    while True:
        try:
            search_value = int(
                input(f"Which integer do you want to search? (0 to 99): "))
        except ValueError:
            print("ValueError. Please enter an integer.")
        else:
            break

    return search_value


# ============= #
# Binary Search #
# ============= #


def binary_search():
    """
    The function takes a list of unique numbers and a search value, and returns the index of the search
    value in the list
    """

    # Declaring variables that will be used in the binary_search() function.
    unique_list = make_unique_list()
    search_value = get_search_value()

    start_index = 0
    end_index = len(unique_list) - 1

    count = 0

    found = False

    # A binary search algorithm. It is searching for a value in a list.
    # Finding the middle index of the list.
    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        middle_value = unique_list[middle_index]

        # Checking if the middle value is equal to the search value. If it is, it prints the index of the
        # middle value.
        if middle_value == search_value:
            print(f"The value that you are searching for is at index {middle_index} (Binary Search).")
            found = True
            count += 1
            break
        # Checking if the middle value is less than the search value. If it is, it adds 1 to the
        # start index and adds 1 to the count.
        elif middle_value < search_value:
            start_index = middle_index + 1
            count += 1
        # Checking if the middle value is greater than the search value. If it is, it subtracts 1
        # from the end index and adds 1 to the count.
        else:
            end_index = middle_index - 1
            count += 1

    # Checking if the search value is not in the list. If it is not in the list, it prints
    # a message.
    if found is False:
        print(f"The value that you are searching for is not in the list: \n{unique_list}")


# ============= #
# Linear Search #
# ============= #


def linear_search():
    """
    The function linear_search() takes a list of unique numbers and a search value, and returns the index
    of the search value if it is in the list, and returns a message if the search value is not in the
    list.
    """

    unique_list = make_unique_list()
    search_value = get_search_value()

    # Iterating through the list and checking if the search value is equal to the value in the list.
    # If it is, it prints the index of the value in the list.
    for i in range(len(unique_list) - 1):
        if search_value == unique_list[i]:
            print(f"The value that you are searching for is at index {i} Linear Search.")
            break
    # Checking if the search value is not in the list.
    else:
        print(
            f"The value that you are searching for is not in the list: \n{unique_list}")


# Q3) create sorting algorithm using bubble, insertion, selection to sort data in an array
def make_random_list():
    """
    It creates a list of 30 random integers between 0 and 99
    :return: A list of 30 random integers between 0 and 99.
    """
    import random
    highest_integer = 99
    lowest_integer = 0

    random_list = []

    for i in range(30):
        random_list.append(random.randint(lowest_integer, highest_integer))

    print(f"\n{random_list} <== Random list.\n")

    return random_list


# Bubble Sort algorithm
def bubble_sort():
    """
    The function makes a random list, then iterates through the list, comparing each element to the next
    element, and if the first element is greater than the second element, the two elements are swapped
    """
    import time

    random_list = make_random_list()
    time.sleep(2)
    list_len = len(random_list)

    # Iterating through the list and comparing each element to the next element, and if the first element
    # is greater than the second element, the two elements are swapped.
    print("Starting Bubble Sort")
    for i in range(list_len):
        for j in range(list_len):
            k = j + 1
            try:
                if random_list[j] > random_list[k]:
                    random_list[j], random_list[k] = random_list[k], random_list[j]
                    print(random_list)
                    time.sleep(0.05)
            except IndexError:
                break
    # Printing the sorted array.
    print(f"\n{random_list} <== Sorted array")


# Insertion Sort algorithm
def insertion_sort():
    """
    For each element in the list, if the element is less than the element before it, swap the two
    elements
    """
    import time

    random_list = make_random_list()
    time.sleep(2)
    list_len = len(random_list)

    # Iterating through the list and comparing each element to the element before it, and if the
    # element is less than the element before it, the two elements are swapped.
    print("Starting Insertion Sort")
    for h in range(list_len):
        for i in range(1, list_len):
            j = i - 1

            if random_list[i] < random_list[j]:
                random_list[i], random_list[j] = random_list[j], random_list[i]
                print(random_list)
                time.sleep(0.05)


# Selection Sort algorithm

# def selectionSort():

#     import time
#     randomList = make_random_list()
#     l = len(randomList)

#     lowestValIndex = 0
#     for i in range(1, l):
#         if randomList[i] < randomList[lowestValIndex]:


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
    factorial_result = 1

    while x != 0:
        factorial_result *= x
        x -= 1
    print(f"Factorial of your integer is: {factorial_result}")


# ================= #
# Calling Functions #
# ================= #
# insert_delete_integers()
binary_search()
linear_search()
# bubble_sort()
# insertion_sort()
# selectionSort()
# factorial()
