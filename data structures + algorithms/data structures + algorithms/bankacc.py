#account id, account holder, account balance, account type
#functions for withdraw(check if there is sufficient balance) + deposit
class Bank_account():
    def __init__(self,number,holder,balance,acctype):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.acctype = acctype

    def get_number(self):
        return self.number
    def set_holder(self,holder):
        self.holder = holder
    def get_holder(self):
        return self.holder
    def set_balance(self,balance):
        self.balance = balance
    def get_balance(self):
            return self.balance
    def get_acctype(self):
         return self.acctype

    def withdraw(self,amount):
        if self.balance - amount >= 0:
             self.balance -= amount
             #self.set_balance(self.balance)
        else:
             print("insufficient balance")

    def deposit(self,amount):
         self.balance += amount

person1 = Bank_account("0001","person1",211203671,"savings")
print('''option 1: check balance\noption 2: withdraw\noption 3: deposit\noption 4: exit''')
while True:
    action = input("which option do you want to choose? ")
    if action == "option 1" or action == "1":
        balance1 = person1.get_balance()
        print(f"balance: {balance1}")
    elif action == "option 2" or action == "2":
        amount = eval(input("what amount would you like to withdraw? "))
        person1.withdraw(amount)
        balance1 = person1.get_balance()
        print(f"balance: {balance1}")
    elif action == "option 3" or action == "3":
        amount = eval(input("what amount would you like to deposit? "))
        person1.deposit(amount)
        balance1 = person1.get_balance()
        print(f"balance: {balance1}")
    elif action == "option 4" or action == "4":
        break 
