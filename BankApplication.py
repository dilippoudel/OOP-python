# Non OOP version
# Single Account
name = 'Dilip Poudel'
password = 'hello123'
balance = 2000

while True:
    print()
    print('press b to get the balance')
    print('press d to get the deposit')
    print('press w to get the withdraw')
    print('press s to show the account')
    print('press q to quit')
    print()
    action = input('What do you want to do? ')
    action.lower()
    action = action[0]
    print()
    if action == 'b':
        print('Get balance')
        userPassword = (input('Enter your user password: '))
        if password == userPassword:
            print(f'Your balance is {balance}')
        else:
            print('Incorrect password')
    elif action == 'd':
        print('Deposit')
        userDepositAmount = int(input('Please enter the amount you want to deposit: '))
        userPassword = input('Please enter your password: ')
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount')
        elif userPassword != password:
            print('Incorrect password')
        else:
            balance += userDepositAmount
            print(f'CONGRATS! DEPOSIT SUCCESS! \nYour new balance is {balance}')

    elif action == 's':
        print('Show:')
        print(f'       Name {name}'
              f'       Balance: {balance}'
              f'       Password: {password}'
              f'')

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = int(input('Please enter the amount to withdraw: '))
        userPassword = input('Please enter the password: ')
        if userWithdrawAmount < 0:
            print('You cant withdraw negative amount.')
        elif userPassword != password:
            print('Incorrect password for this account.')
        elif userWithdrawAmount > balance:
            print('You can not withdraw more than in your account')
        else:
            balance -= userWithdrawAmount
            print(f'Your new balance is: {balance}')
    print('Done')
