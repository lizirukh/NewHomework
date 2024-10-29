# დავალება 1
# squared_numbers = set()

# for i in range(1,11):
#     squared_numbers.add(i**2)
# print(squared_numbers)

# list comprehension
# squared_numbers = set(i**2 for i in range(1, 11))
# print(squared_numbers)
############################################

# დავალება 2
# word = set(input())

# print(word)

#########################

# დავალება 3
# tuple1 = (1,2,3,4,5,6)
# tuple2 = (4,5,5,6,6,7)

# combined_tuple = set(tuple1 + tuple2)
# print(combined_tuple)

# tuple_union = tuple1 + tuple2
# duplicated_values = []
# counter = 1

# ამოხსნა Set-ის გარეშე
# for i in range(0, len(tuple_union)):
#     if tuple_union[i] not in duplicated_values:
#         for j in range(i+1, len(tuple_union)):
#             if tuple_union[i] == tuple_union[j]:
#                 counter += 1
#                 if counter > 1:
#                     duplicated_values.append(tuple_union[i])
#                     counter = 1
#                     break
# print(duplicated_values)

# ამოხსნა Set-ით
# for i in range(0, len(tuple_union)):
#     for j in range(i+1, len(tuple_union)):
#         if tuple_union[i] == tuple_union[j]:
#             counter += 1
#             if counter > 1:
#                 duplicated_values.append(tuple_union[i])
#                 counter = 1
#                 break
# print(set(duplicated_values))

######################################################

# დავალება 4

# tuple1 = (1, 2, 3, 4)
# temp = 0

# rev_lst = list(tuple1)
# temp = rev_lst[0]
# rev_lst[0] = rev_lst[-1]
# rev_lst[-1] = temp

# reversed_tuple = tuple(rev_lst)
# print(reversed_tuple)
#############################

# დავალება 5
tuple1 = (1, (2, 3), (4, (5, 6)))
lst = list(tuple1)
result_lst = []
print(lst)
for i in range(0, len(lst)):
    if isinstance(lst[i], tuple):
        result_lst.append(list(lst[i]))
    else:
        result_lst.append(lst[i])
for j in range(0, len(result_lst)):
    if isinstance(result_lst[j], tuple):
        result_lst[j] = list(result_lst[j])
    else:
        result_lst[j] = result_lst[j]
for m in range(0, len(result_lst)):
    if isinstance(result_lst[m], tuple):
        result_lst[m] = list(result_lst[m])
    else:
        result_lst[m] = result_lst[m]
print(result_lst)


