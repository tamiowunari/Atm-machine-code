import time

print("......................................................ATM program....................................................")
input("press ENTER to continue")
print("")
print("WELCOME TO GTBANK!")
print("")
print("Insert your card -->")
pin = int(input("enter your pin to proceed: "))

atm_pin = [9999, 7777, 8401, 4545]
transaction = ["balance enquiry", "withdraw money", "deposit", "change your pin", "transfer money", "quit"]
print("")
print("     Processing...")
time.sleep(3)
print("")
if pin in atm_pin:
    print("choose your transaction: ")
    print("1. balance enquiry")
    print("2. withdraw money")
    print("3. deposit")
    print("4. change your pin")
    print("5. transfer money")
    print("6. quit")
    trans = int(input("enter transaction: "))
    print("")
    print("     Processing...")
    time.sleep(3)
    if trans == 1:
        print("")
        print("1. YES  or  2. NO")
        slip = int(input("do you want slip? "))
        if slip == 1:
            print("Here is your slip...")
            print("Thanks for banking with us at GTbank!")
        else:
            print("")
            print("Thanks for banking with us at GTbank!")
    elif trans == 2:
        print("")
        amount = float(input("enter amount to proceed: "))
        print("")
        print("     Processing...")
        time.sleep(3)
        if amount > 0:
            print("")
            print("collect your cash. Thanks for banking with us at GTbank!")
        else:
            print("")
            print("enter valid amount to proceed")
    elif trans == 3:
        print("")
        deposit = float(input("enter amount to be deposited: "))
        print("")
        print("     Processing...")
        time.sleep(4)
        if deposit > 0:
            print("")
            print("your deposit of $%d.00 was successful!" %deposit)
            print("Thanks for banking with us at GTbank!")
        else:
            print("")
            print("enter valid amount to proceed")
    elif trans == 4:
        print("")
        old_pin = float(input("enter present pin: "))
        change_pin = float(input("enter new pin: "))
        if change_pin >= 0:
            print("")
            print("your pin has been changed successfully!")
            print("Thanks for banking with us at GTbank!")
        else:
            print("")
            print("enter valid pin to proceed.")
    elif trans == 5:
        print("")
        transfer_money = float(input("enter amount to be transfered: "))
        account_name = input("enter recipient's account name: ")
        account_no = input("enter recipient's account number: ")
        print("")
        print("     Processing...")
        time.sleep(5)
        if transfer_money > 0:
            print("")
            print("The sum of $%d.00 has been transfered successfully to Mr/Mrs %s" %(transfer_money,account_name))
            print("Thanks for banking with us at GTbank!")
        else:
            print("")
            print("enter valid amount to proceed.")
    elif trans == 6:
        print("")
        print("1. YES  or  2. NO")
        quit = float(input("To quit: "))
        if quit == 1:
            print("     QUIT")
        else:
            print("")
            print("Restart program and choose a valid transaction please!")

else:
    print("")
    print("wrong pin, TRY AGAIN!")
print("")
input("press ENTER to end transaction")