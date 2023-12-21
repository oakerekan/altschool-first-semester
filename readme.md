This is the remote repository which contains the implement of the first semester hands-on project for the data enginee course on altschool


Expense Class:
Attributes:
id: Unique identifier for the expense (UUID4 format).
title: Title/name of the expense.
amount: Numerical value representing the expense amount.
created_at: Date and time of expense creation in UTC.
updated_at: Date and time of the last update to the expense in UTC.
Methods:
_init_(self, title, amount): Initializes an Expense object with a unique ID, title, amount, creation time, and update time.
update(self, title=None, amount=None): Updates the title and/or amount of the expense and modifies the updated_at timestamp accordingly.
to_dict(self): Converts the expense object into a dictionary format for easy serialization.
ExpenseDatabase Class:
Attributes:

expenses: List holding Expense objects.
Methods:

_init_(self): Initializes an empty list to store expenses.
add_expense(self, expense): Adds a new expense object to the database.
remove_expense(self, expense_id): Removes an expense from the database by its ID.
get_expense_by_id(self, expense_id): Retrieves an expense by its ID.
get_expense_by_title(self, expense_title): Retrieves a list of expenses with a given title.
to_dict(self): Converts the list of expenses into a dictionary format for easy serialization.
Notes:
The Expense class represents individual expenses with unique IDs, titles, amounts, creation times, and update times.
The ExpenseDatabase class manages a list of expenses, allowing addition, removal, and retrieval based on ID or title.
The code uses UUID for unique identification, datetime for timestamp management, and dictionary formats for easy conversion and serialization.