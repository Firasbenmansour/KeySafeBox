import pyfiglet
from CreateDatabase import *
from CheckDatabase import *

def Banner():
    print("--------------------------------------------------------------")
    Title = pyfiglet.figlet_format("Key Safe Box", font="slant")
    print(Title)
    return 1


def mainMenu():
    print("--------------------------------------------------------------")
    print("Your trustworthy and secure password manager at your service!")
    print("1 - Create Database")
    print("2 - Check Databases")
    print("3 - Generate Password")
    print("4 - Exit")
    while True:
        choice = input("Enter a number (1-4): ")
        if choice == "1":
            createDatabase()
            mainMenu()
            break
        elif choice == "2":
            enterDatabase()
            mainMenu()
            break
        elif choice == "3":
            generatePassword()
            mainMenu()
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please pick a valid option")
    return 1


if __name__ == "__main__":
    if not os.path.exists("Databases"):
        os.makedirs("Databases")
    Banner()
    mainMenu()
