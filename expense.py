# Create a class Expense:


class Expense:

    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"[{self.expense_id}] {self.category.title()} | {self.description.title()} | ${self.amount:.2f} | {self.date}"
