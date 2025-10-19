"""
CP1404 Practical
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate user-specified number of quick picks."""
    number_of_picks = int(input("How many quick picks? "))

    # Create a list to store all generated quick picks
    quick_picks = [generate_quick_pick() for _ in range(number_of_picks)]

    # Use the display function to print them nicely
    display_quick_picks(quick_picks)


def generate_quick_pick():
    """Generate a single quick pick of 6 unique random numbers between 1 and 45."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def display_quick_picks(picks):
    """Display all quick picks neatly formatted."""
    for pick in picks:
        print(" ".join(f"{number:2}" for number in pick))


main()
