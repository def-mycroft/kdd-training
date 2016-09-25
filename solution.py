"""Solution to HW3

Rules:

    *Can only use one line of code in each function.
    *Cannot use functions like min() or max() or any library functions.

"""

def print_string(string, factor):
    """ Prints "strint" a "factor" number of times"""
    print (string + "\n") * factor

def biggest(parameter1, parameter2):
    """Returns the larger of two arguments"""
    x = parameter1 if parameter1 > parameter2 else parameter2
    return x


def mirror(integer):
    """ Returns the mirrored value of the input"""
    for item in integer: print item
    """
    I don't know how to do this one. Something with iterating through the 
    integer. I don't know how to do that. 
    """

def manyargs(*arg):
    print "I was called with", len(arg), "arguments:", arg
    print arg[1]

manyargs(1,2,3,4,5)

#swap_last_first(integer):
#    # interchanges the first and the last digits.
#
#is_palindrome(number):
#    # returns true if a number is a palindrome.
#
#factorial(number): # calculates the factorial of a number.  

#sum_list(list): # returns the sum of all numbers in a list.
#
#
#smallest():
#    # takes an unlimited number of arguments and returns the smallest.
#
#
#union(list1, list2):
#    # takes two lists and returns the list that takes unique values from both.
#
#
#make_odds(SIZE, START):
#    # makes a list of odd numbers of size SIZE, starting with number START.  
#
#fib(n):
    # calculates the nth fibionacii number.


