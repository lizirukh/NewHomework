# class BankAccount:
#     def __init__(self, account_holder, account_number, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def withdraw(self, with_amount):
#         if self.balance >= with_amount:
#             self.balance -= with_amount
#             print(f'The remaining balance for {self.account_holder}, with account number: {self.account_number} is {self.balance}')
    
#     def deposit(self, dep_amount):
#         self.balance += dep_amount
#         print(f'The remaining balance for {self.account_holder}, with account number: {self.account_number} is {self.balance}')

# person1 = BankAccount('John', '1111', 100000)
# person2 = BankAccount('Anna', '2222', 300000)
# person3 = BankAccount('Lizi', '3333', 2000000)

# person1.withdraw(1500)
# person1.deposit(12600)

# person2.deposit(4000)
# person2.withdraw(500)

# person3.withdraw(200000)
# person3.deposit(300000)

# დავალება 2
class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id,
        self.courses = courses

    def info(self):
        print(f'{self.name}\'s ID is {self.student_id}')

    def courses_method(self):
        print(f'{self.student_id} is registered on courses: {self.courses}')

student1 = Student('Lizi', 111, ['Math', "Georgian", 'Physics', 'Programming in Python'])
student2 = Student('John', 222, ['Physics', 'Calculus', 'C#'])
student3 = Student('Tekla', 333, ['Political Science', 'Georgian History', 'Academic Writing'])
student4 = Student('Lizo', 444, 'Psychology, Office Programs, English')
student5 = Student('Natia', 555, 'Economics, Macro Economics, Business English')

student1.info()
student1.courses_method()
student2.info()
student2.courses_method()
student3.info()
student3.courses_method()
student4.info()
student4.courses_method()
student5.info()
student5.courses_method()