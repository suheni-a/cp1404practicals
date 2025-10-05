"""
CP1404 - Practical
Exceptions to complete
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # prevent ZeroDivisionError by checking before dividing
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")