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