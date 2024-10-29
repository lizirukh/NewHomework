#დავალება 1
# txt = input('Text...')
# dict = {}

# for i in txt.split():
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)
##############################

#დავალება 2

##############################

#დავალება 3
# dict = dict([(i, i*i) for i in range(1,11)])
# print(dict)

##############################

#დავალება 4
departments = {
        "accountant": {
            1: {'name': "Nino", "lastname": 'Gvenetadze', "age": 54, "salary": 4500},
            2: {'name': "Lali", "lastname": 'Nikolaishvili', "age": 53, "salary": 4200},
            3: {'name': "Marina", "lastname": 'Eristavi', "age": 61, "salary": 5000}
        },
        "programming": {
            4: {'name': "Salome", "lastname": 'Chikovani', "age": 23, "salary": 4500},
            5: {'name': "Giorgi", "lastname": 'Topuria', "age": 24, "salary": 4630},
            6: {'name': "Sandro", "lastname": 'Vachnadze', "age": 27, "salary": 5000},
        },
        "HR": {
            6: {'name': "Liza", "lastname": 'Tsereteli', "age": 24, "salary": 3500},
            7: {'name': "Natia", "lastname": 'Tsotskolauri', "age": 26, "salary": 2900},
            8: {'name': "Mariam", "lastname": 'Laitadze', "age": 54, "salary": 4500},
        }
    }

sum = 0
num = 0

for key, value in departments.items():
    for key1, value1 in value.items():
        for key2, value2 in value1.items():
            if key == "accountant":                 
                if key2 == "salary":
                    sum += value1['salary']
                    num += 1
        # print(f'Accountants - : {sum/num}')
                    

                    
                