"""Solution to HW3"""

list = [x for x in range(21)]
print list[10]

def smallest():
    """takes an unlimited number of arguments and returns the smallest."""
    # I still don't know how to do this one.
    return output


def make_odds(SIZE, START):
    """Makes a SIZE length list of odd numbers, starting with START"""
    # This one doesn't quite work correctly.
    # need to just create a different list in the filter function, 
    output = list(filter(lambda x: x % 2 != 0, range(START, 100000)))
    return range(output[0], output[SIZE + 1])


def is_palindrome(number):
    """Returns true if a number is a palindrome."""
    # Should be able to use slices to compare two things.
    return bool_is_palindrome


def swap_last_first(integer):
    """ Interchanges the first and last digits"""
    # should be able to use slice methods on this one. 
    return output


def mirror(integer):
    """ Returns the mirrored value of the input"""
    # this is just a slice method as well. 
    return mirrored


"""Functional Solutions"""
###############################################################################

def print_string(string, factor):
    """ Prints "string" a "factor" number of times"""
    print (string + "\n") * factor


def union(list1, list2):
    """Returns the list that contains unique values which are in both"""
    output = list(filter(lambda x: x in list2, list1))
    return output


def biggest(parameter1, parameter2):
    """Returns the larger of two arguments"""
    x = parameter1 if parameter1 > parameter2 else parameter2
    return x


def factorial(number):
    """ Calculates the factorial of a number."""
    return reduce(lambda x,y: x*y, range(1,(number+1)))


def sum_list(input_list):
    """Returns the sum of all numbers in a list."""
    output = reduce(lambda x,y: x + y, input_list)
    return output


