# დავალება 1
# my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]

# sum = my_list[2] + my_list[8] + my_list[13]
# print(sum)

##############################

#დავალება 2
import random

rand_list = [random.randint(1, 100) for i in range(20)]

new_list = []
print(rand_list)

for i in len(rand_list):
    if rand_list[i] % 2 != 0:
        new_list.append(rand_list[i])

# new_list.sort()
# print(new_list)

# print(f'ყველაზე მცირე: {new_list[0]}, \nყველაზე დიდი: {new_list[len(new_list)-1]}')
######################################

#დავალება 3
# my_llist = [43, '22', 12, 66, 210, ["hi"]]

# print(my_llist.index(210))

# # არ ვიცი რამდენად სწორად გავიგე პირობა, ბოლო ელემენტში ჩავამატე და არა ბოლო ელემენტად 
# my_llist[len(my_llist)-1].append('hello') 
# print(my_llist)

# ### ეს მეორე ნაირი ამოხსნა, ბოლო ელემენტის შემდეგ დამატება
# my_llist.append('hello')
# print(my_llist)


# my_llist.pop(2)
# print(my_llist)

# my_llist2 = my_llist.copy()
# # print(id(my_llist))
# # print(id(my_llist2))

# my_llist2.clear()
# print(f'my_llist: {my_llist} \nmy_llist2: {my_llist2}')

##########################################

#დავალება 4

# matrix = [
#     [1, 2, 3],
#     [3, 2, 4]
# ]

# matrix1 = [
#     [2, 6, 1],
#     [3, 2, 6]
# ]

# final_matrix = []
# temp_list = []
# temp_list2 = []

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         temp_list.append(matrix[i][j] + matrix1[i][j])
    
#     temp_list2 = temp_list.copy()
#     final_matrix.append(temp_list2)    
#     temp_list.clear()

# for x in final_matrix:
#     print(x)

##########################################

#დავალება 5
    
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         result[i][j] = matrix[j][i]
# # print(result)
            
# for m in result:
#     print(m)
#################################

#დავალება 6
# import random 

# matrix = [[random.randint(1,50) for i in range(4)] for j in range(4)]

# for m in matrix:
#     print(m)

    