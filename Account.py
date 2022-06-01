# Account class
# Error indicated by raise statements
class AbortTransaction(Exception):
    pass


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount Must be the number')
        if amount <= 0:
            raise AbortTransaction('Amount Must be greater than 0.')

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Password didn\'t match')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw):
        amtToWithdraw = self.validateAmount(amountToWithdraw)
        if amtToWithdraw > self.balance:
            raise AbortTransaction('You can\'t withdraw more than in your account')
        self.balance = self.balance - amtToWithdraw
        return self.balance

    def getBalance(self, password):
        return self.password

    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()
