import os
import csv
import getpass

from encryptionDecryption import decrypt_csv, crypt_csv
from utils import secure_delete, generatePassword, refreshDatabaseList

import globals


directory_path = globals.directory_path


# Function to delete an entry from the database
def deleteEntry(database, password):
    print("Website:", end=' ')
    website = input().strip()
    print("Username:", end=' ')
    username = input().strip()
    
    temp_file_path = os.path.join(directory_path, database + "_temp.csv")
    
    decrypt_csv(os.path.join(directory_path, database + ".csv"), temp_file_path, password)

    with open(temp_file_path, 'r') as decrypted_file:
        csv_reader = csv.reader(decrypted_file)
        rows = list(csv_reader)
        entry_found = False
        for row in rows:
            if row[0] == website and row[1] == username:
                rows.remove(row)
                entry_found = True
                break
        
        if not entry_found:
            print("Entry not found.")
            enterDatabase()
            return
    
    with open(temp_file_path, 'w', newline='') as database_file:
        csv_writer = csv.writer(database_file)
        for row in rows:
            csv_writer.writerow(row)
    
    print("Entry deleted successfully.")
    
    crypt_csv(temp_file_path, os.path.join(directory_path, database + ".csv"), password)
    secure_delete(temp_file_path)    

    enterDatabase()
    



# Function to check the content of the database
def checkDatabaseContent(database, password):
    temp_file_path = os.path.join(directory_path, database + "_temp.csv")
    
    decrypt_csv(os.path.join(directory_path, database + ".csv"), temp_file_path, password)

    with open(temp_file_path, 'r') as decrypted_file:
        csv_reader = csv.reader(decrypted_file)
        rows = list(csv_reader)
        for row in rows:
            print(row)
    
    secure_delete(temp_file_path) 
    print("--------------------------------------------------------------") 
    print("1 - Add new entry")
    print("2 - Delete entry")
    print("3 - Back")
    print("4 - Return to main menu")
    print("--------------------------------------------------------------")
    while True:
        choice = input("Enter a number (1-4): ")
        if choice == "1":
            addNewEntry(database, password)
            break
        elif choice == "2":
            deleteEntry(database, password)
            break
        elif choice == "3":
            enterDatabase()
            break
        elif choice == "4":
            return
        else:
            print("Please pick a valid option:", end=' ')




# Function to add a new entry to the database
def addNewEntry(database, password):
    print("Website:", end=' ')
    website = input().strip()
    print("Username:", end=' ')
    username = input().strip()

    # Password generation
    print("Generate password? (Y/N):", end=' ')
    while True:
        password_choice = input().strip().lower()
        if password_choice == 'y':
            password_choice = generatePassword()
            break
        elif password_choice == 'n':
            getpass.getpass("Enter your password: ").strip()
            break
        else:
            print("Please pick a valid option (Y/N):", end=' ')
    
    temp_file_path = os.path.join(directory_path, database + "_temp.csv")
    
    decrypt_csv(os.path.join(directory_path, database + ".csv"), temp_file_path, password)

    with open(temp_file_path, 'a', newline='') as database_file:
        csv_writer = csv.writer(database_file)
        csv_writer.writerow([website, username, password_choice])
    
    print("Entry added successfully.")
    
    crypt_csv(temp_file_path, os.path.join(directory_path, database + ".csv"), password)
    secure_delete(temp_file_path) 
    
    enterDatabase()





# Function to delete the database
def deleteDatabase(database):
    db_file_path = os.path.join(directory_path, database + ".csv")
    if os.path.exists(db_file_path):
        secure_delete(db_file_path)
        print("Database deleted")
    else:
        print("Database not found.")


# Function to enter the database
def enterDatabase():
    # showcase the databases
    refreshDatabaseList()
    print("--------------------------------------------------------------")
    databases = os.listdir(globals.directory_path)
    if not databases:
        print("No databases found.")
    else:
        print("Databases:")
        for db_file in databases:
            db_name, file_extension = os.path.splitext(db_file)
            print(db_name)
    print("--------------------------------------------------------------")

    print("1 - Enter a database")
    print("2 - Back")
    while True:
        choice = input("Enter a number (1-2): ")
        if choice == "1":
            break
        elif choice == "2":
            return
        else:
            print("Please pick a valid option:", end=' ')

    # Database selection
    print("Please select a Database:", end=' ')
    selected_database = input().strip()
    db_pass = getpass.getpass("Enter your password: ").strip()
    # Check if the database exists
    if selected_database + ".csv" not in databases:
        print("--------------------------------------------------------------")
        print("Database not found.")
        enterDatabase()
        return
    
    # check if the password is correct
    try: 
        temp_file_path = os.path.join(directory_path, selected_database + "_temp.csv")
        decrypt_csv(os.path.join(directory_path, selected_database + ".csv"), temp_file_path, db_pass)
        secure_delete(temp_file_path)
    except:
        secure_delete(temp_file_path)
        print("--------------------------------------------------------------")
        print("Incorrect password or an error ocurred.")
        enterDatabase()
        return
    
    
    # Database menu
    print("--------------------------------------------------------------")
    print("1 - Check database content")
    print("2 - Add new entry")
    print("3 - Delete database")
    print("4 - Back")
    print("5 - Return to main menu")
    print("--------------------------------------------------------------")
    while True:
        choice = input("Enter a number (1-3): ")
        if choice == "1":
            checkDatabaseContent(selected_database, db_pass)
            break
        elif choice == "2":
            addNewEntry(selected_database, db_pass)
            break
        elif choice == "3":
            deleteDatabase(selected_database)
            return
        elif choice == "4":
            enterDatabase()
            break
        elif choice == "5":
            return
        else:
            print("Please pick a valid option:", end=' ')

