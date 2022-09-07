class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, money):
        self.balance += money
        print(f"You have deposed {money} tg")
    
    def withdraw(self, money):
        self.balance -= money
        print(f"You have withdraed {money} tg")
    
    
Account1 = Account("Marat")
Account1.deposit(500000)
Account1.withdraw(100000)

print(Account1.balance)