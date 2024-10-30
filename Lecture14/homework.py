class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, with_amount):
        if self.balance >= with_amount:
            self.balance -= with_amount
            print(f'The remaining balance for {self.account_holder}, with account number: {self.account_number} is {self.balance}')
    
    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f'The remaining balance for {self.account_holder}, with account number: {self.account_number} is {self.balance}')

person1 = BankAccount('John', '1111', 100000)
person2 = BankAccount('Anna', '2222', 300000)
person3 = BankAccount('Lizi', '3333', 2000000)

person1.withdraw(1500)
person1.deposit(12600)

person2.deposit(4000)
person2.withdraw(500)

person3.withdraw(200000)
person3.deposit(300000)