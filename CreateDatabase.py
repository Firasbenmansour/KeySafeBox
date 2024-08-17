import os
import getpass

from encryptionDecryption import crypt_csv
from utils import secure_delete, refreshDatabaseList

# Specify the directory path
if not os.path.exists("Databases"):
       os.makedirs("Databases")
directory_path = "Databases"

databases = os.listdir(directory_path)

def createDatabase():
    print("--------------------------------------------------------------")
    print("Database name:", end=' ')
    dbName = input().strip()
    while True:
       dbPass = getpass.getpass("Enter your password: ").strip()
       dbPassConfirm = getpass.getpass("Confirm password: ").strip()
       if dbPass != dbPassConfirm :
          print("Passwords do not match.")
       elif len(dbPass) < 8:
          print("Password must be at least 12 characters.")
       else:
          break
       
    temp_file_path = os.path.join(directory_path, dbName + "_temp.csv")
    with open(temp_file_path, "x", newline='') as databaseFile:
       databaseFile.write("Website,Username,Password\n")
       databaseFile.close()

    encrypted_file_path = os.path.join(directory_path, dbName + ".csv")
    crypt_csv(temp_file_path, encrypted_file_path, dbPass)
    secure_delete(temp_file_path)
    
    refreshDatabaseList()

    print("Database created successfully.")

