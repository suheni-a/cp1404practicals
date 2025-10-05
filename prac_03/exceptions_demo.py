"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When you enter something that is not an integer (e.g., a letter or symbol instead of a number).

2. When will a ZeroDivisionError occur?
   When you enter 0 as the denominator, since division by zero is not allowed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, by using a loop to keep asking for the denominator until it’s not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")