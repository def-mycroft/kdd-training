"""Solution to HW3"""

def print_string(string, factor):
    """ Prints "string" a "factor" number of times"""
    print (string + "\n") * factor


def biggest(parameter1, parameter2):
    """Returns the larger of two arguments"""
    x = parameter1 if parameter1 > parameter2 else parameter2
    return x


def mirror(integer):
    """ Returns the mirrored value of the input"""
    return mirrored



#swap_last_first(integer):
#    # interchanges the first and the last digits.
#
#is_palindrome(number):
#    # returns true if a number is a palindrome.
#

def factorial(number):
    """ Calculates the factorial of a number."""
    output = reduce(lambda x,y: x*y, range(1,(number+1)))
    return output


def sum_list(input_list):
    """Returns the sum of all numbers in a list."""
    output = reduce(lambda x,y: x + y, input_list)
    return output


def smallest():
    """takes an unlimited number of arguments and returns the smallest."""
    return output


def union(list1, list2):
    """Returns the list that contains unique values which are in both"""
    output = list(filter(lambda x: x in list2, list1))
    return output


def make_odds(SIZE, START):
    """Makes a SIZE length list of odd numbers, starting with START"""
    output = list(filter(lambda x: x % 2 != 0, range(START, 100000)))
    return range(output[0], output[SIZE + 1])


while True:
    size = int(raw_input("size>>"))
    start = int(raw_input("start>>"))
    print(make_odds(size, start))

#fib(n):
    # calculates the nth fibionacii number.


