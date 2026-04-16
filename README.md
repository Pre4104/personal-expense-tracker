# Personal Expense Tracker

A command-line application built with **Python** to track daily expenses, manage income, set budgets, and calculate savings — all stored locally using CSV files.

---

## Features

- Add and view expenses with date, category, amount, and description
- Calculate total expenses and category-wise breakdown
- Find the highest-spending category
- View top 3 largest purchases
- See percentage share of each spending category
- Calculate daily average spending
- Record monthly income (primary + secondary)
- Calculate savings (income minus expenses)
- Create custom category budgets
- Get alerts when spending exceeds budget

---

## Project Structure

```
personal-expense-tracker/
├── personal_expense_tracker.py   ← main program
├── expenses.csv                  ← auto-created on first run
├── income.csv                    ← auto-created on first run
└── README.md
```

> `expenses.csv` and `income.csv` are created automatically when you run the program for the first time. You do not need to create them manually.

---

## How to Run

### Requirements
- Python 3.x (no external libraries needed — uses only built-in modules)

### Steps

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/personal-expense-tracker.git

# Navigate into the folder
cd personal-expense-tracker

# Run the program
python personal_expense_tracker.py
```

---

## Menu Options

| Option | Function |
|--------|----------|
| 1 | Add a new expense |
| 2 | View all recorded expenses |
| 3 | View total expenses |
| 4 | View amount spent per category |
| 5 | View the category with maximum spending |
| 6 | View top 3 largest purchases |
| 7 | View percentage breakdown by category |
| 8 | View daily average spending |
| 9 | Add monthly income |
| 10 | View total savings |
| 11 | Create a category-wise budget |
| 12 | Get alerts for over-budget categories |
| 13 | Exit |

---

## Expense Categories

- Food
- Transport
- Stationary
- Other
- Custom categories (you can add your own via the budget menu)

---

## Data Storage

All data is stored locally in CSV files:

- `expenses.csv` — stores every expense entry (date, category, amount, description)
- `income.csv` — stores monthly income records (primary income, secondary income source and amount, total)

---

## Technologies Used

- **Language:** Python 3.x
- **Libraries:** `csv`, `json`, `collections`, `datetime`, `os` (all built-in)

---

## Author

**B S Lakshmi Prerana**  

---

## Disclaimer

This project is created for educational purposes. All data is stored locally on your machine and is not shared anywhere.
