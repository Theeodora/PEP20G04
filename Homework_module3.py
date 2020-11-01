""" Homework 3  - needs to be presented before exam day"""
# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have there length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]


def ordered_ints(given_list):
    """
    :param given_list: List of which elements have to be converted and reversed sorted
    :return: New sorted list of integers
    """
    pass
    for element in range(0, len(given_list)):
        if type(given_list[element]) == int:
            print("Element is already an int. Nothing to do.")
        elif type(given_list[element]) == str:
            print("Element is a string. \n Element can be converted.")
            given_list[element] = int(given_list[element])
        elif isinstance(given_list[element], int):
            print("Element i san instance of int. \n Element can be converted.")
            given_list[element] = int(given_list[element])
        elif type(given_list[element]):
            print("Element is not convertible to an int.")
            given_list[element] = len(given_list[element])
    sorted_list = sorted(given_list, reverse=True)
    print("Sorted list is", sorted_list)


print(ordered_ints([1, True, '123', False, 6, ()]))


# 25P - (do not rush to resolve this)
# For recursive functions try reading teh articles below
# https://realpython.com/python-thinking-recursively/
# https://www.python-course.eu/python3_recursive_functions.php
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n):
    """
    :param n: Int that indicates the number of iterations
    :return: Result of sum of square (ex. (1^2)+(2^2)+(3^2)...(n^2))
    """
    pass
    if n == 1:
        return 1
    else:
        return n ** 2 + sum_of_square(n - 1)


print("The sum of square for 10 is: ", sum_of_square(10))


# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n):
    """
    :param n: Number of iterations
    :return: Factorial of square
    """
    pass
    if n == 1:
        return 1
    else:
        return n ** 2 * factorial_of_squares(n - 1)


print("The factorial of squares for 5 is:", factorial_of_squares(5))


# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text de te5t" will become  ("1234567A", "_ext_de_te_t")

def process_text(given_string):
    pass
    if not type(given_string) == str:
        print("The input have to be a string.")
        StopIteration
    else:
        given_string = given_string.split(" ", 1)
        given_string[0] = given_string[0].upper()
        for letter in given_string[1]:
            print(letter)
            if not letter.islower():
                given_string[1] = given_string[1].replace(letter, "_")
    new_tuple = (given_string[0], given_string[1])
    return new_tuple


print("The processed text is: ", process_text('1234567a Text de te5t'))
