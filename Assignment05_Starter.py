# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KPhan,2.9.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
import fileinput

objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
file = open(objFile, "w")
dicRow = {"Task": "Task", "Priority": "Priority"}  # Setting header of file
lstTable = [dicRow]  # defining list with data in dictionary

# Writing any current data into the file
for dicRow in lstTable:
    file.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        # TODO: Add Code Here
        file = open(objFile, "r")

        # Navigating the table to read and print each line in file
        for dicRow in lstTable:
            print(dicRow["Task"], ",", dicRow["Priority"])
            file.close()
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        # TODO: Add Code Here

        # Requesting user's input for TASK and PRIORITY
        objRow = {}
        objRow["Task"] = input("Enter a task: ")
        objRow["Priority"] = input("Enter a priority [1-3]: ")

        # Checking if Task is numeric or float input
        if objRow["Task"].isnumeric() or objRow["Task"].isdigit():
            print("Sorry", "'" + objRow["Task"] + "'", "is not a valid input")

        # Checking if Priority is char or alpha
        elif objRow["Priority"].isalpha():
            print("Sorry", "'" + objRow["Priority"] + "'", "is not a valid input")

        # Adding user's data to the table list
        lstTable.append(objRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        # TODO: Add Code Here
        file = open(objFile, "r")
        strData = input("Which 'TASK' would you like to remove?: ")
        check = False  # Will set to TRUE if there is a match

        # Checking if choice exists in list
        for objRow in lstTable:

            # Defining "task" and "priority" to key and value in objRow dictionary
            task, priority = dict(objRow).values()
            if task.lower() == strData.lower():
                lstTable.remove(objRow)
                file.close()
                check = True

        # Checking if choice exists in ToDoList
        if check == True:
            print("'" + strData + "'", "was removed.")

        else:
            print("'" + strData + "'", "is not in the list")

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # TODO: Add Code Here
        strChoice = input("Would you like to save the tasks (Y/N)? ")

        # Setting option to confirm choice (Y/N)
        if strChoice.strip() == 'y':
            file = open(objFile, "w")

            for dicRow in lstTable:
                file.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")

            file.close()
            print("\nTask Saved!")

        else:
            continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        # TODO: Add Code Here
        print("Would you like to exit the program? (Y/N)")
        strChoice = input("(Any unsaved tasks will be deleted): ")

        # Setting option to confirm choice
        if strChoice.lower() == 'y':
            break  # and Exit the program
        else:
            continue

    # Checking if user provides no choice
    elif strChoice == "":
        print("\nNo option was entered. Try again.")

    else:
        print("\nSorry", "'" + strChoice + "'", "is not a valid input.")
