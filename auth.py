import random
import validation
import database
from getpass import getpass 


def init():

    
    print("Welcome to Bank Cyusa")

    

    haveAccount = int(input("Do you have an account with us? : 1 (Yes) 2 (No) \n"))

    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
            
        register()
    else:
        print("Invalid Option")
        init()

def login():
    print("**** Login into your Account ****")


    accountNumberFromUser = input("Enter your Account Number: \n")
    
    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        password = getpass("Enter Password: \n")

        user = database.authenticated_user(accountNumberFromUser, password);
        
        if user:

            bankOperation(user)

        print('Invalid Account Number or Password')
        login()

    else:

        print("Account Number Invalid: check that you have up to 10 digits and only Numbers")
        init()



def register():

    print("****** Register ******")
    email = input("Email address: \n")
    first_name = input("First Name: \n")
    last_name = input("Last Name: \n")
    password = input("Create a Password: \n")

    
    accountNumber = generatingAccountNumber()
    
    
    
    is_user_created = database.create(accountNumber, [ first_name, last_name, email, password, 0])

    if is_user_created:

        print("Your Account Has Been Created.")
        print("== ==== ======== ======== ===")
        print("Your Account number is: %d" % accountNumber)
        print("Make Sure You Keep It Safe")
        print("== ==== ======== ======== ===")

        login()

    else:

        print("Something went wrong, Please Try Again")
        register()



def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    

    selectedOption = int(input("What would you like to do?: (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
            
        depositOperation()
    elif(selectedOption == 2):
            
        withdrawalOperation()
    elif(selectedOption == 3):
           
        Logout()
    elif(selectedOption == 4):
            
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)

def withdrawalOperation():
    print('Withdrawal')

def depositOperation():
    print('Deposit Operations')


def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)

def set_current_balance(userDetails, balance):
    userDetails[4] = balance

def get_current_balance(userDetails):
    return userDetails[4]

def Logout():
    login()

### ACTUAL BANKING SYSTEM ###

init()