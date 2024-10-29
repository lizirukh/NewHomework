# დავალება 1
# def zip_func(a,b):
#     return zip(a,b)

# print(tuple(zip_func([1, 2, 3], ['a', 'b', 'c'])))

# დავალება 2
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# res = list(filter(lambda x : x % 2== 0 , lst))

# print(res)

# დავალება 3
# lst = [-1, 3, 15, -16, -17, 8, 35, 45, -92]

# res = list(filter(lambda x : x > 0, lst))

# print(res)

# დავალება 4
# lst = ['saas', 'python', 'naaan', 'dog', 'civic']

# res = list(filter(lambda x : x == x[::-1], lst))
# print(res)

# დავალება 5
from functools import reduce

# lst = [1, 2, 3, 4, 5]
try:
    lst = [int(x) for x in input().split()]
    mult = reduce(lambda a, b: a * b, lst)
except:
    print('Please enter a valid list of integers.')
    exit()

print(mult)

