import os
import sys
from src.finance_manager import FinanceManager

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- FinTrack CLI Menu ---")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Income Transactions")
    print("4. View Expense Transactions")
    print("5. View Balance")
    print("6. View Category Summary")
    print("7. Edit Transaction")
    print("8. Delete Transaction")
    print("9. Exit")
    print("------------------------")

def get_user_input(prompt: str, validation_func=None, error_msg: str = "Invalid input."):
    """Helper function to get validated user input."""
    while True:
        value = input(prompt).strip()
        if validation_func:
            try:
                if validation_func(value):
                    return value
                else:
                    print(error_msg)
            except ValueError:
                print(error_msg)
        else:
            return value

def validate_amount(amount_str: str) -> float:
    """Validates if a string can be converted to a positive float."""
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Amount must be a positive number.")

def validate_date(date_str: str) -> bool:
    """Validates if a string is in YYYY-MM-DD format."""
    try:
        year, month, day = map(int, date_str.split('-'))
        return 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        print("An error occured!")
    finally:
        print("Execution of try/except/finally block finished.")