from expense import Expense

expense_1 = Expense(1, 125, "bill", "phone bill", "07-27-26")
expense_2 = Expense(2, 50, "food", "chipotle", "12-25-2026")

expenses = []

expenses.append(expense_1)
expenses.append(expense_2)

for expense in expenses:
    print(expense)
