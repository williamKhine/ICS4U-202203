def characters(string):
    """
    For each character in the string, if the character is in the dictionary, add one to the value of that key, otherwise,
    add the character to the dictionary with a value of 1.
    """
    dictionary = dict()
    # Iterating through the string and adding the characters to the dictionary.
    for i in string:
        keys = dictionary.keys()

        if i in keys:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    return dictionary


# Sorting the dictionary by the keys.
sorted_dict = dict(sorted(characters("William".lower()).items()))
print(sorted_dict)
