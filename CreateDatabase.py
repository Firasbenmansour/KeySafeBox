from encryptionDecryption import *
import os

def createDatabase():
    print("Database name:", end=' ')
    dbName = input().strip()
    while True:
       print("Database password:", end=' ')
       dbPass = input().strip()
       print("Confirm password:", end=' ')
       dbPassConfirm = input().strip()
       if dbPass != dbPassConfirm :
          print("Passwords do not match.")
       elif len(dbPass) < 8:
          print("Password must be at least 12 characters.")
       else:
          break

    with open(dbName + ".csv", "x") as databaseFile:
       databaseFile.write("Website,Username,Password\n")
       databaseFile.close()


    crypt_csv(dbName + ".csv", dbName + "_encrypted.csv", dbPass)
    os.remove(dbName + ".csv")
    os.rename(dbName + "_encrypted.csv", dbName + ".csv")
    print("Database created successfully.")


