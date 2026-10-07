"""
Expense Tracker

A command-line program for recording and reviewing personal expenses.

Features:
    1. Add an expense (amount, category, description)
    2. View all expenses
    3. Show total spending
    4. Show spending per category
    5. Search expenses by category or description
    6. Exit

Each expense is stored as a dictionary:
    {"amount": 12.5, "category": "food", "description": "lunch at work"}

All expenses are kept in a list while the program runs.
Note: data is lost when the program exits (saving to a file comes later).

Run with:
    python3 main.py
"""

expenses = []


def add_expense(expenses):
    """
    Ask the user for a new expense and add it to the list.

    Validation:
        - amount must be a number greater than 0
        - category cannot be empty and is stored in lowercase
        - description is optional

    Args:
        expenses (list): The list of expense dictionaries to add to.
    """
    # Keep asking until the amount is a valid positive number.
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid amount. Enter a number.")

    # Keep asking until the category is not empty.
    # Lowercase + strip so "Food", "food " and "FOOD" are the same category.
    while True:
        category = input("Category: ").lower().strip()
        if not category:
            print("Category can't be empty.")
        else:
            break

    description = input("Description: ")

    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)

    print("Expense added.")


def print_expense(number, expense):
    """
    Print a single expense on one line.

    Example output:
        1. 12.50 | food | lunch at work

    Args:
        number (int): The expense's position in the full list (starting at 1).
        expense (dict): The expense to print.
    """
    print(
        f"{number}. {expense['amount']:.2f} | {expense['category']} | {expense['description']}"
    )


def view_expenses(expenses):
    """
    Print every expense, numbered from 1.

    Args:
        expenses (list): The list of expense dictionaries.
    """
    if not expenses:
        print("No expenses yet.")
    else:
        for number, expense in enumerate(expenses, start=1):
            print_expense(number, expense)


def total_spending(expenses):
    """
    Print the sum of all expense amounts.

    Prints "Total: 0.00" when there are no expenses.

    Args:
        expenses (list): The list of expense dictionaries.
    """
    total = 0

    # Accumulator pattern: start at 0 and add each amount.
    for expense in expenses:
        total += expense["amount"]

    print(f"Total: {total:.2f}")


def category_summary(expenses):
    """
    Print the total amount spent in each category.

    Example output:
        food: 20.50
        transport: 45.00

    Args:
        expenses (list): The list of expense dictionaries.
    """
    # Guard clause: nothing to summarise, so stop early.
    if not expenses:
        print("No expenses yet.")
        return

    # Map each category name to its running total.
    totals = {}
    for expense in expenses:
        if expense["category"] in totals:
            totals[expense["category"]] += expense["amount"]
        else:
            totals[expense["category"]] = expense["amount"]

    for name, value in totals.items():
        print(f"{name}: {value:.2f}")


def search_expenses(expenses):
    """
    Ask for a search term and print every expense whose category
    or description contains it. The search is case-insensitive.

    Matches keep their original numbers from the full list.

    Args:
        expenses (list): The list of expense dictionaries.
    """
    search = input("Search: ").lower().strip()

    # Flag: remembers whether at least one match was found in the loop.
    found = False

    for number, expense in enumerate(expenses, start=1):
        if search in expense["category"] or search in expense["description"].lower():
            print_expense(number, expense)
            found = True

    if not found:
        print("No matching expenses.")


# Main menu: runs until the user chooses 6 (Exit).
while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spending")
    print("4. Category summary")
    print("5. Search expenses")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        total_spending(expenses)
    elif choice == "4":
        category_summary(expenses)
    elif choice == "5":
        search_expenses(expenses)
    elif choice == "6":
        print("Goodbye.")
        break
    else:
        print("Invalid choice")
