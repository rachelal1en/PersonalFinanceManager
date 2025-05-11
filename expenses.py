from unicodedata import category

from utils import get_positive_float, print_header, save_to_db, load_from_db

class ExpenseManager:
    def __init__(self, db_connection):
        # call database connection
        self.db_connection = db_connection
        self.expenses = []
        self.load_expenses() #load at startup

    def load_expenses(self):
        #fetch all expenses from the database into memory
        rows = load_from_db(self.db_connection, "expenses")
        # Safely parse and extract only 'category' and 'amount', ignoring extra fields
        self.expenses = []
        for row in rows:
            if isinstance(row, dict):
                # Expecting a dictionary (e.g., {"category": ..., "amount": ...})
                category = row.get("category")
                amount = row.get("amount")
            elif isinstance(row, (list, tuple)) and len(row) >= 2:
                # Expecting a tuple or list (e.g., (category, amount, ...))
                category, amount = row[0], row[1]
            else:
                # Skipping invalid row formats
                continue

            # Only add the row if both fields are valid
            if category is not None and amount is not None:
                self.expenses.append({"category": category, "amount": amount})


    def track_expense(self):
        print_header("Track Expenses")
        # Collect expenses from the user
        category = input("Enter expense category (e.g., food, rent, bills): ")
        amount = get_positive_float("Enter expense amount: ")
        # Append to local list
        self.expenses.append({"category": category, "amount": amount})

        # Save expense to the database
        self.save_expense_to_db(category, amount)
        print(f"Added {amount} to {category} category.\n")

        # Display summary
        self.show_summary()

    def save_expense_to_db(self, category, amount):
        # Validate category is a string
        if not isinstance(category, str):
            print(f"Invalid category: {category}. Expense not saved.")
            return

        # Validate amount is numeric and positive
        try:
            amount = float(amount)
            if amount <= 0:
                print(f"Invalid amount: {amount}. Expense not saved.")
                return
        except ValueError:
            print(f"Invalid amount: {amount}. Expense not saved.")
            return

        # Save expense using the utility function
        data = {"category": category, "amount": amount}
        save_to_db(self.db_connection, "expenses", data)


    def show_summary(self):
        # Display expenses using the utility function
        rows = load_from_db(self.db_connection, "expenses")

        print("DEBUG: Rows retrieved from database ->", rows)

        print_header("Expense Summary:")
        if not rows:
            print("No expenses tracked yet.")
        else:
            total = 0
            for row in rows:
                # Ensure only category and amount are extracted
                category = row["category"] if isinstance(row, dict) else row[0]
                amount = row["amount"] if isinstance(row, dict) else row[1]
                try:
                    amount = float(amount)
                except ValueError:
                    print(f"Skipping invalid amount value: {amount}")
                    continue

                print(f"{category}: {amount}")
                total += amount
            print(f"Total Expenses: {total}\n")
