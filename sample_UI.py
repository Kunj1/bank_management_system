import accounts as acnt
import signup
import sys
import login
import transaction
import updaterecords as up

print('''
......WELCOME TO VIRTUAL BANK......
published by : @abhraneel, @arijeet
Description : It is a local virtual bank management system set up
              to describe the python-mysql interface. This is our
              submission for the computer project assignment for 
              the accademic session of 2020-21 of class XII. Stay safe and healthy.
              Please do listen our explaination. Thank you
              
XXXXXXXX SPECIFICATIONS XXXXXXXXX

# Developed on : MACBOOK PRO,
                 13inches, 
                 8GB RAM, 
                 512GB internal memory,
                 MACOS mojave, 
                 intel core i5 
                 
#FRONT END : Tkinter
#MIDDLE-WARE: PYTHON
#BACKEND : MYSQL

XXXXXXXX END XXXXXXXXX

........PROGRAM BEGINS FROM HERE.......
''')
print()
print()

print('''
    WELCOME. PLEASE CHOOSE FROM THE FOLLOWING : 
    1. Login
    2.Sign Up
    3. Exit

''')

entry = int(input('enter choice : '))

if entry == 1:
    usr = int(input('enter account number:'))
    passwd = int(input('enter 4-digit passcode :'))
    login.login(usr,passwd)
    entry2 = int(input('''Choose you next action :
                1. Withdraw
                2. Deposit
                3. Update profile
                4. Temporary block account 
                5. Transfer money
                6. mini-statement 
                7.Exit
                Your choice : '''))

    if entry2 == 1:
        amount = int(input('enter amount:'))
        print(transaction.withdraw(amount,usr))

    elif entry2 == 2:
        amount = int(input('enter amount:'))
        print(transaction.deposit(amount,usr))

    elif entry2 == 3:
        field = input("enter field to be changed:")
        print(up.update_usr_rec(usr,field))

    elif entry2 == 5:
        amount = int(input('enter amount to be transferred:'))
        child = int(input('enter acount number to be transfered too:'))
        print(transaction.transfer(amount,usr,child))

    elif entry2 == 6:
        tid = input('enter transaction id:')
        print(transaction.get_history(tid))

    elif entry2 == 7:
        sys.exit(0)

elif entry == 2:
    signup.signup()

else:
    print("Thank you and have a great day. Bye")
    sys.exit(0)



















