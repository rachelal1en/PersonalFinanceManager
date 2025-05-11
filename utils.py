import mysql.connector

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


def save_to_db(db_connection, table, data):
    """
    Generic function to save data into a specific table.
    """
    try:
        # Generate the column names and placeholders for query
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        # Execute the query with vvalues
        cursor = db_connection.cursor()
        cursor.execute(query, tuple(data.values()))
        db_connection.commit()
        print(f"Data saved successfully to {table} table.")
    except mysql.connector.Error as e:
        print(f"Error saving data to {table} table: {e}")


def load_from_db(db_connection, table, columns='*', conditions=None):
    """
    Generic function to load data from a specific table.
    """
    try:
        # Start building the query
        conditions_clause = ''
        if conditions:
            # Build WHERE clause dynamically
            conditions_clause = ' WHERE ' + ' AND '.join([f"{col} = %s" for col in conditions.keys()])

        query = f"SELECT {columns} FROM {table}{conditions_clause}"

        # Execute the query
        cursor = db_connection.cursor()
        if conditions:
            cursor.execute(query, tuple(conditions.values()))
        else:
            cursor.execute(query)

        results = cursor.fetchall()
        return results
    except mysql.connector.Error as e:
        print(f"Error loading from database: {e}")
        return []

