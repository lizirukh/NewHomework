# დავალება 1
# int_list = [10,20,30,40]

# def add_element(x):
#     int_list.append(x)
#     print(int_list)

# add_element(79)

# მეორე ამოხსნა
# def add_element2():
#     int_list.append(int(input('შეიყვანეთ რიცხვი: ')))
#     print(int_list)

# add_element2()

#####################################################

# დავალება 2

# sum = 0

# def sum_of_digits(number):
#     if number == 0:
#         return sum
#     else:
#         sum += sum_of_digits(number // 10) 

# print(sum_of_digits(12345))
    
# დავალება 3
# rev_word = ''

# def rev_str(word):
#     if rev_word == reversed(word):
#         return word, rev_word
#     else:
#         rev_str(reversed(word))

# print(rev_str('Hello'))

# davaleba 4
# lst = [0, 1]

# def fibonacci(n):
#     # lst.append[fibonacci(n-2) + fibonacci(n-1)]
#     if n <= 1:
#         return n
#     else: 
        
#         return fibonacci(n-2) + fibonacci(n-1)
    
# print(fibonacci(8))