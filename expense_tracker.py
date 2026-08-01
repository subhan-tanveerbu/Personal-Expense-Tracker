"""
==========================================
Personal Expense Tracker
Week 1 Mini Project
Author: Subhan Tanveer
==========================================
"""

import csv
import os

FILE_NAME = "expenses.csv"


# -----------------------------
# File Setup
# -----------------------------
def initialize_file():
    """Create CSV file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# -----------------------------
# Add Expense
# -----------------------------
def add_expense():
    """Add a new expense."""

    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense Added Successfully!\n")


# -----------------------------
# View Expenses
# -----------------------------
def view_expenses():
    """Display all expenses."""

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n========== Expenses ==========")

        total = 0

        for row in reader:
            print(
                f"Date: {row[0]} | "
                f"Category: {row[1]} | "
                f"Description: {row[2]} | "
                f"Amount: Rs {row[3]}"
            )

            total += float(row[3])

        print("------------------------------")
        print(f"Total Expense: Rs {total:.2f}")
        print()


# -----------------------------
# Search Expense
# -----------------------------
def search_expense():
    """Search expense by category."""

    keyword = input("Enter Category to Search: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nSearch Results\n")

        for row in reader:
            if row["Category"].lower() == keyword:
                print(row)
                found = True

    if not found:
        print("No Expense Found.\n")


# -----------------------------
# Expense Summary
# -----------------------------
def expense_summary():
    """Display category-wise summary."""

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    print("\n===== Expense Summary =====")

    for category, amount in summary.items():
        print(f"{category:<15} Rs {amount:.2f}")

    print()


# -----------------------------
# Highest Expense
# -----------------------------
def highest_expense():
    """Display highest single expense."""

    expenses = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    if not expenses:
        print("No expenses available.\n")
        return

    highest = max(expenses, key=lambda x: float(x["Amount"]))

    print("\nHighest Expense")
    print("----------------------")
    print(f"Date: {highest['Date']}")
    print(f"Category: {highest['Category']}")
    print(f"Description: {highest['Description']}")
    print(f"Amount: Rs {highest['Amount']}\n")


# -----------------------------
# Export Summary
# -----------------------------
def export_summary():
    """Export summary to text file."""

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    with open("summary.txt", "w") as file:
        file.write("Expense Summary\n")
        file.write("=====================\n")

        for category, amount in summary.items():
            file.write(f"{category}: Rs {amount:.2f}\n")

    print("Summary exported to summary.txt\n")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    """Main program."""

    initialize_file()

    while True:

        print("========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Expense Summary")
        print("5. Highest Expense")
        print("6. Export Summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            expense_summary()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            export_summary()

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid Choice!\n")


if __name__ == "__main__":
    main()