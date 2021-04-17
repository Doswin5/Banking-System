from datetime import datetime

name = input("What is your name? \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if (name in allowedUsers):
    password = input("Your Password? \n")
    userId = allowedUsers.index(name)
    dateAndTime = datetime.now()

    if (password == allowedPassword[userId]):
        print("Your Current Time and Date after you logged in is ", dateAndTime)
        print("Welcome ",name)
        print("These are the options available:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaints")

        selectedOption = int(input("Please select an option: "))

        if (selectedOption == 1):
            print("You selected ",selectedOption)
            int(input("How much would you like to withdraw? \n"))
            print("Take your cash")

        elif (selectedOption== 2):
            print("You selected ",selectedOption)
            currentBalance = int((input("How much would you like to deposit? \n")))
            print("Current Balance is: ",currentBalance)

        elif (selectedOption == 3):
            print("You selected ", selectedOption)
            input("What issue will you like to report? \n")
            print("Thank you for contacting us")

        else:
            print("Invalid option selected, please try again")

    else:
        print("Password incorrect, please try again")

else:
    print("Name not found, please try again")


