 # ICS4U Unit 1 Activity 9 - Code Maintenance Reading and Worksheet

Phone Pyae Thet Khine
Teacher NEDA
ICS4U
16th Feb 2022

```python
# Creating a dictionary with the keys listed in the list.
profile = dict.fromkeys([
    "firstname",
    "lastname",
    "birthplace",
    "school",
    "favourite_subject"
    ])

# Looping through the dictionary and asking for the user input.
for key in profile:
    profile[key] = input(f"What is your {key}?: ")


# Printing the string with the values from the dictionary.
print(f"""
To Whom This May Concern:
My name is {profile["firstname"]} {profile["lastname"]}. I am originated from {profile["birthplace"]}. I am currently attending
{profile["school"]} with my favorite course as {profile["favourite_subject"]}.
""")
```
Output
```txt
What is your firstname?: William
What is your lastname?: Khine
What is your birthplace?: Rangoon
What is your school?: Yorkville Highschool
What is your favourite_subject?: Computer Science

To Whom This May Concern:
My name is William Khine. I am originated from Rangoon. I am currently attending
Yorkville Highschool with my favorite course as Computer Science.
```