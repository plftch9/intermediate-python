"""
Paul Fitch
SDEV 300-7615
Wk5 Assignment
10 February 2023

This program opens csv files and presents graphs based on contained data
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


def greeting():
    """
    This function will print a greeting to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Welcome to CSV file reader!")


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
    This function prints the menu used to select optinos in the main function
    params: none
    user inputs: none
    return value: none
    """
    print("Type and enter options using numbers from the menu")
    print("1. Load Population Data\n2. Load Housing\n9. Exit Program")


def population_menu():
    """
    This function prints the menu used to select options related to population
    params: none
    user inputs: none
    return value: none
    """
    print("Select column to analyze")
    print("1. April 1 Pop\n2. July 1 Pop\n3. Population Change\n9. Return to Main Menu")


def housing_menu():
    """
    This function prints the menu used to select options related to housing
    params: none
    user inputs: none
    return value: none
    """
    print("Select column to analyze")
    print("1. Age\n2. Bedrooms\n3. Built\n4. Rooms\n5. Utility\n9. Return to Main Menu")


def select_csv(selection):
    """
    This function determines path and file needed for selected operations
    params: string value denoting selected csv file (pop change or housing)
    user inputs: none
    return value: path to necessary file
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if selection == "pop_change":
        current_dir = current_dir + r"\csv_files\PopChange.csv"

    if selection == "housing":
        current_dir = current_dir + r"\csv_files\Housing.csv"

    return current_dir


def create_graph(data_frame, column):
    """
    This function creates a histogram graph from data in specific colums of csv file
    params: panda data frame, column to graph
    user inputs: none
    return value: none
    """
    data_frame[column].hist(align='right', edgecolor='black')
    plt.show()
    plt.close()


def population():
    """
    This function gathers user input to determine which column information is displayed and graphed
    and calls functions to display and graph the columns
    params: none
    user input: numeric value from menu, denoting selected column
    return value: none
    """
    file_path = select_csv("pop_change")
    frame = pd.read_csv(file_path)
    loop_control = True
    while loop_control:
        print()
        population_menu()
        user_select = input("Enter your selection: ")
        if user_select == "1":
            print()
            print("April 1 population:")
            print(frame["Pop Apr 1"].describe())
            create_graph(frame, "Pop Apr 1")

        if user_select == "2":
            print()
            print("July 1 population:")
            print(frame["Pop Jul 1"].describe())
            create_graph(frame, "Pop Jul 1")

        if user_select == "3":
            print()
            print("Population Change:")
            print(frame["Change Pop"].describe())
            create_graph(frame, "Change Pop")

        if user_select == "9":
            print()
            loop_control = False

        else:
            print("That is not one of the options")


def housing():
    """
    This function gathers user input to determine which column information is displayed and graphed
    and calls functions to display and graph the columns
    params: none
    user input: numeric value from menu, denoting selected column
    return value: none
    """
    file_path = select_csv("housing")
    frame = pd.read_csv(file_path)
    loop_control = True
    while loop_control:
        print()
        housing_menu()
        user_select = input("Enter your selection: ")
        if user_select == "1":
            print()
            print("Housing Age:")
            print(frame["AGE"].describe())
            create_graph(frame, "AGE")

        if user_select == "2":
            print()
            print("Housing Bedrooms:")
            print(frame["BEDRMS"].describe())
            create_graph(frame, "BEDRMS")

        if user_select == "3":
            print()
            print("Housing Built:")
            print(frame["BUILT"].describe())
            create_graph(frame, "BUILT")

        if user_select == "4":
            print()
            print("Housing Rooms:")
            print(frame["ROOMS"].describe())
            create_graph(frame, "ROOMS")

        if user_select == "5":
            print()
            print("Housing Utility:")
            print(frame["UTILITY"].describe())
            create_graph(frame, "UTILITY")

        if user_select == "9":
            print()
            loop_control = False
        else:
            print("That is not one of the options")


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
    loop_control = True
    while loop_control:
        print_menu()
        user_select = input("Enter your selection: ")
        if user_select == "1":
            population()
            continue

        if user_select == "2":
            housing()
            continue

        if user_select == "9":
            farewell()
            loop_control = False

        else:
            print("That is not one of the options")
            print()


main()
