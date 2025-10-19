"""
CP1401 - Practical Task: Wimbledon Data
Estimate: 15 minutes
Actual:   18 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read the Wimbledon data file and display processed information."""
    records = read_wimbledon_data(FILENAME)
    champion_to_wins, countries = process_wimbledon_data(records)
    display_results(champion_to_wins, countries)


def read_wimbledon_data(filename):
    """Read data from the Wimbledon CSV file and return a list of records (lists)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        records = [line.strip().split(",") for line in in_file]
    return records


def process_wimbledon_data(records):
    """
    Process the data to count wins per champion and collect unique countries.
    Returns:
        champion_to_wins (dict): {champion_name: number_of_wins}
        countries (set): unique set of countries
    """
    champion_to_wins = {}
    countries = set()

    for record in records:
        country = record[1]
        champion = record[2]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1

    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display the champions and their win counts, and the countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
