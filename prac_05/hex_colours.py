"""
Colour Lookup Program
Estimate: 15 minutes
Actual:   17 minutes
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlueViolet": "#8a2be2",
    "Brown": "#a52a2a",
    "CadetBlue": "#5f9ea0"
}

# Print all available colours
print("Available colours:")
for colour in COLOUR_TO_HEX:
    print(f"  {colour:15} → {COLOUR_TO_HEX[colour]}")

# Ask user for colour names
colour_name = input("\nEnter a colour name: ").title()

while colour_name != "":
    try:
        print(f"{colour_name} code is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").title()



