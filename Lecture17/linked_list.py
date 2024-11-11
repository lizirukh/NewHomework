class Node:
    def __init__(self, data=None): 
        self.data = data  # data-ს ვანიჭებთ მოცემულ მონაცემს
        self.next = None # next-ს კი defauld-ად ვტოვებთ ცარიელს რადგან არ 
        #ვიცით ექნება თუ არა შემდეგი ელემენტი 

class LinkedList:
    def __init__(self):
        self.head = None  # თავიდან ვქმნით ცარიელ head-ს
    
    def append(self, data):  
        new_node = Node(data) # ვქმნით ახალ Node-ის ობიექტს 
        if self.head is None: ## თუ head-ი ცარიელია,  
            self.head = new_node ## head-ს ვანიჭებთ ახალ შექმნილ ობიექტს
            return # და უბრალოდ ვწერთ return-ს რომ გამოვიდეს append მეთოდიდან
        
        last_node = self.head  # არ ვიცით ბოლო ელემენტი რა არის, ამიტომ last_node-ს ვანიჭებთ head-ს
        while last_node.next: # სანამ last_node-ის next-ი none არ არის
            last_node = last_node.next # last_node-ს ვანიჭებთ last_node-ის next-ს
        last_node.next = new_node # ესე ვპოულობთ ბოლო ელემენტს, რომლის next-იც ცარიელია ანუ none-ია, და იქ ვამატებთ new node-ს

    def remove_at(self, index): 
        if index < 0 or self.head is None:  # თუ ინდექსი არის ნოლზე ნაკლები ან head არის ცარიელი 
            return # return-ით ვაჩერებთ მეთოდს რომ მის მერე არსებული ლოგიკა აღარ ამოქმედდეს
        
        if index == 0: # განვიხილავთ იმ ვარიანტს რომელშიც ინდექსი ნულია
            self.head = self.head.next # წაშლის მაგივრად ხდება გადაწერა linked list-ებში, და პირველ ინდექსზე მყოფ ელემენტს უბრალოდ ვანიჭებთ შემდეგი ელემენტის მონაცემს
            return 
        
# მაშინ როცა ინდექსი ნოლზე მეტია და გვჭიდება მოძებნა ელემენტის, ინდექსის მიხედვით, საწყის ელემენტად ვირჩევთ ჰედს. და საწყის ინდექსის პოზიციად ნოლს. 
        current_node = self.head
        current_position = 0
# while ციკლი უნდა გაჩერდეს მაშინ როცა გადაცემული ინდექსის ელემენტს აქვს ნექსთი, და ინდექსის პოზიცია ნაკლებია 
# index - 1-ზე, რადგან უნდა ვიყოთ წინა ელემენტზე შემდეგი ელემენტის ამოსაშლელად
        while current_node.next and current_position < index - 1:
            current_node = current_node.next # უნდა ვცვალოთ ამ ცვლადის მნიშვნელობა რომ ციკლმა გააგრძელოს მოქმედება
            current_position += 1 # index-ის პოზიციაც უნდა იზრდებოდეს ერთით ყოველ ჯერზე

# თუ ინდექსი სწორად არის გადაცემული, ვდგებით წინა ელემენტზე და შემდეგს ვანიჭებთ მის შემდეგ ელემენტს
        if current_node.next:
            current_node.next = current_node.next.next
            

    def insert_at(self, index, value):
        if index < 0:
            return
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return self.head
        else:
            current_node = self.head
            current_position = 0
            while current_node and current_position < index:
                current_node = current_node.next
                current_position += 1

            new_node.next = current_node.next
            current_node.next = new_node

        # return self.head
        # current_position = 0
        # current_node = self.head

        # while current_position < index - 1:
        #     current_node.next = current_node
        #     current_position += 1

        # current_node.next = current_node
        # current_node.data = value

    def display(self):
        current_node = self.head # გამოსატანად შემოგვაქვს current_node ცვლადი, და ვანიჭებთ self.head-ს რადგან დაიბეჭდოს ბოლო ელემენტიც 
        while current_node: # სანამ current_node არსებობს..
            print(current_node.data, end=' -> ') # იქამდე გამოიტანოს current_node-ის მონაცემი და default endline-ს ვცვლით ისრით, ქვედა ხაზზე ჩამოტანის მაგივრად (რომელიც გათვალისწინებულია default-ად)
            current_node = current_node.next # current_node-ს ვანიჭებთ შემდეგი ელემენტის data-ს ანუ current_node.next-ს რომ არ მივიღოთ დაუსრულებელი ციკლი 

        print() # ვიძახებთ ცარიელ პრინტს რომ შეცვლილი endline დაუბრუნდეს თავის დეფოლტ მნიშვნელობას
linked_list = LinkedList() # ვქმნით ობიექტს რომ შევძლოთ მეთოდების გამოყენება

linked_list.append(50) # 0 # ვამატებთ ამ მონაცემებს
linked_list.append(87) # 1
linked_list.append(20) # 2
linked_list.append(25) # 3
linked_list.append(11) # 4
linked_list.append(5)  # 5

linked_list.display() # display მეთოდის გამოყენებით გამოგვაქვს მონაცემები 
# linked_list.remove_at(2) 
# linked_list.display()
# linked_list.remove_at(2) 
# linked_list.display()
# linked_list.remove_at(0) 
# linked_list.display()
# linked_list.remove_at(4)
# linked_list.display()

linked_list.insert_at(5, 70)
linked_list.display()