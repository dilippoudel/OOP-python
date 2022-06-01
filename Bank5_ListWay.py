accountList = []


def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDictionary = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountList.append(newAccountDictionary)


def show(accountNumber):
    global accountList
    print('Account', accountNumber)
    thisAccountDict = accountList[accountNumber]
    print(f'    Name: {thisAccountDict["name"]}'
          f'    Balance: {thisAccountDict["balance"]}'
          f'    Password: {thisAccountDict["password"]}')
    print()





