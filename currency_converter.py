from utils import print_header


class CurrencyConverter:
    def __init__(self):
        self.rates = {"EUR": 0.94, "GBP": 0.83, "JPY": 146.53, "CAD": 1.34, "RUB": 97.17}

    def show_rates(self):
        print("Current Exchange Rates (per USD):")
        for currency, rate in self.rates.items():
            print(f"1 USD = {rate} {currency}")

    def convert_currency(self):
        print_header("Currency Converter")
        self.show_rates()
        currency = input("Enter currency code (e.g., EUR, GBP, JPY): ").upper()
        if currency in self.rates:
            from utils import get_positive_float
            amount = get_positive_float(f"Enter amount in USD to convert to {currency}: ")
            converted = amount * self.rates[currency]
            print(f"{amount} USD = {converted:,.2f} {currency}\n")
        else:
            print("Unknown currency code. Please try again.\n")
