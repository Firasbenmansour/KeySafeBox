import os
import random
import string



#deleteFile.py
def overwrite_with_random_data(file_path, passes=3):
    """Overwrites the file multiple times with random data."""
    with open(file_path, "ba+", buffering=0) as f:
        length = f.tell()  # Get the file size
        for _ in range(passes):
            f.seek(0)  # Go to the start of the file
            f.write(os.urandom(length))  # Overwrite with random bytes

def secure_delete(file_path, passes=3):
    """Securely deletes the file by overwriting and then deleting it."""
    if os.path.exists(file_path):
        # Overwrite the file contents
        overwrite_with_random_data(file_path, passes)
        
        # Rename the file to minimize metadata traces
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        new_path = os.path.join(os.path.dirname(file_path), random_name)
        os.rename(file_path, new_path)
        
        # Delete the renamed file
        os.remove(new_path)






#passwordGenerator.py
def optionPick():
     while True: 
          choice = input().strip().lower()
          if choice == 'y':
             return True
          elif choice == 'n':
             return False
          else:
             print("Please pick a valid option:", end=' ')

def generatePassword():
     # password length 
     print("--------------------------------------------------------------")
     print("How long you would want your password to be:", end=' ')
     
     while True:
        try:
            passLength=input()
            passLength = int(passLength)
            if not(passLength < 8):      
               break
            else:
               print("Please choose a password that is at least 8 characters:", end=' ')
        except:
            print("Please pick a valid number:", end=' ')
     
     # password user configuration input  
     while True:
         print("Uppercase characters?(Y/N)):", end=' ')
         uppercase = optionPick()
         print("Lowercase characters?(Y/N)):", end=' ')
         lowercase = optionPick()  
         print("Numbers?(Y/N)):", end=' ')
         numbers = optionPick()  
         print("Symbols?(Y/N)):", end=' ')
         symbols = optionPick()
         if sum([uppercase, lowercase, numbers, symbols]) >= 2:
            break
         else:
             print("Please select at least two options.")
     
     # password generation
     
     characterSet = ""
     if uppercase:
        characterSet += string.ascii_uppercase
     if lowercase:
        characterSet += string.ascii_lowercase
     if numbers:
        characterSet += string.digits
     if symbols:
        characterSet += string.punctuation
        
     password = ""
     for _ in range(passLength):
         password += random.choice(characterSet)
         
     print("Generated Password:", password)
     return password
     
     
directory_path = "Databases"
def refreshDatabaseList():
    global databases
    databases = os.listdir(directory_path)
