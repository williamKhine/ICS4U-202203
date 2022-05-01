# ICS4U Unit 1 Activity 4 - Data Types Worksheet

Phone Pyae Thet Khine
ICS4U
4th Feb 2022

##### 1. Write a program to convert string to integer.
```python
string0 = '420' # a variable of type string
print('Changing data type', type(string0), 'to', type(int(string0))) # conversion
print(int(string0), 'type of', type(int(string0))) # output
```
Output
```txt
Changing data type <class 'str'> to <class 'int'>
420 type of <class 'int'>
```
##### 2. Write a program to convert Character to integer.
```python
char0 = 'A' # a variable of type character
print('Changing data type', type(char0), 'to', type(ord(char0))) # conversion
print(ord(char0), 'type of', type(ord(char0))) # output # output
```
Output
```txt
Changing data type <class 'str'> to <class 'int'>
65 type of <class 'int'>
```
##### 3. Write a program to convert integer to character.
```python
int0 = 80 # a variable of type integer
print('Changing data type', type(int0), 'to', type(chr(int0))) # conversion
print(chr(int0), 'type of', type(chr(int0))) # output
```
Output
```txt
Changing data type <class 'int'> to <class 'str'>
P type of <class 'str'>
```
##### 4.Write a program to convert floating point to integer.
```python
float0 = 4.20 # a variable of type float
print('Changing data type', type(float0), 'to', type(int(float0))) # conversion
print(int(float0), 'type of', type(int(float0))) # output
```
Output
```txt
Changing data type <class 'float'> to <class 'int'>
4 type of <class 'int'>
```