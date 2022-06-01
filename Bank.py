from Account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accountDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('Please enter your account number: ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if accountNumber not in self.accountDict:
            raise AbortTransaction('Your account number doesn\'t exit.')
        return accountNumber

    def getUserAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[accountNumber]
        self.askForValidAccountNumber(oAccount)
        return oAccount

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        print(theName, thePassword, theStartingAmount)
        newAccountNumber = self.nextAccountNumber
        self.accountDict[newAccountNumber] = oAccount
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print(f'Opening Account: ')
        username = input('Enter the Name: ')
        userStartingAmount = input('Enter the amount as starting balance: ')
        userPassword = input('Enter the password: ')
        userAccountNumber = self.createAccount(username, userStartingAmount, userPassword)
        print(f'Your account number is {userAccountNumber}')

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = int(input('What is your account Number: '))
        userPassword = input('Enter Password: ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print(f'You had , {theBalance} in your account, which is being to return to you.')
            del self.accountDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('GET Balance')
        userAccNumber = int(input('Enter the acc number: '))
        oAccount = self.accountDict[userAccNumber]
        userAccountPassword = input('Enter the password: ')
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is {theBalance}')

    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUserAccount()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print(f'Deposited: {theBalance}')
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** WithDraw ***')
        oAccount = self.getUserAccount()
        withdrawAmount = input('Please enter the amount: ')
        theBalance = oAccount.withDraw(withdrawAmount)
        print(f'Withdraw: {withdrawAmount}')
        print(f'your new balance is {theBalance}')

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountDict:
            oAccount = self.accountDict[userAccountNumber]
            print('    Account:', userAccountNumber)
            oAccount.show()


    def getInfo(self):
        print(f'Hours {self.hours}\n'
              f'Address: {self.address}\n'
              f'Phone: {self.phone}\n'
              f'we currently have {len(self.accountDict)}')

    def show(self):
        print('*** show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()

