from utils import format_currency, print_header, save_to_db, load_from_db

class SavingsCalculator:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.savings_history = []
        self.load_savings()

    def load_savings(self):
        # Fetch all savings data from the database into memory
        rows = load_from_db(self.db_connection, "savings",
                                columns="principal, monthly_contribution, annual_rate, years, future_value")
        self.savings_history = [
            {"principal": principal, "monthly_contribution": monthly_contribution,
            "annual_rate": annual_rate, "years": years, "future_value": future_value}
            for principal, monthly_contribution, annual_rate, years, future_value in rows
        ]

    def calculate_future_value(self):
        print_header("Savings Calculator")
        principal = float(input("Enter initial savings: "))
        monthly_contribution = float(input("Enter monthly contribution: "))
        annual_rate = float(input("Enter annual interest rate (in %): ")) / 100
        years = int(input("Enter number of years: "))

        # Calculating future value
        months = years * 12
        monthly_rate = annual_rate / 12
        future_value = principal * (1 + monthly_rate) ** months
        for i in range(1, months + 1):
            future_value += monthly_contribution * (1 + monthly_rate) ** (months - i)

        print(f"Your savings will grow to: {format_currency(future_value)} in {years} years.\n")

        # Save to database
        self.save_savings_to_db(principal, monthly_contribution, annual_rate, years, future_value)

    def save_savings_to_db(self, principal, monthly_contribution, annual_rate, years, future_value):
        data = {
            "principal": principal,
            "monthly_contribution": monthly_contribution,
            "annual_rate": annual_rate,
            "years": years,
            "future_value": future_value
        }
        save_to_db(self.db_connection, "savings", data)


    def show_summary(self):
        """
        Display historical data saved in the 'savings' table.
        """
        print_header("Savings History:")
        rows = load_from_db(self.db_connection, "savings",
                            columns="principal, monthly_contribution, annual_rate, years, future_value")

        if not rows:
            print("No savings data found.")
        else:
            print(
                f"{'Principal':<12}{'Monthly Contribution':<22}{'Annual Rate (%)':<15}{'Years':<7}{'Future Value':<15}")
            print("-" * 80)
            for row in rows:
                principal, monthly_contribution, annual_rate, years, future_value = row
                print(
                    f"{format_currency(principal):<12}{format_currency(monthly_contribution):<22}{annual_rate * 100:<15.1f}{years:<7}{format_currency(future_value):<15}")
        print("\n")
