# Q1) 2) Recursive Functions

def recursive_function(num):
    if num != 0:
        print(num)
        recursive_function(num - 1)


recursive_function(5)

# function2()

# Q1) 3) Loops

x = 10

while x != 0:
    print(x)
    x -= 1

# Q2)


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


def linear_search(unique_list, search_value):
    count = 0
    for i in range(len(unique_list) - 1):
        count += 1
        if search_value == unique_list[i]:
            print(f"The value that you are searching for is at index {i} (Linear Search).")
            break

    else:
        print(
            f"The value that you are searching for is not in the list: \n{unique_list}")
    return count


def binary_search(unique_list, search_value):
    
    start_index = 0
    end_index = len(unique_list) - 1

    count = 0

    found = False

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        middle_value = unique_list[middle_index]

        if middle_value == search_value:
            print(f"The value that you are searching for is at index {middle_index} (Binary Search).")
            found = True
            count += 1
            break
        elif middle_value < search_value:
            start_index = middle_index + 1
            count += 1
        else:
            end_index = middle_index - 1
            count += 1
            
    if found is False:
        print(f"The value that you are searching for is not in the list: \n{unique_list}")

    return count


import time

unique_list_Q2 = make_unique_list()
search_value_Q2 = int(input("What number are you searching for? (1 - 100): "))

start = time.time()
linear_count = linear_search(unique_list_Q2, search_value_Q2)
end = time.time()
linear_time = end - start

start = time.time()
binary_count = binary_search(unique_list_Q2, search_value_Q2)
end = time.time()
binary_time = (end - start)

print(f"Linear Search makes {linear_count} operation(s) and took {linear_time}")
print(f"Binary Search makes {binary_count} operation(s) and took {binary_time}")

# Q3)


def fibonacci():
    n = int(input("How many sequences of the fibonacci do you want?: "))

    if n == 1:
        print([1])
    elif n == 2:
        print([1, 2])
    else:
        n -= 2

        fibonacci_result = [1, 2]
        for i in range(n):
            fibonacci_result.append(fibonacci_result[-1] + fibonacci_result[-2])
        print(fibonacci_result)


fibonacci()

# Q4)

import turtle as t

t.speed(1)
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()
