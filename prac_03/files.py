"""
CP1404 - Practical
File reading and writing exercises
"""

# 1. Write name to a file using open() and close()
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read name from file and print greeting using open() and close()
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt and add them (using with)
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    result = number1 + number2
print(result)  # Expected output: 59

# 4. Print total of all numbers in numbers.txt (using with and for loop)
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
