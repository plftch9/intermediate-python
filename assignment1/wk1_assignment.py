"""
Paul Fitch
Wk1 Assignment
16 Jan 2023
SDEV 300-7615

This program will simulate an application to allow users to register to vote
"""

import sys


def greeting():
    """
    This function will print a grreting to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Welcome to voter registration!")


def farewell():
    """
    This function will print a farewell message to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Thank you for using voter registration. Goodbye!")


def confirm():
    """
    This functon will gather confirmation that the user wants to continue
    params: none
    User input: y or n, denoting whether user wishes to continue or not
    return value: indication or user input
    """

    while True:
        confirmation = input(
            "Do you want to continue registration?\nType \"y\" or \"n\":\t")
        if confirmation.lower() == "y":
            return 1

        if confirmation.lower() == "n":
            return 0

        print("Answer not recognized.")


def get_age():
    """
    This functon will gather user age
    params: none
    User input: user age
    return value: user age, or -1
    """

    while True:
        try:
            user_age = int(input("Please enter your age:\t"))
        except ValueError:  # catches no input
            print("No input has been recorded")
        else:
            if user_age < 18:
                print("You must be at least 18 years old to vote. \
                        \nPlease come back when you are old enough!")
                return -1

            if user_age > 99:
                print("Please ensure that you have entered your correct age")
                continue

            return user_age


def get_first_name():
    """
    This function will gather user first name
    params: none
    user input: user first name
    return value: uaser first name
    """

    while True:
        user_first_name = input("Please enter your first name:\t")
        if len(user_first_name) < 3:  # length of first name should be 3 or more
            print("Please enter a valid name. Min 3 characters.")
            continue
        if user_first_name.isdigit():
            print("You cannot enter a number")
            continue
        return user_first_name.capitalize()


def get_last_name():
    """
    This function will gather user last name
    params: none
    user input: user last name
    return value: uaser last name
    """
    while True:
        user_last_name = input("Please enter your last name:\t")
        if len(user_last_name) < 3:  # length of last name shoud be 3 or more
            print("Please enter a valid name. Min 3 characters.")
            continue
        if user_last_name.isdigit():
            print("You cannot enter a number")
            continue
        return user_last_name.capitalize()


def get_citizen():
    """
    This function will gather whether the user is a US citizen
    params: none
    user input: y or n, denoting whether user is a US citizen
    return value: user citizenship, boolean value
    """

    while True:
        user_citizen = input(
            "Are you a US citizen?\nType \"y\" or \"n\":\t")
        if user_citizen.lower() == "y":
            return True

        if user_citizen.lower() == "n":
            return False

        print("Answer not recognized.")


def get_residence():
    """
    This function will gather user state residency
    params: none
    user input: abbreviated state code
    return value: abbriviated state code
    """

    states = ["al", "ak", "ar", "az", "ca", "co", "ct",  # all 50 states, plus 6 territories
              "de", "fl", "ga", "hi", "id", "il", "in",
              "ia", "ks", "ky", "la", "me", "md", "ma",
              "mi", "mn", "ms", "mo", "mt", "ne", "nv",
              "nh", "nj", "nm", "ny", "nc", "nd", "oh",
              "ok", "or", "pa", "ri", "sc", "sd", "tn",
              "tx", "ut", "vt", "va", "wa", "wv", "wi",
              "wy", "dc", "gu", "mh", "mp", "pr", "vi"]

    while True:
        user_state = input(
            "Please enter the state code of your state of residence:\t")
        if user_state.lower() in states:
            return user_state.upper()
        if user_state not in states:
            print("Please enter a valid state code")


def show_application(fname, lname, age, is_citizen, state_residence):
    """
    This function will print all information entered by user
    params: user first name, user last name, user age, user citizenship, user state of residence
    """
    print("Thank you for registering to vote. Here is the information you have provided:")

    print("First Name: ", fname, "\nLast Name: ", lname, "\nAge: ", age,
          "\nU.S. Citizen: ", is_citizen, "\nState of Residence: ", state_residence)


def main():
    """
    This main function will run at progrm startup
    It will call other functions to obtain necessary user inputs
    params: none
    user inputs: none
    return value: none
    """
    greeting()
    age = get_age()
    if age == -1:
        farewell()
        sys.exit()
    proceed = confirm()
    if proceed == 0:
        farewell()
        sys.exit()
    first_name = get_first_name()
    proceed = confirm()
    if proceed == 0:
        farewell()
        sys.exit()
    last_name = get_last_name()
    proceed = confirm()
    if proceed == 0:
        farewell()
        sys.exit()
    is_citizen = get_citizen()
    proceed = confirm()
    if proceed == 0:
        farewell()
        sys.exit()
    residence = get_residence()
    proceed = confirm()
    if proceed == 0:
        farewell()
        sys.exit()
    show_application(first_name, last_name, age, is_citizen, residence)
    farewell()


main()
