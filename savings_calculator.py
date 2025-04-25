from utils import format_currency, print_header

class SavingsCalculator:
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

