#To create a class of named BankAccount
class BankAccount:
    def __init__(self, account_number, balance=0.0):        #Taking the formal parameters
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):            #Taking the actual parameters for the deposit
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid Deposit Amount.")

    def withdraw(self, amount):                #Taking actual parameters for withdrawl
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")

    def check_balance(self):       #Checking the bank balance
        print(f"Account Balance: ₹{self.balance}")

# Creating the object 

print("Total summary of your account: ")
account = BankAccount(10000,350)
account.deposit(300)
account.withdraw(100)
account.check_balance()