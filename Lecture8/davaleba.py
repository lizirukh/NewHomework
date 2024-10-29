# დავალება 1
# def is_anagram(word1, word2):
#     dict1 = {}
#     dict2 = {}
#     word1 = word1.lower()
#     word2 = word2.lower()
#     bool_var = False
#     for i in range(0, len(word1)):
#         if word1[i] not in dict1:
#             dict1.setdefault(word1[i], 1)
#         else: 
#             dict1[word1[i]] += 1
#     # return dict1
#     for i in range(0, len(word2)):
#         if word2[i] not in dict2:
#             dict2.setdefault(word2[i], 1)
#         else: 
#             dict2[word2[i]] += 1
    
#     for i in dict1.items():
#         if dict1.items() == dict2.items():
#              bool_var = True

#         # if dict1[i] in dict2 and dict1[i] == dict2[i]:
#         #     dict2.pop(dict2[i])
#     return bool_var

# print('Given words are anagrams' if is_anagram('Race', 'Care') else 'Given words are not anagrams')


# დავალება 2
# def sym_counter(str, char):
#     return str.count(char)

# print(sym_counter('ananasi', 'a'))

#######################

# დავალება 3

# 0, 1, 1, 2, 3, 5, 8, 13 ...
# def fib(n):
#     if n > 1:
#         lst = [0, 1]
#         for i in range(2, n):
#             lst.append(lst[i-2] + lst[i-1])
#         return lst    
   
# n = int(input('Enter number which is greater than 1: '))   
# print(f'Fibonacci sequence for n={n} is {fib(n)}')