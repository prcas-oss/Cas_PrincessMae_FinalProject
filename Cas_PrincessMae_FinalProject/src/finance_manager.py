import json
import datetime
from transaction import Transaction # Import the Transaction class

class FinanceManager:
    """
    Manages a collection of financial transactions, including adding,
    viewing, summarizing, and persisting them to a file.
    """

    def __init__(self, data_file='data/transactions.json'):
        """
        Initializes the FinanceManager and loads transactions from the data file.

        Args:
            data_file (str): The path to the JSON file for storing transactions.
        """
        self.data_file = data_file
        self.transactions: list[Transaction] = []
        self._load_data()

    def _load_data(self):
        """
        Loads transaction data from the JSON file.
        Updates Transaction.next_id to ensure new transactions get unique IDs.
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    print(f"Warning: Data file '{self.data_file}' is not a list. Initializing with empty transactions.")
                    self.transactions = []
                    return

                self.transactions = []
                max_id = 0
                for item in data:
                    try:
                        transaction = Transaction.from_dict(item)
                        self.transactions.append(transaction)
                        if transaction.id > max_id:
                            max_id = transaction.id
                    except (ValueError, TypeError, KeyError) as e:
                        print(f"Error loading transaction from file: {item}. Skipping. Error: {e}")
                Transaction.next_id = max_id + 1 if max_id >= Transaction.next_id else Transaction.next_id
                print(f"Loaded {len(self.transactions)} transactions. Next ID set to {Transaction.next_id}.")
        except FileNotFoundError:
            print(f"No data file found at '{self.data_file}'. Starting with no transactions.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{self.data_file}'. File might be corrupted. Starting with no transactions.")
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
        finally:
            # Ensure the data directory exists
            import os
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)


    def _save_data(self):
        """
        Saves all current transactions to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=4)
            print("Data saved successfully.")
        except IOError as e:
            print(f"Error saving data to '{self.data_file}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving data: {e}")


    def add_transaction(self, date_str: str, description: str, amount: float, type: str, category: str) -> bool:
        """
        Adds a new transaction to the manager and saves the data.

        Args:
            date_str (str): The date of the transaction in YYYY-MM-DD format.
            description (str): A description of the transaction.
            amount (float): The amount of the transaction.
            type (str): 'income' or 'expense'.
            category (str): The category of the transaction.

        Returns:
            bool: True if transaction was added successfully, False otherwise.
        """
        try:
            transaction_date = datetime.date.fromisoformat(date_str)
            transaction = Transaction(transaction_date, description, amount, type, category)
            self.transactions.append(transaction)
            self._save_data()
            print(f"Transaction added: {transaction}")
            return True
        except ValueError as e:
            print(f"Error adding transaction: {e}. Please check date format (YYYY-MM-DD), amount, type, and category.")
            return False
        except TypeError as e:
            print(f"Error adding transaction: {e}.")
            return False

    def view_transactions(self, filter_type: str = None, filter_category: str = None):
        """
        Displays all transactions, optionally filtered by type or category.

        Args:
            filter_type (str, optional): 'income' or 'expense' to filter transactions.
            filter_category (str, optional): Category name to filter transactions.
        """
        filtered_transactions = self.transactions

        if filter_type:
            filtered_transactions = [t for t in filtered_transactions if t.type == filter_type]
        if filter_category:
            filtered_transactions = [t for t in filtered_transactions if t.category.lower() == filter_category.lower()]

        if not filtered_transactions:
            print("No transactions to display.")
            return

        print("\n--- All Transactions ---")
        # Sort by date for better readability (optional, but good practice)
        for t in sorted(filtered_transactions, key=lambda x: x.date):
            print(t)
        print("------------------------")

    def get_balance(self) -> float:
        """
        Calculates and returns the current balance (total income - total expenses).
        """
        total_income = sum(t.amount for t in self.transactions if t.type == 'income')
        total_expense = sum(t.amount for t in self.transactions if t.type == 'expense')
        balance = total_income - total_expense
        print(f"\nCurrent Balance: ${balance:,.2f}")
        return balance

    def get_summary_by_category(self):
        """
        Calculates and displays the total amount for each category.
        """
        category_summary = {}
        for t in self.transactions:
            if t.category not in category_summary:
                category_summary[t.category] = {'income': 0.0, 'expense': 0.0}
            category_summary[t.category][t.type] += t.amount

        print("\n--- Category Summary ---")
        if not category_summary:
            print("No categories to summarize.")
            return

        for category, amounts in category_summary.items():
            net_amount = amounts['income'] - amounts['expense']
            print(f"Category: {category:<15} | Income: ${amounts['income']:<10,.2f} | Expense: ${amounts['expense']:<10,.2f} | Net: ${net_amount:,.2f}")
        print("------------------------")

    def edit_transaction(self, transaction_id: int, new_data: dict) -> bool:
        """
        Edits an existing transaction based on its ID.

        Args:
            transaction_id (int): The ID of the transaction to edit.
            new_data (dict): A dictionary of fields to update (e.g., {'amount': 60.0, 'description': 'New Desc'}).

        Returns:
            bool: True if the transaction was found and updated, False otherwise.
        """
        for i, t in enumerate(self.transactions):
            if t.id == transaction_id:
                try:
                    # Validate new data before applying
                    if 'date' in new_data:
                        new_data['date'] = datetime.date.fromisoformat(new_data['date'])
                    if 'amount' in new_data and not isinstance(new_data['amount'], (int, float)):
                        raise ValueError("Amount must be a number.")
                    if 'type' in new_data and new_data['type'] not in ['income', 'expense']:
                        raise ValueError("Type must be 'income' or 'expense'.")
                    if 'description' in new_data and not new_data['description']:
                        raise ValueError("Description cannot be empty.")
                    if 'category' in new_data and not new_data['category']:
                        raise ValueError("Category cannot be empty.")
                    if 'amount' in new_data and new_data['amount'] <= 0:
                        raise ValueError("Amount must be positive.")

                    # Apply updates
                    for key, value in new_data.items():
                        setattr(t, key, value)
                    self._save_data()
                    print(f"Transaction ID {transaction_id} updated successfully.")
                    return True
                except (ValueError, TypeError) as e:
                    print(f"Error updating transaction ID {transaction_id}: {e}")
                    return False
        print(f"Transaction with ID {transaction_id} not found.")
        return False

    def delete_transaction(self, transaction_id: int) -> bool:
        """
        Deletes a transaction based on its ID.

        Args:
            transaction_id (int): The ID of the transaction to delete.

        Returns:
            bool: True if the transaction was found and deleted, False otherwise.
        """
        initial_len = len(self.transactions)
        self.transactions = [t for t in self.transactions if t.id != transaction_id]
        if len(self.transactions) < initial_len:
            self._save_data()
            print(f"Transaction ID {transaction_id} deleted successfully.")
            return True
        else:
            print(f"Transaction with ID {transaction_id} not found.")
            return False
