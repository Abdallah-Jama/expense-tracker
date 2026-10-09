# Expense Tracker

A command-line expense tracker written in Python. Add your expenses, view them, see your total and per-category spending, and search by keyword, all from the terminal.

## Features

- **Add expense**: record an amount, a category and an optional description
- **View expenses**: list every expense, numbered, with amounts to 2 decimal places
- **Total spending**: the sum of all expenses
- **Category summary**: total spent in each category
- **Search expenses**: find expenses by category or description (case-insensitive)
- **Input validation**: invalid amounts, zero or negative values and empty categories are rejected without crashing
- **Saved data**: expenses are stored in expenses.json and reloaded on startup”
- **Limitations**: remove the line about losing data. If nothing is left in that section, delete the whole section.
- **Planned improvements:**: remove “Save and load expenses with JSON”
## Requirements

- Python 3

No external libraries are needed.

## How to run

```
git clone https://github.com/Abdallah-Jama/expense-tracker.git
cd expense-tracker
python3 main.py
```

## Example

```
1. Add expense
2. View expenses
3. Total spending
4. Category summary
5. Search expenses
6. Exit
Choose: 1
Amount: 12.50
Category: Food
Description: lunch at work
Expense added.

Choose: 2
1. 12.50 | food | lunch at work
2. 30.00 | transport | taxi to work

Choose: 4
food: 12.50
transport: 30.00

Choose: 5
Search: work
1. 12.50 | food | lunch at work
2. 30.00 | transport | taxi to work
```

## How it works

- Each expense is stored as a dictionary:
  ```python
  {"amount": 12.5, "category": "food", "description": "lunch at work"}
  ```
- All expenses are kept in a list while the program runs.
- Categories are stored in lowercase, so `Food`, `food ` and `FOOD` count as the same category.
- Each menu option is handled by its own function, and a shared `print_expense` helper keeps the output format in one place.

## Limitations

- Expenses are stored in memory only, so they are lost when the program exits.

## Planned improvements

- Save and load expenses with a JSON file
- Edit and delete expenses
- Add dates to expenses and filter by month
- Unit tests
