#Project 1: Expense Tracker
#Author: [Selim Reza]
import csv
import os

expenses = []
monthly_budget = 0.0
filename = "expenses.csv"

#load expenses
def load_expenses():
    global expenses
    if os.path.exists(filename):
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
        print(f"Loaded {len(expenses)} expense(s) from {filename}.")

#save expenses
def save_expenses():
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Saved {len(expenses)} expense(s) to {filename}.")

#add expenses
def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (e.g. Food, Travel): ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    })
    print("Expense added.")

#view expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for e in expenses:
        if not all(k in e and e[k] for k in ["date", "category", "amount", "description"]):
            print("[Incomplete entry skipped]")
            continue
        print(f"  {e['date']}  |  {e['category']:<14}  |  ${float(e['amount']):>8.2f}  |  {e['description']}")

#track xpenses
def track_budget():
    global monthly_budget
    if monthly_budget == 0:
        monthly_budget = float(input("Enter your monthly budget: "))
    total = sum(e["amount"] for e in expenses)
    remaining = monthly_budget - total
    print(f"Total spent: ${total:.2f} / ${monthly_budget:.2f}")
    if remaining < 0:
        print(f"You have exceeded your budget by ${abs(remaining):.2f}!")
    else:
        print(f"You have ${remaining:.2f} left for the month.")

#load main menu
def menu():
    load_expenses()
    while True:
        print("\n--- Expense Tracker for Unit 1 Project ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            track_budget()
        elif choice == "4":
            save_expenses()
        elif choice == "5":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    menu()