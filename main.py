import os

from Bank import *

fileName = __file__
print('Hello there .....', dir(fileName))
print(os.path)

oBank = Bank('9-5', 'Hakaniemenranta 12B', '555-5555')
oAccNum = oBank.createAccount('Joe', 100, 'JoesPassword')
print("Joe's account number is:", oAccNum)
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action.lower()
    action = action[0]
    print()
    try:
        if action == 'b':
            oBank.balance()
        elif action == 'd':
            oBank.deposit()
        elif action == 'o':
            oBank.openAccount()
        elif action == 's':
            oBank.show()
        elif action == 'q':
            break
        elif action == 'w':
            oBank.withdraw()
        elif action == 'c':
            oBank.closeAccount()
    except AbortTransaction as error:
        print(error)

print('DONE')


