"""
CP1404
"""

import random


def main():
    score = get_valid_score()
    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print("*" * int(score))  # show stars = number of score
        elif choice == "Q":
            print("Farewell :)")
        else:
            print("Invalid choice")

    random_score = random.randint(0, 100)
    print(f"\nRandom score: {random_score}")
    print(determine_result(random_score))


def print_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score (0–100 inclusive)."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """Return the result string based on score (SRP: no printing)."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Run the program
if __name__ == "__main__":
    main()
