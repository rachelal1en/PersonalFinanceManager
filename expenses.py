from utils import get_positive_float, print_header

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def track_expense(self):
        print_header("Track Expenses")
        category = input("Enter expense category (e.g., food, rent, bills): ")
        amount = get_positive_float("Enter expense amount: ")
        self.expenses.append({"category": category, "amount": amount})
        print(f"Added {amount} to {category} category.\n")
        self.show_summary()

    def show_summary(self):
        print("Expense Summary:")
        print("-" * 20)
        if not self.expenses:
            print("No expenses tracked yet.")
        else:
            total = sum(expense['amount'] for expense in self.expenses)
            for expense in self.expenses:
                print(f"{expense['category']}: {expense['amount']}")
            print(f"Total Expenses: {total}\n")

