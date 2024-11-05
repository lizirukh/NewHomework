from multipledispatch import dispatch

class Person:
    deposit = 1000
    loan = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}\'s deposit is {self.deposit} and loan is {self.loan}.'

class House:
    def __init__(self, ID, price, owner, status):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    @dispatch(str)
    def sell_house(self, buyer):
        person2.deposit += house.price
        house.owner = buyer
        house.status = 'Sold'
        return f'The deposit of seller - {person2.name} has increased by {house.price}. \nThe new house owner is {person1.name}.\nThe new status of the house is {house.status}'

    @dispatch(str, int)
    def sell_house(self, buyer, loan_amount):
        person2.deposit += house.price
        house.owner = buyer
        house.status = 'Sold with loan'
        person1.loan += loan_amount
        return f'The deposit of seller - {person2.name} has increased by {house.price}. \nThe new house owner is {person1.name}.\nThe new status of the house is {house.status} \nThe buyer\'s loan was increased by {person1.loan}.'

person1 = Person('Brian')
person2 = Person('Jackie')
house = House('15D', 800000, 'Jackie', 'For Sale')
print(person1)
print(person2)
# print(house.sell_house('Brian'))

print(house.sell_house('Brian', 400000))