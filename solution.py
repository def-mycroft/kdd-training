"""Solution to HW3"""
def smallest(*args):
    """takes an unlimited number of arguments and returns the smallest."""
    return reduce(lambda x, y: x if x < y else y, args)


def swap_last_first(integer):
    """ Interchanges the first and last digits"""
    return int(str(integer)[-1] + str(integer)[1:-1] + str(integer)[0])


"""Functional Solutions"""
def make_odds(size, start):
    """Returns a SIZE length list of odd numbers, starting with START"""
    return list([x for x in range(start, (start + size * 2)) if x % 2])


def mirror(integer):
    """ Returns the mirrored value of the input"""
    return str(integer)[-1:(-len(str(integer)) - 1):-1]


def print_string(string, factor):
    """ Prints "string" a "factor" number of times"""
    print (string + "\n") * factor


def is_palindrome(number):
    """Returns true if a number is a palindrome."""
    return str(number)[-1:(-len(str(number)) - 1):-1] == str(number)


def union(list1, list2):
    """Returns the list that contains unique values which are in both"""
    return list(filter(lambda x: x in list2, list1))


def biggest(parameter1, parameter2):
    """Returns the larger of two arguments"""
    return parameter1 if parameter1 > parameter2 else parameter2


def factorial(number):
    """ Calculates the factorial of a number."""
    return 1 if number is 1 or number is 0 else number * factorial(number - 1)


def sum_list(input_list):
    """Returns the sum of all numbers in a list."""
    return reduce(lambda x,y: x + y, input_list)
