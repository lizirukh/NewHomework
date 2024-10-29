# დავალება 1
# import string
# import random

# def write_sentences(file_name, num_lines, content):
#     with open(file_name, 'w+') as file:
#         for _ in range(num_lines):
#             line = content()
#             file.write(line + '\n')
#         # file.close()
        
#        # print(file.readable())
#     # return file_name.readlines()
#     # f = file_name.open()
#     # return file_name.readlines()

# def content():
#     letters = string.ascii_lowercase
#     return ( ''.join(random.choice(letters) for i in range(0, 1000)) )

# def read_lines(filename):
#     with open(filename, 'r') as f: 
#         lines = f.readlines()
#     return lines    

# write_text = write_sentences('text.txt', 1000, content)
# # print(f'The length of the sentences is {len(read_lines('text.txt'))}')
# print(f"Length of the list is {len(read_lines('text.txt'))}")

# # read_file = open('text.txt', 'r')
# # print(rea)
# # print(f'The number of lines in text.txt is {len(write_sentences('text.txt', 1000, content).writelines())}')

###########################

# დავალება 2
# dict = {2: 'second', 8: 'eighth', 10: 'tenth', 13: 'thirteenth', 17: 'seventeenth'}

# with open('file2.txt', 'a') as file:
#     for i in range(1, 18):
#         if i in dict:
#             file.write(f'{dict[i]} \n')
#         else: 
#             file.write('\n')       

############################

# დავალება 3

# new_file = open('new_file.txt', 'r+')
# with open('test.txt', 'r') as file:
#     with open('file2.txt', 'r') as file1:
#         with open('new_file.txt', 'w') as new_file:
#             new_file.writelines(file.readlines() + file1.readlines())
#         # new_file.writelines(file.readlines() + file1.readlines())

# new_file = open('new_file.txt', 'r')
# print(new_file.read())

# new_file.close()

#########################################


