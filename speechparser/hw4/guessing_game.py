""" Guessing Game - works as shown below."""
from __future__ import print_function
import random

def play_game(low, high):
    """The guessing game"""
    mystery_number = random.randrange(low, (high + 1))
    user_guess = 0

    print("Welcome to the mystery number game!")
    user_guess = int(raw_input(" Guess >>"))

    while user_guess != mystery_number:
        if user_guess > mystery_number:
            print("The mystery number is smaller.")
            user_guess = int(raw_input(" Guess >>"))
        if user_guess < mystery_number:
            print("The mystery number is larger.")
            user_guess = int(raw_input(" Guess >>"))
        if user_guess == mystery_number:
            print("Correct!! You won!!")
