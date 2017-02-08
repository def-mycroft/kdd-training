""" Displays all of the modules in this HW. 
Note that the speech parser uses a file called "punctuation.txt" in order to
strip punctuation marks from the input speech file.
"""
from __future__ import print_function
from hw4 import guessing_game
from hw4 import more_functions
from hw4 import speech_parser


def display_results():
    """ Display results of parsing "musk_article.txt" text file."""
    print("parse_text:\n")
    speech_parser.parse_text('musk_article.txt')
    print("\n")

    """ Display of functions from more_functions"""
    list1 = list(range(10,21))
    list2 = list(range(1,10))
    dict1 = more_functions.make_dict(list1)
    dict2 = more_functions.make_dict(list2)

    """ Display odd_even_merge"""
    print("odd_even_merge:\n")
    print(more_functions.odd_even_merge(list1, list2))
    print("\n")

    """ Display Transpose Matrix function """
    print("odd_even_merge:\n")
    print(more_functions.transpose_matrix(list1, list2))
    print("\n")

    """Display make_dict function"""
    print("make_dict:\n")
    print(dict1) # Generated from make_dict function called above.
    print("\n")

    """ Display merge_dict functions"""
    print("merge_dicts:\n")
    print(more_functions.merge_dicts(dict1, dict2))
    print("\n")

    """ Display squares function """
    start = 1; qty = 10
    print("squares qty=%s start=%s:\n" % (qty, start))
    print(more_functions.squares(start, qty))
    print("\n")

    """ Displays guessing game"""
    guessing_game.play_game(1,20)
