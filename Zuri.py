import random
from datetime import datetime
dateAndTime = datetime.now()

database = {}
def init():

    performTransaction = int(input("Would you like to perform a new transaction?: 1(yes). 2(No).\n"))

    if performTransaction == 1:
        welcomeMessage = ("Welcome to Dosunmu Bank")
        welcomeMessage = welcomeMessage.center(50, '*')
        print(welcomeMessage + "\n")

        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

        if (haveAccount == 1):
            print("\n")
            login()

        elif (haveAccount == 2):
            print("\n")
            register()

        else:
            print("You have selected an invalid option")

    elif performTransaction == 2:
        print("\n")
        logout()

    else:
        print("You selected an invalid option, please try again")
        init()


def register():

    print("Register".center(50, '*'))

    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create a password for yourself? \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = [firstName, lastName, email, password]

    print("Your Account has been created")
    print("== ==== ====== ==== ==")
    print(f"Your account number is: {accountNumber}")
    print("Make sure you keep it safe")
    print("== ==== ====== ==== ==")

    login()

def login():
    print("***** Login *****")
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                print(f"Your Current Time and Date after you logged in is {dateAndTime}\n\n")
                bankOperation()
            else:
                print("Invalid account number or password")
                login()
def bankOperation():
    for accountNumber, userDetails in database.items():
        feedback = "***************************************\n"
        feedback += f'Welcome {userDetails[0]} {userDetails[1]}\n'
        feedback += "***************************************\n"
        feedback += "These are the options available: \n"
        feedback += "1. Withdrawal\n"
        feedback += "2. Deposits\n"
        feedback += "3. Complaints\n"
        print(feedback)

        selectedOption = int(input("Please select an option: "))

        if (selectedOption == 1):
            print("You selected 1. Withdrawal")
            withdrawalOperation()

        elif (selectedOption== 2):
            print("You selected 2. Deposits")
            depositOperation()

        elif (selectedOption == 3):
            print("You selected 3. Complain")
            complaintOperation()

        else:
            feedback = "You selected an invalid option\n"
            feedback += "Try selecting a valid option"
            print(feedback)
            bankOperation()

def withdrawalOperation():
    withdrawalAmount = int(input("How much would you like to withdraw?\n"))
    print(f"Your withdrawal of {withdrawalAmount} was successful")
    init()

def depositOperation():
    amountToBeDeposited = int(input("How much would you like to deposit?\n"))
    print(f"Your deposit of {amountToBeDeposited} was successful")
    print(f"Your Current Balance is {amountToBeDeposited}")
    init()

def complaintOperation():
    input("What issue will you like to report? \n")
    print("Thank you for contacting us\n")
    init()



def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    feedback = "***************************************\n"
    feedback += "Thank you for banking with us\n"
    feedback += "***************************************\n"
    print(feedback)


init()