import winsound
from datetime import *  # I have imported the time of the current location for users to determine what time it

# is where they are currently located.

now = datetime.now()
time = datetime.now
today = date.today()
current_time = now.strftime("%H:%M")


def main_menu():  # This main Menu is used throughout the program to allow the user to see the different location
    # options.
    print("""  \n    The Current time is""", current_time)
    print("""   The Date today is""", today)
    print("""\033[1;32;1m   ----------------------------
   ----------------------------
     WELCOME TO TRAVELCEPTION
   ----------------------------
   ----------------------------
""" " \033[1;37;1m Where are we traveling today? ")
    print("         1. America")
    print("         2. Italy")
    print("         3. Greece")
    print("         4. Help")
    print("         5. Exit")


def america():  # This is the main interface for the American option which is defined as a variable to save space later
    # in the program when printing
    print("Yes America, how wonderful")
    print("\nAmerican Information  ")
    print("1. Culture of America")
    print("2. Simple Terms and Phrases")
    print("3. Do's and Dont's")
    print("4. Go Back")


def italy():  # This is the interface for the Italy option on the main screen, again used to save space
    print("Italy, going to the city of love are we ;)")
    print("\nItaly Information  ")
    print("1. Culture of Italy")
    print("2. Simple Terms and Phrases")
    print("3. Do's and Dont's")
    print("4. Go Back")


def greece():  # This is the interface for the Greece option on the main screen, again used to save space
    print("Ahh Greece, the birthplace of the olympics!")
    print("\nGreece Information  ")
    print("1. Culture of Greece")
    print("2. Simple Terms and Phrases")
    print("3. Do's and Dont's")
    print("4. Go Back")


def help():  # This is a help screen that is shown to users to help them navigate the application
    print("""
                        ------------------
                            How to use
                        ------------------
    When starting the program, input the option you want to 
    through inputting the number on your keyboard. For example
    if you want to learn information about America input 1 on 
    your keyboard to select American information. All options 
    will have a choice to go back to the main menu if you 
    accidentally select the wrong option. If you want to leave
    the program just input 5 on the main menu to quit.

    """)
    input("Click enter to go back...")  # This code bellow allows the user to go back to the main screen and
    # continue through the rest of the application
    main_menu()
    locationchoice = input("Where do you want to go?: ")
    location(locationchoice)
    userchoice = choice()
    selection(locationchoice, userchoice)


def Exit():  # This is a simple exit for users to use to leave the program
    print("It was a pleasure")
    exit()


def errorcheck(locationchoice):
    if locationchoice >= "5":
        print("Invalid choice please try again!!")
        locationchoice = input("Where do you want to go?: ")
        errorcheck(locationchoice)
    location(locationchoice)
    userchoice = choice()
    selection(locationchoice, userchoice)


def location(locationchoice):  # This function runs the input of the user and selects what country should be printed
    # on the screen
    if locationchoice == "1" or choice == "America":
        america()
    elif locationchoice == "2" or choice == "Italy":
        italy()
    elif locationchoice == "3" or choice == "Greece":
        greece()
    elif locationchoice == "4" or choice == "Help":
        help()
    elif locationchoice == "5" or choice == "Exit":
        Exit()
    else:  # The Else statement is used to detect invalid inputs and allow the user to go back and try again
        print("Invalid option please try again")
        locationchoice = input("\nWhere do you want to go?: ")
        errorcheck(locationchoice)
    return locationchoice


def choice():  # The function Choice asks the user what they want to learn about each country and returns the outcome
    # as a variable used in other functions.
    userchoice = input("What are we learning about today?: ")
    return userchoice


def selection(locationchoice, userchoice):  # The Selection function uses the users input to determine the type of
    # information the user wants to learn about from what country through using 2 separate inputs. Each elif statement
    # is has a different set of inputs that determine what information to use.

    if locationchoice in ("1", "America") and userchoice == "1":  # This documentation is used to read the parameters of
        f = open("AmericaInformation/AmericaCulture.txt", "r")    # the application and then open the desired file and
        print(f.read())                                           # proceed the read off of the file and print it to the
        input("Click enter to go back...")                        # user. The use of if statements and elif allows the
        locationgoback(locationchoice)                            # the function to select the right option and print it
    elif locationchoice in ["2", "Italy"] and userchoice == "1":
        f = open("ItalyInformation/ItalyCulture.txt", "r")
        print(f.read())
        locationgoback(locationchoice)
    elif locationchoice in ["3", "Greece"] and userchoice == "1":
        f = open("GreeceInformation/GreeceCulture.txt", "r")
        print(f.read())
        input("Click enter to go back...")
        locationgoback(locationchoice)

    elif locationchoice in ("1", "America") and userchoice == "2":
        f = open("AmericaInformation/AmericaPhrases.txt", "r")
        print(f.read())
        input("Click enter to go back...")
        locationgoback(locationchoice)
    elif locationchoice in ["2", "Italy"] and userchoice == "2":
        f = open("ItalyInformation/ItalyPhrases.txt", "r")
        print(f.read())
        goback = input("Click enter to go back or input a number...")
        while goback != "":
            if goback == "1":
                winsound.PlaySound('IPlease.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "2":
                winsound.PlaySound('IThank you.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "3":
                winsound.PlaySound('IYour welcome.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "4":
                winsound.PlaySound('IGood Morning.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "5":
                winsound.PlaySound('IGood Evening.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "6":
                winsound.PlaySound('IBuy.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "7":
                winsound.PlaySound('IYes.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "8":
                winsound.PlaySound('INo.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "9":
                winsound.PlaySound('ICiao.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "10":
                winsound.PlaySound('II Love Italy', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            else:
                print("You're option is not valid please try again")
                goback = input("Click enter to go back or input a number...")
        locationgoback(locationchoice)
    elif locationchoice in ["3", "Greece"] and userchoice == "2":
        f = open("GreeceInformation/GreecePhrases.txt", encoding="utf8")
        print(f.read())
        goback = input("Click enter to go back or input a number...")
        while goback != "":
            if goback == "1":
                winsound.PlaySound('GHello.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "2":
                winsound.PlaySound('GHow Are You.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "3":
                winsound.PlaySound('GGood Morning.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "4":
                winsound.PlaySound('GGood Night.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "5":
                winsound.PlaySound('GPlease.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "6":
                winsound.PlaySound('GGoodbye.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "7":
                winsound.PlaySound('GYes.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "8":
                winsound.PlaySound('GNo.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "9":
                winsound.PlaySound('GSorry.wav', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
            elif goback == "10":
                winsound.PlaySound('GI Love Greece', winsound.SND_FILENAME)
                goback = input("Click enter to go back or input a number...")
        locationgoback(locationchoice)

    elif locationchoice in ("1", "America") and userchoice == "3":
        f = open("AmericaInformation/AmericaDos.txt", "r")
        print(f.read())
        input("Click enter to go back...")
        locationgoback(locationchoice)
    elif locationchoice in ["2", "Italy"] and userchoice == "3":
        f = open("ItalyInformation/ItalyDos.txt", "r")
        print(f.read())
        input("Click enter to go back...")
        locationgoback(locationchoice)
    elif locationchoice in ["3", "Greece"] and userchoice == "3":
        f = open("GreeceInformation/GreeceDos.txt", "r")
        print(f.read())
        input("Click enter to go back...")
        locationgoback(locationchoice)
    # Maingoback and locationgoback are 2 different functions that allows the user to go back to the previous state to
    # Reselect or change their different inputs
    elif locationchoice in ("1", "America") and userchoice == "4":
        maingoback()
    elif locationchoice in ["2", "Italy"] and userchoice == "4":
        maingoback()
    elif locationchoice in ["3", "Greece"] and userchoice == "4":
        maingoback()
    else:
        while userchoice != "1" or "2" or "3" or "4" or "America" or "Greece" or "Italy":
            print("Not a valid choice, please try again")
            userchoice = input("What do you want to learn?: ")
            selection(locationchoice, userchoice)


def maingoback():  # Maingoback is a function that takes the user back to the main menu from the location screens
    main_menu()
    locationchoice = input("Where do you want to go?: ")
    while locationchoice >= "6":
        print("Wrong choice please try again!!!")
        locationchoice = input("Where do you want to go:?")

    if locationchoice == "1":
        america()
    elif locationchoice == "2":
        italy()
    elif locationchoice == "3":
        greece()
    elif locationchoice == "4":
        help()
    elif locationchoice == "5":
        Exit()
    userchoice = input("What are we learning about today?: ")
    selection(locationchoice, userchoice)


def locationgoback(locationchoice):  # Locationgoback takes the user from the information back to the location menu
    location(locationchoice)
    userchoice = choice()
    selection(locationchoice, userchoice)


# This starts and runs the main program and starts the user off in exploring the application
main_menu()
locationchoice = input("Where do you want to go?: ")
while locationchoice >= "6":
    print("Wrong choice please try again!!!")
    locationchoice = input("Where do you want to go:?")
location(locationchoice)
userchoice = choice()
selection(locationchoice, userchoice)
