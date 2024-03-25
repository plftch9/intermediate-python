"""
Paul Fitch
SDEV 300-7615
Wk4 Assignment
5 February 2023

This program tests formats of phone numbers and zip codes as well as taking two user input \
matrices and performing mathematical operations
"""

import re
import numpy as np


def greeting():
    """
    This function will print a greeting to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Welcome to matrix game!")


def farewell():
    """
    This function will print a farewell message to the user
    params: none
    user inputs: none
    return value: none
    """
    print("Thank you for using the program, goodbye!")


def play():
    """
    This function will gather input from the user denoting if they would like to play again
    params: none
    user input: option from yes / no menu
    return value: boolean value of user selection
    """

    while True:
        print("Do you want to play the Matrix Game?")
        user_select = input("Enter Y for Yes or N for No: ")
        if user_select.lower() == "y":
            print()
            return True
        if user_select.lower() == "n":
            print()
            return False

        print("please enter \"Y\" or \"N\"")


def get_phone_number():
    """
    This function prompts and validates phone numbers and phone number format
    params: none
    user input: user's phone number in specific format
    return value: none
    """
    loop_control = True
    while loop_control:
        phone_number = input(
            "Please input your phone number (XXX-XXX-XXXX):\n")
        if len(re.findall(r"[\d]{3}-[\d]{3}-[\d]{4}", phone_number)) == 0:
            print("Your phone number is not in the correct format")
            continue
        print()
        loop_control = False


def get_zip():
    """
    This function prompts and validates zip codes and zip code format
    params: none
    user input: user's zip code in specific format
    return value: none
    """
    loop_control = True
    while loop_control:
        zip_code = input("Please enter your zip code + 4 (XXXXX-XXXX):\n")
        if len(re.findall(r"[\d]{5}-[\d]{4}", zip_code)) == 0:
            print("Your zip code is not in the correct format")
            continue
        print()
        loop_control = False


def populate_matrix():
    """
    This function gathers input to populate a numpy matrix
    params: none
    user input: nine values to be added to matrix
    return value: matrix with user specified values
    """
    # pylint: disable=invalid-name
    while True:
        try:
            a, b, c = map(int,
                          input("Enter first three matrix numbers seperated by a space: ").split())
        except ValueError:
            print("Too many inputs, or invalid input type")
            continue
        break

    while True:
        try:
            i, j, k = map(int,
                          input("Enter next three matrix numbers seperated by a space: ").split())
        except ValueError:
            print("Too many inputs, or invalid input type")
            continue
        break

    while True:
        try:
            x, y, z = map(int,
                          input("Enter last three matrix numbers seperated by a space: ").split())
        except ValueError:
            print("Too many inputs, or invalid input type")
            continue
        break

    matrix = np.array([[a, b, c], [i, j, k], [x, y, z]])
    print()
    # pylint: enable=invalid-name
    return matrix


def get_operation(mat_x, mat_y):
    """
    This function allows users to select the operation to perform on matrices
    params: matrices used for operations
    user input: menu item
    return value: none
    """
    loop_control = True
    while loop_control:
        print(
            "Select a Matrix Operation from the list below: \n \
    a. Addition \n \
    b. Subtraction \n \
    c. Matrix Multiplication \n \
    d. Element by element multiplication")
        user_select = input("Selection: ")
        if user_select.lower() == "a":
            print()
            matrix_addition(mat_x, mat_y)
            loop_control = False
            continue

        if user_select.lower() == "b":
            print()
            matrix_subtraction(mat_x, mat_y)
            loop_control = False
            continue

        if user_select.lower() == "c":
            print()
            matrix_mult(mat_x, mat_y)
            loop_control = False
            continue

        if user_select.lower() == "d":
            print()
            mult_by_element(mat_x, mat_y)
            loop_control = False
            continue

        print("That is not one of the options")


def matrix_addition(mat_x, mat_y):
    """
    This function performs and displays result of matrix addition
    params: two matrices to be used in matrix addition
    user inputs: none
    return value: none
    """
    result = mat_x + mat_y
    print("Matrix addition result = \n", result[0][0], result[0][1], result[0][2],
          "\n", result[1][0], result[1][1], result[1][2], "\n",
          result[2][0], result[2][1], result[2][2])
    print()
    show_transpose(result)
    print()
    show_axis_means(result)


def matrix_subtraction(mat_x, mat_y):
    """
    This function performs and displays result of matrix suptraction
    params: two matrices to be used in matrix subtraction
    user inputs: none
    return value: none
    """
    result = mat_x - mat_y
    print("Matrix subtraction result = \n", result[0][0], result[0][1], result[0][2],
          "\n", result[1][0], result[1][1], result[1][2], "\n",
          result[2][0], result[2][1], result[2][2])
    print()
    show_transpose(result)
    print()
    show_axis_means(result)


def matrix_mult(mat_x, mat_y):
    """
    This function performs and displays result of matrix multiplication
    params: two matrices to be used in matrix multiplication
    user inputs: none
    return value: none
    """
    result = np.matmul(mat_x, mat_y)
    print("Matrix multiplication result = \n", round(result[0][0], 4),
          round(result[0][1], 4), round(result[0][2], 4),
          "\n", result[1][0], result[1][1], result[1][2], "\n",
          round(result[2][0], 4), round(result[2][1], 4), round(result[2][2], 4))
    print()
    show_transpose(result)
    print()
    show_axis_means(result)


def mult_by_element(mat_x, mat_y):
    """
    This function performs and displays result of matrix multiplication by element
    params: two matrices to be used in matrix multiplication by element
    user inputs: none
    return value: none
    """
    result = np.multiply(mat_x, mat_y)
    print("Element by element multiplication result = \n", result[0][0], result[0][1], result[0][2],
          "\n", result[1][0], result[1][1], result[1][2], "\n",
          result[2][0], result[2][1], result[2][2])
    print()
    show_transpose(result)
    print()
    show_axis_means(result)


def show_transpose(mat):
    """
    This function performs and displays result of transposing matrix
    params: matrix to be transposed
    user inputs: none
    return value: none
    """
    result = mat.transpose()
    print("Transpose of results = \n", result[0][0], result[0][1], result[0][2],
          "\n", result[1][0], result[1][1], result[1][2], "\n",
          result[2][0], result[2][1], result[2][2])


def show_axis_means(mat):
    """
    This function performs and displays result of matrix mean by column and row
    params: matrix to find column / row mean
    user inputs: none
    return value: none
    """
    y_axis = np.mean(mat, axis=0)
    x_axis = np.mean(mat, axis=1)
    print("row means = ", round(y_axis[0], 4), round(
        y_axis[1], 4), round(y_axis[2], 4))
    print("column means = ", round(x_axis[0], 4), round(
        x_axis[1], 4), round(x_axis[2], 4))
    print()


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
    loop_control = play()
    while loop_control:
        get_phone_number()
        get_zip()
        print("Enter the first 3 x 3 matrix")
        matrix_a = populate_matrix()
        print("Enter the second 3 x 3 matrix")
        matrix_b = populate_matrix()
        get_operation(matrix_a, matrix_b)
        loop_control = play()
    farewell()


main()
