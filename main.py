from expense import Expense
from datetime import datetime

# Sample Data
expense_1 = Expense(1, 125, "bill", "phone bill", "07-27-26")
expense_2 = Expense(2, 50, "food", "chipotle", "12-25-2026")

# Expense list with sample data
expenses = []
expenses.append(expense_1)
expenses.append(expense_2)


# Function to display menu
def display_menu():
    print("\n===== Expense Tracker =====\n")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Quit")


# Function to view expenses
def view_expenses(expenses):
    print("\nView Expenses\n")

    if not expenses:
        print("No expenses found. Add an expense first.")
        return

    for expense in expenses:
        print(expense)


# Function to add expenses
def add_expense(expenses):
    print("\nAdd Expense\n")

    largest_id = 0
    for expense in expenses:
        if expense.expense_id > largest_id:
            largest_id = expense.expense_id

    next_id = largest_id + 1

    while True:
        category = input("Category: ").strip()
        if not category:
            print("Invalid input. Please enter a valid Category: ")
        else:
            break

    while True:
        description = input("Description: ").strip()
        if not description:
            print("Invalid input. Please enter a valid Description: ")
        else:
            break

    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Invalid amount. Please enter an amount > 0: ")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        date = input("Date: ").strip()
        if not date:
            date = datetime.now().strftime("%m-%d-%Y")
            break
        try:
            datetime.strptime(date, "%m-%d-%Y")
            break
        except ValueError:
            print("Invalid date. Please use MM-DD-YYYY.")

    new_expense = Expense(next_id, amount, category, description, date)
    expenses.append(new_expense)
    print("Expense added successfully!")


# Function to delete expenses
def delete_expense(expenses):
    print("\nDelete Expense\n")

    while True:
        try:
            expense_id = int(input("Enter Expense ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid ID: ")
    # for each expense in expenses list
    for expense in expenses:
        # if the ID matches
        if expense.expense_id == expense_id:
            # remove it and stop searching
            expenses.remove(expense)
            print("\nExpense removed successfully!")
            print(expense)
            break
    # otherwise, if loop finished without stopping
    else:
        # report it wasnt found
        print(f"\nExpense with ID '{expense_id}' not found.")


# Main program
while True:
    display_menu()

    user_choice = input("\nChoose an option: ")

    if user_choice == "1":
        view_expenses(expenses)
    elif user_choice == "2":
        add_expense(expenses)
    elif user_choice == "3":
        delete_expense(expenses)
    elif user_choice == "4":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid option. Please try again.\n")
