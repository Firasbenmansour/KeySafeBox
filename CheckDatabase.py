import os
import csv
from encryptionDecryption import decrypt_csv, crypt_csv
from passwordGenerator import generatePassword

# Specify the directory path
directory_path = "Databases"

# Get the list of files and directories
databases = os.listdir(directory_path)

def checkDatabaseContent(database, password):
    temp_file_path = os.path.join(directory_path, database + "_temp.csv")
    
    decrypt_csv(os.path.join(directory_path, database + ".csv"), temp_file_path, password)

    with open(temp_file_path, 'r') as decrypted_file:
        csv_reader = csv.reader(decrypted_file)
        rows = list(csv_reader)
        for row in rows:
            print(row)
    
    os.remove(temp_file_path)

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
            print("Password:", end=' ')
            password_choice = input().strip()
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
    os.remove(temp_file_path)
    
    enterDatabase()

def deleteDatabase(database):
    db_file_path = os.path.join(directory_path, database + ".csv")
    if os.path.exists(db_file_path):
        os.remove(db_file_path)
        print("Database deleted")
    else:
        print("Database not found.")
    exit()

def enterDatabase():
    if not databases:
        print("No databases found.")
    else:
        print("Databases:")
        for db_file in databases:
            db_name, file_extension = os.path.splitext(db_file)
            print(db_name)
    
    print("Please select a Database:", end=' ')
    selected_database = input().strip()
    print("Database password:", end=' ')
    db_pass = input().strip()
    
    print("1 - Check database content")
    print("2 - Add new entry")
    print("3 - Delete database")
    
    while True:
        choice = input().strip()
        if choice == "1":
            checkDatabaseContent(selected_database, db_pass)
            break
        elif choice == "2":
            addNewEntry(selected_database, db_pass)
            break
        elif choice == "3":
            deleteDatabase(selected_database)
            break
        else:
            print("Please pick a valid option (1/2/3):", end=' ')

