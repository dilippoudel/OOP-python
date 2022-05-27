# Non OOP
# Bank 2
# Single Account
accountName = ''
accountBalance = 0
accountPassword = ''


# Creating account

def newAccount(name, balance, password):
    global accountName, accountPassword, accountBalance
    accountName = name
    accountBalance = balance
    accountPassword = password

    def show():
        global accountName, accountPassword, accountBalance
        print(f'    Name: {accountName}'
              f'    Balance: {accountBalance}'
              f'    password: {accountPassword}')
        print()


def getBalance(password):
    global accountName, accountPassword, accountBalance
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountPassword, accountBalance
    if amountToDeposit < 0:
        print('You can not deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect password')
        return None
    accountBalance += amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountPassword, accountBalance
    if amountToWithdraw < 0:
        print('You cant withdraw negative amount.')
        return None
    if password != accountPassword:
        print('Password Incorrect')
        return None
    if amountToWithdraw > accountBalance:
        print('You can not withdraw more than you have in your account')
        return None

    accountBalance -= amountToWithdraw
    return accountBalance


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
