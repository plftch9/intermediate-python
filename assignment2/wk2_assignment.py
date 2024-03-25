"""
Paul Fitch
Wk2 Assignment
22 Jan 2023
SDEV 300-7615

This program will create strong passwords and calculate the following math :
percentages, days until 4 july 2025, volume of right cirular cylinder
"""

import random
import array
import math
from datetime import date


def greeting():
    """
    This function will print a greeting to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Welcome to math and secure password generator!")


def farewell():
    """
    This function will print a farewell message to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Thank you for using the program, goodbye!")


def print_menu():
    """
    This function prints the menu for the main function
    params: none
    user inputs: none
    return value: none
    """
    print("Type and enter options using numbers from the menu")
    print("1. Generate Password\n2. Calculate and Format a Percentage")
    print("3. How Many Days Until July 4, 2025\n4. Use Law of Cosines to Find Leg of Triangle")
    print("5. Calculate Volume of Right Circular Cylinder\n9. Exit Program")


def get_password_length():
    """
    This function will prompt and validate desired length of secure password
    params: none
    user inputs: desired length of password
    return value: desired length of password
    """
    while True:
        try:
            password_length = int(
                input("First enter the desired password length (min 4, max 20): "))
        except ValueError:
            print("You must enter an integer")
            continue

        if password_length < 4:
            print("Password length too short")
            continue

        if password_length > 20:
            print("Password length too long")
            continue

        return password_length


def get_password_complexity():
    """
    This function will prompt and validate desired complexity of secure password
    params: none
    user inputs: menu options denoting complexity element
    return value: list of chosen values
    """
    # empty "cart" to be appended with complexity options
    complexity_options = []

    print("Next select complexity options."
          f'{"Type and enter options one at a time using numbers from menu" : <20}')
    print("1. Upper case characters\n2. Lower case characters\n3. Numbers\n4. Symbols\n9. Continue")

    loop_control = True
    while loop_control:

        complexity_selection = input("Enter your selection: ")

        if complexity_selection in complexity_options:
            print("That complexity option is already enabled")
            continue

        if complexity_selection == "1":
            complexity_options.append(complexity_selection)
            print("Upper case characters enabled")
            continue

        if complexity_selection == "2":
            complexity_options.append(complexity_selection)
            print("Lower case characters enabled")
            continue

        if complexity_selection == "3":
            complexity_options.append(complexity_selection)
            print("Numbers enabled")
            continue

        if complexity_selection == "4":
            complexity_options.append(complexity_selection)
            print("Symbols enabled")
            continue

        if complexity_selection == "9":
            if len(complexity_options) < 1:
                print("You must select at least one option")
                continue

            loop_control = False

        else:
            print("That is not one of the options")

    return complexity_options


def password(length, complexity_selections):
    """
    This function will generate a password with desired length and complexity
    params: desired length of password, list containing complexity options
    user inputs: none
    return value: none
    """

    # initialize as empty strings
    random_upper = ""
    random_lower = ""
    random_number = ""
    random_symbol = ""

    character_list = []

    final_password = ""

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']

    upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z']

    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    for i in complexity_selections:
        if i == "1":
            # if option is selected from previous step, add upper case characters to pool
            character_list = character_list + upper_case_letters
            # assign a random upper character
            random_upper = random.choice(upper_case_letters)

        if i == "2":
            # if option is selected from previous step, add lower case characters to pool
            character_list = character_list + lower_case_letters
            # assign a random lower character
            random_lower = random.choice(lower_case_letters)

        if i == "3":
            character_list = character_list + numbers
            random_number = random.choice(numbers)

        if i == "4":
            character_list = character_list + symbols
            random_symbol = random.choice(symbols)

    # prime the first characters of the password with 1 of each selected complexity option
    primed_password = random_lower + random_upper + random_number + random_symbol

    for i in range(length - len(primed_password)):
        primed_password = primed_password + random.choice(character_list)

        # create an array containing each character in primed password
        primed_password_list = array.array('u', primed_password)
        # shuffle the characters to prevent patterns
        random.shuffle(primed_password_list)

    for i in primed_password_list:
        # re-assemble shuffled characters into final password
        final_password = final_password + i

    print("\nPassword: " + final_password + "\n")


def get_numerator():
    """
    This function will prompt the user for a numerator
    params: none
    user inputs: value of numerator
    return value: numerator of fraction
    """

    while True:
        try:
            numerator = int(input("First enter the numerator: "))
        except ValueError:
            print("You must enter an integer")
            continue
        return numerator


def get_denominator():
    """
    This function will prompt the user for a denominator
    params: none
    user inputs: value of denominator
    return value: denominator of fraction
    """
    while True:
        try:
            denominator = int(input("Next enter the denominator: "))
        except ValueError:
            print("You must enter an integer")
            continue

        return denominator


def get_digits():
    """
    This function will prompt the user for number of desired decimal places
    params: none
    user inputs: desired number of decimal places
    return value: user defined decimal places
    """
    while True:
        try:
            digits = int(input("Finally enter the number of decimal places: "))
        except ValueError:
            print("You must enter an integer")
            continue
        return digits


def percentage(numerator, denominator, digits):
    """
    This function will calculate a percentage from numbers provided by users
    and format to a user defined decimal length
    params: numerator of fraction, denominator of fraction, desired decimal points
    user inputs: none
    return value: none
    """
    product = (numerator / denominator) * 100
    # format to user defined decimal places
    print("Answer: "f"{product:.{digits}f}%" "\n")


def calculate_days():
    """
    This function will calculate the number of days from current date to July 4, 2025
    params: none
    user inputs: none
    return value: none
    """
    today = date.today()
    july_4_2025 = date(2025, 7, 4)
    date_difference = july_4_2025 - today
    print("Days until July 4, 2025: ", date_difference.days, "\n")


def get_side_length():
    """
    This function will prompt the user for the length of a side of a triangle
    params: none
    user inputs: length of triangle side
    return value: length of triangle side
    """
    while True:
        try:
            side = int(input("Enter the length of the side: "))
        except ValueError:
            print("You must enter an integer")
            continue

        return side


def get_angle():
    """
    This function will prompt the user for the degrees in an angle
    params: none
    user inputs: degrees of an angle
    return value: degrees of an angle
    """
    while True:
        try:
            angle = int(input("Enter the degrees of an angle: "))
        except ValueError:
            print("You must enter an integer")
            continue

        if angle >= 180:
            print("There are only 180° in a triangle")
            continue
        return angle


def triangle(side_a, side_b, angle):
    """
    This function calculates the missing side of a triangle using the law of cosines
    params: length of side a, length of side b, opposite angle of side c
    user inputs: none
    return value: none
    """
    side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 *
                       side_a * side_b * math.cos(math.radians(angle)))

    # format to 4 decimal places
    print("Answer: "f"{side_c:.{4}f}" "\n")


def get_radius():
    """
    This function prompts the user for the raduis of a cylinder
    params: none
    user inputs: numerical value of radius
    return value: radius of cylinder
    """
    while True:
        try:
            radius = int(input("Enter the radius of the cylinder: "))
        except ValueError:
            print("You must enter an integer")
            continue

        return radius


def get_height():
    """
    This function prompts the user for the height of a cylinder
    params: none
    user inputs: numerical value of cylinder height
    return value: cylinder height
    """
    while True:
        try:
            height = int(input("Enter the height of the cylinder: "))
        except ValueError:
            print("You must enter an integer")
            continue

        return height


def cylinder_volume(radius, height):
    """
    This function calculates and displays the volume of a cylinder
    params: raduis and height of cylinder
    user inputs: none
    return value: none
    """
    volume = math.pi * (radius ** 2) * height

    # format to 4 decimal places
    print("The volume of the cylinder is: "f"{volume:.{4}f}" "\n")


def main():
    """
    This main function will run at program startup
    it will prompt the user for desired services and call
    functions necessary to fulfil user needs
    params: none
    user inputs: menu options denoting desired services
    return value: none
    """

    greeting()
    while True:
        print_menu()
        user_select = input("Enter your selection: ")

        if user_select == "1":
            print()
            password(get_password_length(), get_password_complexity())
            continue

        if user_select == "2":
            print()
            percentage(get_numerator(), get_denominator(), get_digits())
            continue

        if user_select == "3":
            print()
            calculate_days()
            continue

        if user_select == "4":
            print()
            triangle(get_side_length(), get_side_length(), get_angle())
            continue

        if user_select == "5":
            print()
            cylinder_volume(get_radius(), get_height())
            continue

        if user_select == "9":
            farewell()
            break

        print("That is not one of the options")


main()
