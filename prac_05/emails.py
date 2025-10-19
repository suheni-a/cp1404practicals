"""
Emails
Estimate: 25 minutes
Actual:   23 minutes
"""

def extract_name(email):
    """Extract a name from an email address."""
    # Split before @ symbol, replace dots with spaces, and title-case the result
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    name = ' '.join(parts).title()
    return name


def main():
    """Store emails and names in a dictionary, then print them."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        # Guess name from email
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    # Print all stored names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
