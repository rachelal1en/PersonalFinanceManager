from expenses import ExpenseManager
from savings_calculator import SavingsCalculator
from currency_converter import CurrencyConverter
from change_calculator import ChangeCalculator
from mysql_connection import get_db_connection

def main_menu():
    print("Welcome to your Personal Finance Manager!")
    print("=" * 40)
    print("1. Track Expenses")
    print("2. View Expense Summary")
    print("3. Calculate Savings/Investments")
    print("4. View Savings History")
    print("5. Convert Currency")
    print("6. Calculate Change")
    print("7. View Change History")
    print("8. Exit")
    print("=" * 40)
    choice = input("Choose an option (1-8): ")
    return choice

def main():
    #open database connection
    db_connection = get_db_connection()

    #initialize managers and calculators
    expense_manager = ExpenseManager(db_connection)
    savings_calculator = SavingsCalculator(db_connection)
    currency_converter = CurrencyConverter()
    change_calculator = ChangeCalculator(db_connection)

    while True:
        choice = main_menu()
        if choice == "1":
            expense_manager.track_expense()
        elif choice == "2":
            expense_manager.show_summary()
        elif choice == "3":
            savings_calculator.calculate_future_value()
        elif choice == "4":
            savings_calculator.show_summary()
        elif choice == "5":
            currency_converter.convert_currency()
        elif choice == "6":
            change_calculator.calculate_change()
        elif choice == "7":
            change_calculator.show_history()
        elif choice == "8":
            print("Saving data before exiting...")
            expense_manager.save_expense_to_db()
            savings_calculator.save_savings_to_db()
            change_calculator.save_change_to_db()
            print("Thank you for using the Personal Finance Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select between 1 and 8.")


if __name__ == "__main__":
    main()
