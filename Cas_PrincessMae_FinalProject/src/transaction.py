import datetime

class Transaction:
    """
    Represents a single financial transaction (income or expense).

    Attributes:
        id (int): A unique identifier for the transaction.
        date (datetime.date): The date the transaction occurred.
        description (str): A brief description of the transaction.
        amount (float): The monetary value of the transaction.
        type (str): The type of transaction ('income' or 'expense').
        category (str): The category the transaction belongs to (e.g., 'Food', 'Salary').
    """
    next_id = 1 # Class-level attribute to assign unique IDs

    def __init__(self, date: datetime.date, description: str, amount: float, type: str, category: str, id: int = None):
        """
        Initializes a new Transaction object.

        Args:
            date (datetime.date): The date of the transaction.
            description (str): A description of the transaction.
            amount (float): The amount of the transaction.
            type (str): 'income' or 'expense'.
            category (str): The category of the transaction.
            id (int, optional): An optional ID for loading existing transactions.
                                If None, a new unique ID is assigned.
        """
        if not isinstance(date, datetime.date):
            raise TypeError("Date must be a datetime.date object.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if type not in ['income', 'expense']:
            raise ValueError("Type must be 'income' or 'expense'.")
        if not description or not category:
            raise ValueError("Description and category cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.id = id if id is not None else Transaction.next_id
        if id is None: # Only increment next_id if it's a new transaction
            Transaction.next_id += 1

        self.date = date
        self.description = description
        self.amount = amount
        self.type = type
        self.category = category

    def __str__(self):
        """
        Returns a human-readable string representation of the transaction.
        """
        sign = "+" if self.type == "income" else "-"
        return f"ID: {self.id:<4} | Date: {self.date} | {self.description:<30} | Category: {self.category:<15} | {sign}PHP{self.amount:,.2f}"

    def to_dict(self):
        """
        Converts the Transaction object into a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "date": self.date.isoformat(),  
            "description": self.description,
            "amount": self.amount,
            "type": self.type,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Transaction object from a dictionary (e.g., loaded from JSON).
        Also updates the class's next_id to ensure uniqueness for new transactions.
        """
        # Ensure next_id is greater than any loaded ID
        if data["id"] >= cls.next_id:
            cls.next_id = data["id"] + 1

        return cls(
            date=datetime.date.fromisoformat(data["date"]), 
            description=data["description"],
            amount=data["amount"],
            type=data["type"],
            category=data["category"],
            id=data["id"]
        )


if __name__ == "__main__":
    try:
        t1 = Transaction(datetime.date(2026, 4, 27), "Groceries", 50.00, "expense", "Food")
        print(t1)
        t2 = Transaction(datetime.date(2026, 4, 25), "Salary", 1500.00, "income", "Work")
        print(t2)
        t3 = Transaction(datetime.date(2026, 4, 26), "Bus Fare", 3.50, "expense", "Transport")
        print(t3)
        print(f"Next ID to be assigned: {Transaction.next_id}")

        
        t1_dict = t1.to_dict()
        print(f"\nTransaction 1 as dict: {t1_dict}")
        t1_from_dict = Transaction.from_dict(t1_dict)
        print(f"Transaction 1 from dict: {t1_from_dict}")

        
        t_loaded_high_id = Transaction.from_dict({"id": 100, "date": "2026-01-01", "description": "Old Bill", "amount": 20, "type": "expense", "category": "Utilities"})
        print(f"Loaded high ID transaction: {t_loaded_high_id}")
        print(f"Next ID after loading high ID: {Transaction.next_id}")
        t4 = Transaction(datetime.date(2026, 4, 28), "Dinner", 25.00, "expense", "Food")
        print(t4) # Should have ID 101
        print(f"Next ID after new transaction: {Transaction.next_id}")


    except (TypeError, ValueError) as e:
        print(f"Error creating transaction: {e}")
