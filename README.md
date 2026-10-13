💰 Expense Tracker Using Python

A simple, menu-driven Expense Tracker built with Python that helps users record, manage, and analyze their daily expenses using file handling.

The application stores expense records permanently in a text file, making it easy to track spending without requiring a database.
```
✨ Features
➕ Add Expense – Add a new expense with title, category, and amount.
📋 View All Expenses – Display all saved expense records.
💵 Calculate Total Expense – Calculate the total amount spent.
🏆 Find Highest Expense – Identify the expense with the highest amount.
🔍 Search by Category – Find expenses belonging to a specific category.
💾 File-Based Storage – Save expense records permanently in expenses.txt.
🔄 Menu-Driven Interface – Navigate through options using a simple command-line menu.
🇮🇳 Currency Formatting – Display expense amounts using the ₹ symbol.
```
🛠️ Technologies Used
```
Language: Python
Concepts: Functions, Loops, Conditional Statements, File Handling, Exception Handling
Storage: Text file (expenses.txt)
Interface: Command-Line Interface (CLI)
```
📁 Project Structure
```
Expense-Tracker/
│
├── expense.py
├── expenses.txt
└── README.md
```

File Description
```
expense.py – Contains the main program and all expense management functions.
expenses.txt – Stores expense records permanently.
README.md – Provides project documentation and usage instructions.
Note: expenses.txt is created automatically when the first expense is added. You do not need to create it manually.
```
⚙️ Getting Started
Prerequisites

Install Python 3 on your computer.

Check whether Python is installed:

python --version


Alternatively, on some systems:

python3 --version

1. Clone the Repository

Replace YOUR-USERNAME with your GitHub username.

git clone https://github.com/YOUR-USERNAME/Expense-Tracker.git

2. Navigate to the Project Directory
cd Expense-Tracker

3. Run the Application

Windows:

python expense.py


Linux/macOS:

python3 expense.py

🖥️ Sample Output
========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. Calculate Total Expense
4. Find Highest Expense
5. Search Expense by Category
6. Exit
```
Enter your choice: 1

Enter expense title: Groceries
Enter category: Food
Enter amount: 500

Expense added successfully!

Sample Expense Records

The expenses.txt file stores records in the following format:

Groceries|Food|500.0
Petrol|Travel|1200.0
Electricity Bill|Utilities|1500.0
```

Each record contains the expense title, category, and amount separated by the | character.
```
🎯 Learning Objectives
Understand Python file handling using open().
Learn to read and append data to text files.
Practice functions and modular programming.
Work with lists, tuples, and string operations.
Handle missing files using exception handling.
Perform calculations and category-based searches.
🚀 Future Enhancements
Add expense date tracking.
Validate expense amounts and user inputs.
Edit and delete existing expenses.
Generate monthly expense reports.
Display category-wise spending summaries.
Export expense reports to CSV.
Add a graphical user interface (GUI).
👨‍💻 Author

Your Name

GitHub: YOUR-USERNAME
📄 License
```
This project is intended for educational and learning purposes. Add an appropriate open-source license if you plan to distribute it publicly.

⭐ If you find this project useful, consider giving the repository a star!
