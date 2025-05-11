import mysql.connector

from expenses import ExpenseManager
from savings_calculator import SavingsCalculator
from change_calculator import ChangeCalculator

def get_db_connection():
    # Establish and return the database connection
    return mysql.connector.connect(
        host="localhost",
        user="pfm",
        password="pfm2025",
        database="pfm"
    )

# Passing the connection
# expense_manager = ExpenseManager(mydb)
# savings_calculator = SavingsCalculator(mydb)
# change_calculator = ChangeCalculator(mydb)
#
#
# # usages
# expense_manager.track_expense()
# savings_calculator.calculate_future_value()

# print(mydb)