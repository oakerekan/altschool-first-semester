<h1>1.0 Building an Expense Tracker in Python using Object Oriented Programming.</h1>

This project intends to build an expense tracker using python object-oriented programming concepts. 

In this project we created two classes: "Expense" and "ExpenseDatabase"

<h2>Expense Class</h2>
Have methods such as __init__, update and to_dict.

Methods:

__init__(self, title, amount): Initializes an Expense object with a unique ID, title, amount, creation time, and update time.<br>
update(self, title=None, amount=None): Updates the title and/or amount of the expense and modifies the updated_at timestamp accordingly.<br>
to_dict(self): Converts the expense object into a dictionary format for easy serialization.<br>

<h2>ExpenseDatabase Class</h2>

Have methods such as __init__, add_expense, remove_expense, get_expense_by_id, get expense_by_title, to_dict

Methods:

__init__(self): Initializes an empty list to store expenses.<br>
add_expense(self, expense): Adds a new expense object to the database.<br>
remove_expense(self, expense_id): Removes an expense from the database by its ID.<br>
get_expense_by_id(self, expense_id): Retrieves an expense by its ID.<br>
get_expense_by_title(self, expense_title): Retrieves a list of expenses with a given title.<br>
to_dict(self): Converts the list of expenses into a dictionary format for easy serialization.<br>


<h2>Notes</h2>
The Expense class represents individual expenses with unique IDs, titles, amounts, creation times, and update times.<br>
The ExpenseDatabase class manages a list of expenses, allowing addition, removal, and retrieval based on ID or title.<br>
The code uses UUID for unique identification, datetime for timestamp management, and dictionary formats for easy conversion and serialization.


<h1>2.0 Cloning the Project</h1>

In Github, we clone the repository by using the git clone. The git clone command is used to create a copy of a specific repository or branch within a repository.

Git is a distributed version control system. Maximize the advantages of a full repository on your own machine by cloning.

<h2>Steps to Clone</h2>
The steps to Initiation a git clone.<br>
1. Create a folder in the local machine to clone your remote repository into by using the keyword in windows "mkdir {directory-name}", after initially setting your terminal to the right directory using the "cd {directory-name}." <br>
Any of the terminal on your system can be used for handling git provided it is already installed on your system. Be it Powershell, CommandPrompt, Git Bash, VS Code and even Git GUI.<br>
2. Cloning the git repository into the folder created using the ```git clone https://github.com/oakerekan/altschool-first-semester.git/``` command. <br>

When you clone a repository, you don't get one file, like you may in other centralized version control systems. By cloning with Git, you get the entire repository - all files, all branches, and all commits.

<p>Cloning a repository is typically only done once, at the beginning of your interaction with a project. Once a repository already exists on a remote, like on GitHub, then you would clone that repository so you could interact with it locally. Once you have cloned a repository, you won't need to clone it again to do regular development.</p>

<p>The ability to work with the entire repository means that all developers can work more freely. Without being limited by which files you can work on, you can work on a feature branch to make changes safely.</p>


<h1> 3.0 How to Run the Expense Tracker</h1>