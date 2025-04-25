from utils import get_positive_int, format_currency, print_header

class ChangeCalculator:
    def __init__(self):
        self.overall_change = 0  # Running total of all change entered.

    def calculate_change(self):
        print_header("Change Calculator")

        # Loop for entering multiple sets of change
        while True:
            # Prompt user for each coin type, using input validation from utils
            half_dollars = get_positive_int("How many half-dollars? ")
            quarters = get_positive_int("How many quarters? ")
            dimes = get_positive_int("How many dimes? ")
            nickels = get_positive_int("How many nickels? ")
            pennies = get_positive_int("How many pennies? ")

            # Calculate total change in cents
            total_cents = (half_dollars * 50) + (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
            self.overall_change += total_cents

            # Calculate dollars and cents
            total_dollars = total_cents // 100
            remaining_cents = total_cents % 100

            # Print results
            print("\nYou entered:")
            print(f"  Half-dollars: {half_dollars}")
            print(f"  Quarters: {quarters}")
            print(f"  Dimes: {dimes}")
            print(f"  Nickels: {nickels}")
            print(f"  Pennies: {pennies}")
            print(f"  Total change: {total_cents} cents")
            print(
                f"  Which is: {total_dollars} dollars and {remaining_cents} cents ({format_currency(total_dollars + remaining_cents / 100)})\n")

            # Prompt to add more change or exit
            while True:
                user_choice = input("Do you have more change to calculate? (y/n): ").strip().lower()
                if user_choice == "n":
                    break
                elif user_choice != "y":
                    print("Invalid choice. Please enter 'y' or 'n'.")

        # Final Summary
        print("\nThanks for using the Change Calculator!")
        overall_dollars = self.overall_change // 100
        overall_cents = self.overall_change % 100
        print(f"You entered a total of {self.overall_change} cents across all calculations.")
        print(
            f"Which is: {overall_dollars} dollars and {overall_cents} cents ({format_currency(overall_dollars + overall_cents / 100)})\n")
