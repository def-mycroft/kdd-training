"""Solution to HW3"""

def smallest():
    """takes an unlimited number of arguments and returns the smallest."""
    # TODO I don't know how to do this one.
    # I still don't know how to do this one.
    return output


def make_odds(size, start):
    # TODO I still don't have this one down.
    # The problem with the below solution is that it does not create the 
    # correct quantity of the odd numbers, it stops at the start plus 
    # the end.
    """Returns a SIZE length list of odd numbers, starting with START"""
    return list([x for x in range(start, 2 * (start + size + 1)) if x % 2])


def swap_last_first(integer):
    """ Interchanges the first and last digits"""
    # TODO I don't have a solution here.
    # should be able to use slice methods on this one. 
    return output


"""Functional Solutions"""
###############################################################################

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
    return reduce(lambda x,y: x*y, range(1,(number+1)))


def sum_list(input_list):
    """Returns the sum of all numbers in a list."""
    return reduce(lambda x,y: x + y, input_list)


