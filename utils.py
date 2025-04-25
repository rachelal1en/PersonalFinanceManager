def get_positive_float(prompt):
    """
    Prompt the user for a positive float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value must be positive! Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_positive_int(prompt):
    """
    Prompt the user for a positive integer value.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value must be a non-negative integer! Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def format_currency(value):
    """
    Format a float or integer as a currency (e.g., $1,234.56).
    """
    return f"${value:,.2f}"

def print_header(title):
    print("\n" + title)
    print("=" * len(title))
