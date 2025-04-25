from expenses import ExpenseManager
from savings_calculator import SavingsCalculator
from currency_converter import CurrencyConverter
from change_calculator import ChangeCalculator

def main_menu():
    print("Welcome to your Personal Finance Manager!")
    print("=" * 40)
    print("1. Track Expenses")
    print("2. Calculate Savings/Investments")
    print("3. Convert Currency")
    print("4. Calculate Change")
    print("5. Exit")
    print("=" * 40)
    choice = input("Choose an option (1-5): ")
    return choice

def main():
    expense_manager = ExpenseManager()
    savings_calculator = SavingsCalculator()
    currency_converter = CurrencyConverter()
    change_calculator = ChangeCalculator()

    while True:
        choice = main_menu()
        if choice == "1":
            expense_manager.track_expense()
        elif choice == "2":
            savings_calculator.calculate_future_value()
        elif choice == "3":
            currency_converter.convert_currency()
        elif choice == "4":
            change_calculator.calculate_change()
        elif choice == "5":
            print("Thank you for using the Personal Finance Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select between 1 and 5.")


if __name__ == "__main__":
    main()

