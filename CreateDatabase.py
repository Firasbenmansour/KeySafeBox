import os
import getpass
import globals
from utils import secure_delete, refreshDatabaseList
from encryptionDecryption import crypt_csv

def createDatabase():
    print("--------------------------------------------------------------")
    dbName = input("Database name: ").strip()
    dbNameCheck = dbName + ".csv"

    while dbNameCheck in globals.databases:
       print("Database already exists.")
       dbName = input("Database name: ").strip()
       dbNameCheck = dbName + ".csv"
   
    while True:
        dbPass = getpass.getpass("Enter your password: ").strip()
        dbPassConfirm = getpass.getpass("Confirm password: ").strip()
        if dbPass != dbPassConfirm:
            print("Passwords do not match.")
        elif len(dbPass) < 8:
            print("Password must be at least 8 characters.")
        else:
            break

    temp_file_path = os.path.join(globals.directory_path, dbName + "_temp.csv")
    with open(temp_file_path, "x", newline='') as databaseFile:
        databaseFile.write("Website,Username,Password\n")

    encrypted_file_path = os.path.join(globals.directory_path, dbName + ".csv")
    crypt_csv(temp_file_path, encrypted_file_path, dbPass)
    secure_delete(temp_file_path)

    # Refresh the global database list
    refreshDatabaseList()

    print("Database created successfully.")
