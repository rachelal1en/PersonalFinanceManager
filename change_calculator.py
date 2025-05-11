from utils import get_positive_int, format_currency, print_header, save_to_db, load_from_db

class ChangeCalculator:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.change_history = []
        self.load_change_amount()
        self.cummulative_change = 0 # total change: historical + runtime


    def load_change_amount(self):
        rows = load_from_db(self.db_connection, "change", columns="half_dollars, quarters, dimes, nickels, pennies, total_cents")
        self.change_history = [
            {"half_dollars": half_dollars, "quarters": quarters, "dimes": dimes,
             "nickels": nickels, "pennies": pennies, "total_cents": total_cents}
            for half_dollars, quarters, dimes, nickels, pennies, total_cents in rows
        ]
        self.cumulative_change = sum(
            change['total_cents'] for change in self.change_history
        )


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
            self.cumulative_change += total_cents  # Update cumulative total

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

            # Save to database
            self.save_change_to_db(half_dollars, quarters, dimes, nickels, pennies, total_cents)

            # Prompt to add more change or exit
            user_choice = input("Do you have more change to calculate? (y/n): ").strip().lower()
            if user_choice == "n":
                break
            elif user_choice != "y":
                print("Invalid choice. Please enter 'y' or 'n'.")

        # Final Summary
        print("\nThanks for using the Change Calculator!")
        overall_dollars = self.cumulative_change // 100
        overall_cents = self.cumulative_change % 100
        print(f"You entered a total of {self.cumulative_change} cents across all calculations.")
        print(
            f"Which is: {overall_dollars} dollars and {overall_cents} cents ({format_currency(overall_dollars + overall_cents / 100)})\n")

    def save_change_to_db(self, half_dollars, quarters, dimes, nickels, pennies, total_cents):
        data = {
                "half_dollars": half_dollars,
                "quarters": quarters,
                "dimes": dimes,
                "nickels": nickels,
                "pennies": pennies,
                "total_cents": total_cents
            }
        save_to_db(self.db_connection, "change", data)


    def show_history(self):
        """
        Display historical data saved in the 'change' table.
        """
        print_header("Change History:")
        rows = load_from_db(self.db_connection, "change",
                            columns="half_dollars, quarters, dimes, nickels, pennies, total_cents")

        if not rows:
            print("No change data found.")
        else:
            print(
                f"{'Half-Dollars':<13}{'Quarters':<10}{'Dimes':<7}{'Nickels':<8}{'Pennies':<8}{'Total Change (cents)':<20}")
            print("-" * 70)
            for row in rows:
                half_dollars, quarters, dimes, nickels, pennies, total_cents = row
                print(f"{half_dollars:<13}{quarters:<10}{dimes:<7}{nickels:<8}{pennies:<8}{total_cents:<20}")
        print("\n")


