# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# Change Log (Who, When, What):
# RRoot, 1.1.2020, Created started script
# HChung, 5.16.2020, Added code to complete Assignment 5
# HChung, 5.16.2020, Removed unnecessary variables; Added "(in Memory)" storage information for user
# HChung, 5.17.2020, Added user option to save/not save when choose Option 4
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare my variables
objFile = None  # An object that represents a file
strFile = "ToDoList.txt" # Data storage file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection
strTask = "" # The name of the task
strPriority = "" # The task's priority
strRemoved = "" # The removed task


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")
for row in objFile:  # Capturing data from the File
    t, p = row.split(",")  # Split to capture Task & Priority in variables (split will unpack)
    dicRow = {"Task": t.strip(), "Priority": p.strip()} # get rid of \n
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your Current Data (in Memory) is: \n")
        print("TASK - PRIORITY")
        for row in lstTable:
            print(row["Task"] + ' - ' + row["Priority"])
        continue

    # Step 4 Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Capturing data from the user
        while (True):
            print("Enter a 'Task' and its 'Priority' - ")
            strTask = str(input("Enter Task Name: "))
            strPriority = str(input("Enter Priority ['Low', 'Med', 'High']: "))
            lstTable.append({"Task": strTask, "Priority": strPriority}) # making a dictionary row in the list
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while (True):
            print("\nWhich item would you like to remove (from Memory)?")
            for row in lstTable:
                print(row["Task"])
            strRemoved = str(input("\nTask to Remove: "))
            for row in lstTable:
                if row["Task"].lower() == strRemoved.lower():
                    lstTable.remove(row)
                    print("Task Removed")
                    break
            else:
                print("Row not found")
            strChoice = input ("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would you like to save your data to " + strFile + " ?")
        strChoice = str(input("Enter 'y' or 'n': "))
        if (strChoice.lower() == 'y'):
            objFile = open(strFile, "w")
            print("\nThe following 'Task' and 'Priority' were saved to " + strFile + ": ")
            for row in lstTable:
                objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n") # Use ',' separator for file
                print(row["Task"] + " - " + row["Priority"]) # Use '-' separator for user
            objFile.close()

        else:
            print("\nChanges were not saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press the 'Enter' key to exit the program. ")
        break  # and Exit the program
