"""
CP1404 Practical
Program to calculate and display cumulative total income.
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))  #renamed from 'months' to 'number_of_months'

    #use f-string for input
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)  #call the new function


def print_income_report(incomes):
    """Print income report showing monthly and cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${total:10.2f}")


main()
