import pyfiglet
from passwordGenerator import *
from CreateDatabase import *

def Banner():
    print("-----------------------------------------------")
    Title = pyfiglet.figlet_format("PassMan", font="slant")
    print(Title)
    print("-----------------------------------------------")
    return 1


##### MAIN #####
Banner()
print("Your trustworthy password manager at your service anytime you want!")
print("1 - Create Database")
print("2 - Check Databases")
print("3 - Generate Password")
choice = input("Enter a number (1-4): ")
match choice:
      case "1":
          createDatabase()
      case "2":
          checkDatabase()
      case "3":
          generatePassword()
      case _:
          print("Please pick a valid option")

