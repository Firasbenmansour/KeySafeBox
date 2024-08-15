import pyfiglet
from passwordGenerator import *
from CreateDatabase import *
from CheckDatabase import *

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
while True:
    choice = input("Enter a number (1-3): ")
    if choice == "1":
        print("-----------------------------------------------")
        createDatabase()
        break
    elif choice == "2":
        print("-----------------------------------------------")
        enterDatabase()
        break
    elif choice == "3":
        print("-----------------------------------------------")
        generatePassword()
        break
    else:
        print("Please pick a valid option")

