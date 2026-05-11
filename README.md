 
Project Description
 
This is a Command Line Interface (CLI) application developed in Python to help users track and manage personal finances. It records all income and expense transactions, ensures data integrity with validation, supports JSON storage, and automatically manages unique IDs for every record.
 
 
 
Features
 
- Object-Oriented Design: Built with a  Transaction  class to encapsulate all transaction logic, attributes, and behaviors for clean and maintainable code.
- Unique ID System: Automatically assigns unique IDs to every new transaction; properly updates sequencing even when loading existing records from storage.
- Strict Input Validation: Prevents invalid entries — checks date format, numeric amount, correct transaction type ( income  /  expense ), non-empty fields, and positive values.
- Data Serialization: Convert transaction objects to dictionary format for easy JSON saving, and reconstruct them back into objects when loading data.
- Human-Readable Formatting: Displays transactions in a clear, aligned format with proper sign ( +  for income,  -  for expense) and currency formatting.
- Data Persistence Ready: Built with methods  to_dict()  and  from_dict()  so you can easily save/load records to a JSON file.
 
 
 
Class Structure Overview
 
 Transaction  Class
 
Represents a single financial transaction.
 
Attributes:
 
-  id  (int): Unique identifier
-  date  (datetime.date): Date of transaction
-  description  (str): Short note about the transaction
-  amount  (float): Monetary value
-  type  (str): Either  income  or  expense 
-  category  (str): Classification (e.g., Food, Salary, Transport, Utilities)
 
Main Methods:
 
-  __init__()  → Initialize and validate transaction data
-  __str__()  → Return formatted readable string
-  to_dict()  → Convert object to dictionary (for saving)
-  from_dict()  → Class method to create object from dictionary (for loading)
 
 
 
 Installation & Usage
 
1. Clone the Repository
 
bash
  
git clone https://github.com/[your-username]/[your-repo-name].git
 
 
2. Navigate to Project Folder
 
bash
  
cd [your-repo-name]/src
 
 
3. Run the Program
 
bash
  
python main.py
 
 
 Sample Output
 
plaintext
  
ID: 1    | Date: 2026-04-27 | Groceries                     | Category: Food           | -$50.00
ID: 2    | Date: 2026-04-25 | Salary                        | Category: Work           | +$1,500.00
ID: 3    | Date: 2026-04-26 | Bus Fare                      | Category: Transport      | -$3.50
Next ID to be assigned: 4

Transaction 1 as dict: {'id': 1, 'date': '2026-04-27', 'description': 'Groceries', 'amount': 50.0, 'type': 'expense', 'category': 'Food'}
Transaction 1 from dict: ID: 1    | Date: 2026-04-27 | Groceries                     | Category: Food           | -$50.00

Loaded high ID transaction: ID: 100  | Date: 2026-01-01 | Old Bill                      | Category: Utilities      | -$20.00
Next ID after loading high ID: 101
ID: 101  | Date: 2026-04-28 | Dinner                        | Category: Food           | -$25.00
Next ID after new transaction: 102
 
 
 
 
 Video Demonstration
 
👉 https://youtu.be/5fscHLPZV78
 
 
 
📌 Project Details
 
- Developer: Cas, Princess Mae
- Language: Python 3
- Core Concept: OOP, Data Validation, Serialization, File Handling
- Project Type: Final Project — CLI Finance Manager
 
