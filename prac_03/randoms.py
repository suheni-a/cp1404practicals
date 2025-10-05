"""
CP1404 - Practical
Random number examples
"""

import random

# Run these lines multiple times to see how the output changes
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# --- Answers in comments ---

# What did you see on line 1?
# Random integer between 5 and 20 (inclusive).
# Smallest = 5, Largest = 20

# What did you see on line 2?
# Random integer from the sequence starting at 3 up to (but not including) 10, stepping by 2.
# Possible values: 3, 5, 7, 9
# Smallest = 3, Largest = 9
# Could line 2 have produced a 4? → No, because it skips even numbers (step = 2).

# What did you see on line 3?
# Random floating-point number between 2.5 and 5.5.
# Smallest possible ≈ 2.5, Largest possible ≈ 5.5

# --- Task: produce a random number between 1 and 100 inclusive ---
random_number = random.randint(1, 100)
print(random_number)
