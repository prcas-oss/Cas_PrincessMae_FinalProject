FinTrack CLI - Personal Finance Tracker
 
System Overview
 
FinTrack CLI is a robust Command-Line Interface (CLI) application designed for personal finance tracking. It provides users with an intuitive and efficient platform to manage and analyze their income and expenses directly from the terminal. The system aims to offer a clear and accessible way to monitor financial habits, enabling better insight and control over personal economic activities.
 
Core Features
 
The FinTrack CLI system incorporates the following functionalities:
 
- Transaction Management:- Add New Transactions: Facilitates the entry of income and expense records, including details such as date, textual description, monetary amount, transaction type (income/expense), and category.
- Edit Existing Transactions: Allows modification of details for any recorded transaction.
- Delete Transactions: Supports the removal of specific transactions from the record.
- Transaction Viewing & Filtering:- View All Transactions: Displays a comprehensive list of all recorded financial activities, typically sorted chronologically.
- View Income-Specific Transactions: Filters and presents only income entries.
- View Expense-Specific Transactions: Filters and presents only expense entries.
- Financial Reporting:- Current Balance Calculation: Computes and displays the net financial position (total income minus total expenses).
- Category-Based Summary: Generates a detailed breakdown of income, expenses, and net amounts aggregated by user-defined categories, aiding in financial analysis and budgeting.
- Data Persistence: All transaction data is automatically saved to and loaded from a structured JSON file, ensuring that financial records are preserved across application sessions.
 
Technical Architecture
 
The FinTrack CLI is engineered using Python, adhering to Object-Oriented Programming (OOP) paradigms for a structured and maintainable codebase. Key architectural components include:
 
-  Transaction  Class:- Serves as the data model for individual financial records, encapsulating attributes such as a unique identifier ( id ),  date ,  description ,  amount ,  type , and  category .
- Includes built-in data validation mechanisms for attributes like  date ,  amount , and  type  to ensure data integrity.
- Manages automatic assignment of unique transaction identifiers.
- Provides serialization ( to_dict ) and deserialization ( from_dict ) methods for seamless conversion between object instances and dictionary representations suitable for JSON storage.
-  FinanceManager  Class:- Acts as the central business logic controller, managing a collection of  Transaction  objects.
- Implements all core operations: adding, viewing, editing, deleting, and summarizing transactions.
- Manages data loading from ( _load_data ) and saving to ( _save_data ) the persistent  transactions.json  file.
- Data Processing & Validation:- Utilizes efficient Python constructs such as list comprehensions for filtering,  sorted()  with  lambda  for ordering, and dictionary aggregations for generating summary reports.
- Incorporates robust input validation and error handling routines to prevent invalid data entries and ensure a stable user experience.
