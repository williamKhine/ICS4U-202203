def store_input() -> list:
    # Creating a list of dictionaries.
    students = list()
    # Asking the user to input a name and age 10 times.
    for i in range(10):
        name: str = input("Enter name: ")
        age: int = int(input("Enter age: "))
        students.append({"name": name, "age": age})

    return students


def check_eligibility(students: list) -> list:
    # Checking if the age is less than 16 and if it is, it is setting the eligible key to False.
    for i in students:
        if i["age"] < 16:
            i["eligible"] = False
        else:
            i["eligible"] = True

    return students


def print_results(results: list) -> None:
    """
    It takes a list of dictionaries, and prints out the names and ages of the people who are eligible to drive, and the names
    and ages of the people who are not eligible to vote
    """
    eligible = list()
    not_eligible = list()

    # Checking if the eligible key is True or False, and if it is True, it is appending it to the eligible list,
    # and if it is False, it is appending it to the not_eligible list.
    for i in results:
        if i["eligible"]:
            eligible.append(i)
        else:
            not_eligible.append(i)

    # Checking if the eligible list is empty or not, and if it is not empty, it is printing out the names and ages of
    # the people who are eligible to drive, and if the not_eligible list is not empty, it is printing out the names
    # and ages of the people who are not eligible to drive.
    if len(eligible) != 0:
        print("Eligible")
        for i in eligible:
            print(i["name"], i["age"], end="\n\n")
    if len(not_eligible) != 0:
        print("Not Eligible")
        for i in not_eligible:
            print(i["name"], i["age"], end="\n\n")


def main():
    students = store_input()
    student_results = check_eligibility(students)
    print_results(student_results)


main()
