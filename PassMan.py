import pyfiglet
import cryptography
import random
import string
from passwordGenerator import *

def Banner():
    print("-----------------------------------------------")
    Title = pyfiglet.figlet_format("PassMan", font="slant")
    print(Title)
    print("-----------------------------------------------")
    return 1

def databaseMenu():
    print("1 - Stock Password")
    print("2 - Check Password database")
    choice=input()
    match choice:
          case 1:
              Stock()
          case 2:
              checkDatabase()
          case _:
              print("Please pick a valid option")
    return 1


##### MAIN #####
Banner()
print("Your trustworthy password manager at your service anytime you want!")
print("1 - Create Database")
print("2 - Enter Database")
print("3 - Delete Database")
print("4 - Generate Password")
choice=input()
match choice:
      case 1:
          createDatabase()
      case 2:
          enterDatabase()
      case 3:
          deleteDatabase()
      case "4":
          generatePassword()
      case _:
          print("Please pick a valid option")

