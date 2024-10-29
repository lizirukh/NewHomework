#davaleba 1

num = int(input('Enter number:'))

while num > 0:
    print(num)
    num-=1
#--------------------------------------------------

#davaleba 2

total_sum = 0

while True:
    symbol = input("შეიყვანეთ სიმბოლო: ")
    if symbol == 'sum':
        print(total_sum)
        break
    else:
        number = int(symbol)
        if number > 0:
            total_sum += number
#--------------------------------------------------

#davaleba 3
from random import randint

random_integer = randint(1,5)
lives = 5

while lives > 0:
    number = int(input('Enter number: '))
    if random_integer == number: 
        print('რიცხვები დაემთხვა.')
        break
    if number > random_integer:
        print('მომხმარებლის მიერ შეყვანილი რიცხვი მეტია')
    else:
        print('მომხმარებლის მიერ შეყვანილი რიცხვი ნაკლებია')
    lives-=1
else:
    print("სიცოცხლეების რაოდენობა ამოიწურა.")


        
    
    