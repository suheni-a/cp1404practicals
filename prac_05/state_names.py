"""
CP1404 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all state codes and names neatly
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Ask user for short state name
state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
