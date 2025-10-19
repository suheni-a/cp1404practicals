"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

# Ask the user for a string of text
text = input("Text: ")

# Split the text into words
words = text.split()

# Create an empty dictionary to count occurrences
word_to_count = {}

# Count how many times each word appears
for word in words:
    # Convert to lowercase to count words case-insensitively
    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Find the length of the longest word for alignment
max_length = max(len(word) for word in word_to_count)

# Print results in alphabetical order, aligned neatly
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
