#passwordGenerator.py

import random
import string

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
     
     
     
