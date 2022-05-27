# Non OOP
# Bank 2
# Single Account
account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''


# Creating account

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Password, account0Balance
    global account1Name, account1Password, account1Balance
    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

    def show():
        global account0Name, account0Password, account0Balance
        global account1Name, account1Password, account1Balance
        if account0Name != '':
            print(f'    Name: {account0Name}'
                  f'    Balance: {account0Balance}'
                  f'    password: {account0Password}')
        if account1Name != '':
            print(f'    Name: {account1Name}'
                  f'    Balance: {account1Balance}'
                  f'    password: {account1Password}')
            print()


def getBalance(accountNumber, password):
    global account0Name, account0Password, account0Balance
    global account1Name, account1Password, account1Balance
    if accountNumber == 0:
        if password != accountPassword:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != accountPassword:
            print('Incorrect password')
            return None
        return account1Balance


def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Password, account0Balance
    global account1Name, account1Password, account1Balance
    if accountNumber == 0:
        if amountToDeposit < 0:
            print('You can not deposit a negative amount!')
            return None
        if password != account0Password:
            print('Incorrect password')
            return None
        account0Balance += amountToDeposit
        return account0Balance
    if accountNumber == 1:
        if amountToDeposit < 0:
            print('You can not deposit a negative amount!')
            return None
        if password != account1Password:
            print('Incorrect password')
            return None
        account0Balance += amountToDeposit
        return account1Balance


def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Password, account0Balance
    global account1Name, account1Password, account1Balance
    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('You cant withdraw negative amount.')
            return None
        if password != account0Password:
            print('Password Incorrect')
            return None
        if amountToWithdraw > account0Balance:
            print('You can not withdraw more than you have in your account')
            return None

        account0Balance -= amountToWithdraw
        return account0Balance
    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('You cant withdraw negative amount.')
            return None
        if password != account1Password:
            print('Password Incorrect')
            return None
        if amountToWithdraw > account1Balance:
            print('You can not withdraw more than you have in your account')
            return None

        account1Balance -= amountToWithdraw
        return account1Balance


newAccount('Dilip', 100, 'dilip123')
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    if action == 'b':
        print('Get Balance')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f'Your balance is {theBalance}')

    elif action == 'd':
        print('Deposit')
        userDepositAmount = int(input('Please enter the amount to deposit'))
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f'Your balance is {newBalance}')
        print('Done')
