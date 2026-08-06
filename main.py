from expense import Expense

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

    for expense in expenses:
        print(expense)


# Function to add expenses
def add_expenses(expenses):
    print("\nAdd Expense\n")

    next_id = len(expenses) + 1
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    date = input("Date: ")

    new_expense = Expense(next_id, amount, category, description, date)
    expenses.append(new_expense)
    print("Expense added successfully!")


# Function to delete expenses
def delete_expense(expenses):
    print("\nDelete Expense\n")
    expense_id = int(input("Enter Expense ID: "))

    # for each expense
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
        add_expenses(expenses)
    elif user_choice == "3":
        delete_expense(expenses)
    elif user_choice == "4":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid option. Please try again.\n")
