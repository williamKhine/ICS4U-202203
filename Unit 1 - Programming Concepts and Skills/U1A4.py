# ========================================== #
# Unit 1 - Activity 4 - Data Types Worksheet #
# ========================================== #


# Q1) Write a program to convert string to integer
def stringToInteger():
    string0 = '420'  # a variable of type string
    print('\nChanging data type', type(string0),
          'to', type(int(string0)))  # conversion
    print(int(string0), 'type of', type(int(string0)))  # output

# Q2) Write a program to convert Character to integer


def characterToInteger():
    char0 = 'A'  # a variable of type character
    print('\nChanging data type', type(char0),
          'to', type(ord(char0)))  # conversion
    print(ord(char0), 'type of', type(ord(char0)))  # output # output

# Q3) Write a program to convert integer to character


def integerToCharacter():
    int0 = 80  # a variable of type integer
    print('\nChanging data type', type(int0),
          'to', type(chr(int0)))  # conversion
    print(chr(int0), 'type of', type(chr(int0)))  # output

# Q4) Write a program to convert floating point to integer


def floatToInteger():
    float0 = 4.20  # a variable of type float
    print('\nChanging data type', type(float0),
          'to', type(int(float0)))  # conversion
    print(int(float0), 'type of', type(int(float0)))  # output


# ================= #
# Calling Functions #
# ================= #
stringToInteger()
characterToInteger()
integerToCharacter()
floatToInteger()
