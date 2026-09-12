#account id, account holder, account balance, account type
#functions for withdraw(check if there is sufficient balance) + deposit
class Bank_account():
    def __init__(self,number,holder,balance,type):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.type = type

    def get_number(self):
        return self.number
    def set_holder(self,holder):
        self.holder = holder
    def get_holder(self):
        return self.holder