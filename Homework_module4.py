""" Homework 4  - needs to be presented before exam day"""
import random

# We want to check which of the following function has the smallest minimum for x in range -10, 10 and use that function
# to calculate for x = 0
# 1x^2 -2x + 2
# 2x^2 -4x + 4
# 3x^2 -6x + 6

# 20P
# Create a function (build) that takes 3 int arguments (a, b, c) and return a function (response) that takes one int
# argument (x) and calculates ax^2+bx+c
x = random.randint(-10, 10)


def build(a, b, c):
    """
    :param a: first argument for build function used for ax^2+bx+c equation
    :param b: second argument for build function used for ax^2+bx+c equation
    :param c: last argument for build function used for ax^2+bx+c equation
    :return: function returns a function that takes one int argument x
    """

    def response(x):
        """
        :param x: argument that was inserted from keyboard
        :return: the result of the equation ax^2+bx+c
        """
        return int(a) * x ** 2 + int(b) * x + int(c)
    return response(x)


# 20P
# Create a list of response functions by calling build function with the arguments (1,-2,3), (2,-4,4), (3,-6,5)
list_of_functions = []
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a,b,c))

# 20P
# Create a dictionary that contains the result functions as keys and as values the list of results from calling that
# function with x in range -10, 10 as value
dict_of_results = {}
print("Generated x is: ", x)
i = 0
result_function_name_list=[]
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    result_function_name_list.append(str(a) + "*x^2 " + str(b)+"*x +" + str(c))

for function in list_of_functions:
    temp_dict={result_function_name_list[i]: function }
    dict_of_results.update(temp_dict)
    i += 1

print("dict_of_result is:", dict_of_results)

# 20P
# Check dict_of_results and determine which function has the smallest value in the list of values

function_with_smallest_result = min(dict_of_results.keys())
smallest_value = min(dict_of_results.values())

print("Function with smallest result is", function_with_smallest_result)
print("The value of the function with smallest result is", smallest_value)


# # 20P
# # Call function_with_smallest_result with argument x = 0 and print the returned value (you should get 2)
# pass  # <your code here>
a=int(function_with_smallest_result[0:1])
b=int(function_with_smallest_result[6:8])
c=int(function_with_smallest_result[-1])
x=0
print(build(a,b,c))


