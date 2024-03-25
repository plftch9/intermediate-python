"""
Paul Fitch
Wk3 Assignment
28 Jan 2023
SDEV 300-7615

This program will Display information on all 50 states, images of state flowers,
and a bar graph of top 5 populations
"""

import matplotlib.pyplot as plt
import states
import flower_module

# pylint for some reason reports that states and flower module have no members
# pylint: disable=no-member


def greeting():
    """
    This function will print a greeting to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Welcome to state information display!")


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
    print("1. Display all states in alphabetical order")
    print("2. Search for a specific state and show picture of state flower.")
    print("3. Provide a Bar graph of the top 5 populated States showing their overall population.")
    print("4. Update the overall state population for a specific state.")
    print("5. Exit Program")


def get_state_and_flower():
    """
    This function searches for desired state, gets path of state flower image file, and displays
    the state information with the image
    params: none
    user inputs: name of state to be searched
    return value: none
    """

    search = input("Enter full state name to search:\t")
    target = states.search_states(search)
    if target == -1:
        return
    for i in flower_module.FLOWERS:
        if i["name"] == target[0]["flower"]:
            print(target[0]["name"], "\nCapital:", target[0]["capitol"], ", Population:",
                  target[0]["population"], "\nFlower:", target[0]["flower"])
            plt.imshow(plt.imread(i["path"]))
            plt.show()


def graph_top_populations():
    """
    this function gets the information from the 5 states with highest populations
    and creates a bar graph to compare them
    params: none
    user inputs: none
    return value: none
    """
    topfivepop = states.top_five_population()
    for i in topfivepop:
        # print(i["name"], i["population"])
        plt.bar(i["name"], i["population"], color="maroon", width=0.4)

    plt.ticklabel_format(axis="y", style='plain')
    plt.xlabel("States")
    plt.ylabel("Populations")
    plt.title("Top 5 State Populations")
    plt.show()


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
        print()
        print_menu()
        user_select = input("Enter your selection: ")

        if user_select == "1":
            print()
            states.display_states_alphabetical()
            continue

        if user_select == "2":
            print()
            get_state_and_flower()
            continue

        if user_select == "3":
            graph_top_populations()
            continue

        if user_select == "4":
            print()
            states.update_population()
            continue

        if user_select == "5":
            farewell()
            loop_control = False

        else:
            print("That is not one of the options")


main()
