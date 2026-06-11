import csv
import json
from collections import defaultdict
from datetime import datetime
import os

# ── helper: ensure CSV files exist with headers ──────────────────────────────
def init_files():
    if not os.path.exists("expenses.csv"):
        with open("expenses.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "description"])
            writer.writeheader()

    if not os.path.exists("income.csv"):
        with open("income.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["month", "primary income",
                                                    "source of secondary income",
                                                    "secondary income", "total monthly income"])
            writer.writeheader()

init_files()


# ── sub-function 1: validated date input ─────────────────────────────────────
def get_date():
    while True:                                          
        date_str = input("Enter the date (DD-MM-YYYY): ")
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str                             
        except ValueError:
            print("Invalid date format! Please use DD-MM-YYYY.")


# ── function 1: load all expenses from CSV ───────────────────────────────────
def load_expenses():
    expenses = []                                        \
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses


# ── function 2: view all expenses ────────────────────────────────────────────
def view_expenses():
    expenses = load_expenses()
    if len(expenses) == 0:
        print("No expense is recorded")
        return
    for row in expenses:
        print(row["date"] + ":\n" + row["category"] + " | ₹" +
              str(row["amount"]) + " | " + row["description"])


# ── function 3: save a new expense ───────────────────────────────────────────
def save_expenses():
    date = get_date()
    cat  = input("Enter category (Food/Transport/Stationary/Other): ")
    amt  = int(input("Enter the amount spent: "))
    des  = input("Enter description: ")

    with open("expenses.csv", "a", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writerow({"date": date, "category": cat, "amount": amt, "description": des})
    print("Expense added successfully!")


# ── function 4: total of all expenses ────────────────────────────────────────
def total_expenses():
    total = 0
    t     = 0
    expenses = load_expenses()
    for row in expenses:
        t     += 1
        total += float(row["amount"])            
    if t == 0:
        print("No expense is recorded")
        return 0
    return total


# ── function 5: amount spent per category ────────────────────────────────────
def amt_by_cat():
    expenses = load_expenses()
    if len(expenses) == 0:
        print("No expense is recorded")
        return {}
    cat_dict = {}                                
    for row in expenses:                           #   logic iterated dict keys as rows
        cat = row["category"]
        amt = float(row["amount"])
        if cat in cat_dict:
            cat_dict[cat] += amt
        else:
            cat_dict[cat]  = amt
    print("The amount spent on:")
    for cat, amt in cat_dict.items():
        print(f"  {cat}: ₹{amt:.2f}")
    return cat_dict


# ── function 6: category with highest spending ───────────────────────────────
def max_spent_cat():
    cat_dict = amt_by_cat()                        
    if not cat_dict:                              
        return
    max_cat = max(cat_dict, key=cat_dict.get)      
    print(f"The maximum amount spent on '{max_cat}' is ₹{cat_dict[max_cat]:.2f}")


# ── function 7: top 3 purchases ──────────────────────────────────────────────
def top3_purchases():
    expenses = load_expenses()
    if len(expenses) < 3:
        print("Not enough expenses recorded (need at least 3).")
        return
    print("The top 3 largest purchases are:")
    sorted_exp = sorted(expenses, key=lambda r: float(r["amount"]), reverse=True)
    for rank, row in enumerate(sorted_exp[:3], start=1):
        print(f"{rank}. ₹{int(float(row['amount']))} | {row['category']} "
              f"({row['description']}) on {row['date']}")


# ── function 8: category percentages ─────────────────────────────────────────
def cat_percentages():
    total = total_expenses()
    if total == 0:
        return
    cat_dict = amt_by_cat()
    for cat, amt in cat_dict.items():
        per = amt / total * 100
        print(f"  {cat}: {per:.1f}%")


# ── function 9: daily average spending ───────────────────────────────────────
def daily_avg():
    expenses = load_expenses()
    if not expenses:
        print("No expense is recorded")
        return
    expenses_by_date = defaultdict(float)
    for row in expenses:
        expenses_by_date[row["date"]] += float(row["amount"]) 
    total = sum(expenses_by_date.values())
    n     = len(expenses_by_date)
    print(f"Daily Average: ₹{total/n:.2f}")


# ── function 10: record income ───────────────────────────────────────────────
def input_income():
    salary   = int(input("Enter the salary/primary income: "))
    s_source = input("Enter the source of the secondary income: ")
    s_income = int(input("Enter the secondary income: "))
    month    = input("Enter the month (e.g. April-2025): ")
    income   = salary + s_income
    with open("income.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["month", "primary income",
                                                   "source of secondary income",
                                                   "secondary income", "total monthly income"])
        writer.writerow({"month": month, "primary income": salary,
                         "source of secondary income": s_source,   
                         "secondary income": s_income,
                         "total monthly income": income})
    print("Income added successfully!")


# ── function 11: view savings ─────────────────────────────────────────────────
def savings():
    totalincome = 0
    with open("income.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        t = 0
        for row in reader:
            t += 1
            totalincome += int(row["total monthly income"])  
    if t == 0:
        print("No income is recorded")
        return 0
    totalexpense  = total_expenses()
    total_savings = totalincome - totalexpense
    return total_savings


# ── function 12: create budget ───────────────────────────────────────────────
def budget_create():
    budget_dict = {}
    
    categories = ["Food", "Transport", "Stationary", "Other"]
    print("Set a budget for each category (enter 0 to skip):")
    for cat in categories:
        amt = int(input(f"  Budget for {cat}: ₹"))
        if amt > 0:
            budget_dict[cat] = amt
    while True:
        ch = int(input("Add a custom category budget? (yes-1 / no-0): "))
        if ch == 0:
            break
        cat = input("Enter the category: ")
        amt = int(input(f"Enter the budget for {cat}: ₹"))
        budget_dict[cat] = amt
    return budget_dict


# ── function 13: budget alerts ───────────────────────────────────────────────
def budget_alerts():
    budget_dict  = budget_create()
    expense_dict = amt_by_cat()
    exceeded     = {}
    for cat in budget_dict:
        if cat in expense_dict and expense_dict[cat] > budget_dict[cat]:
            exceeded[cat] = round(expense_dict[cat] - budget_dict[cat], 2)
    if exceeded:
        print("\n⚠️  WARNING! The following categories exceeded their budget:")
        print(json.dumps(exceeded, indent=4, sort_keys=True))
    else:
        print("✅ All categories are within budget!")


# ── main menu ─────────────────────────────────────────────────────────────────
while True:
    print("\n===== Personal Expense Tracker =====")
    print("1.  Add Expense")
    print("2.  View Expenses")
    print("3.  Total Expenses")
    print("4.  Amount Spent by Category")
    print("5.  Max Spent Category")
    print("6.  Top 3 Purchases")
    print("7.  Category Percentages")
    print("8.  Daily Average Spending")
    print("9.  Add Income")
    print("10. View Savings")
    print("11. Create Budget")
    print("12. Budget Alerts")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")

    if choice == "1":
        save_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print(f"Total Expenses: ₹{total_expenses():.2f}")
    elif choice == "4":
        amt_by_cat()
    elif choice == "5":
        max_spent_cat()
    elif choice == "6":
        top3_purchases()
    elif choice == "7":
        cat_percentages()
    elif choice == "8":
        daily_avg()
    elif choice == "9":
        input_income()
    elif choice == "10":
        print(f"Savings: ₹{savings():.2f}")
    elif choice == "11":
        budget_create()
    elif choice == "12":
        budget_alerts()
    elif choice == "13":
        print("Exiting... Goodbye!")
        break                                     
    else:
        print("Invalid choice. Please try again.")
