print("Atm program...")
input()
print("Welcome to bankworld!")
print("Insert your card below")
pin = int(input("enter your pin to proceed: "))

atm_pin = 9999
transaction = ["balance enquiry", "withdraw money", "deposit", "change your pin", "transfer money", "quit"]
if pin == 9999:
    print("choose your transaction: ")
    print("1. balance enquiry")
    print("2. withdraw money")
    print("3. deposit")
    print("4. change your pin")
    print("5. transfer money")
    print("6. quit")
    trans = input("enter transaction: ")
    if trans == "balance enquiry":
        slip = input("do you want slip? ")
        if slip == "yes":
            print("here is your slip. Thanks for using bankworld!")
        else:
            print("Thanks for using bankworld")
    elif trans == "withdraw money":
        amount = float(input("enter amount to proceed: "))
        if amount > 0:
            print("collect your cash. Thanks for using bankworld!")
        else:
            print("enter valid amount to proceed")
    elif trans == "deposit":
        deposit = float(input("enter amount to be deposited: "))
        if deposit > 0:
            print("your deposit was succesful. Thanks for using bankworld!")
        else:
            print("enter valid amount to proceed")
    elif trans == "change your pin":
        change_pin = float(input("enter new pin: "))
        if change_pin >= 0:
            print("your pin has been changed successfully. Thanks for using with bankworld!")
        else:
            print("enter valid pin to proceed.")
    elif trans == "transfer money":
        transfer_money = float(input("enter amount to be transfered: "))
        if transfer_money > 0:
            print("your money has been transfered successfully. Thanks for using bankworld!")
        else:
            print("enter valid amount to proceed.")
    elif trans == "quit":
        quit = input("press 'yes' to quit!")
        if quit == "yes":
            print("quit")
        else:
            print("choose any transaction please: ")

else:
    print("wrong pin, try again!")

input("press enter to exit program")