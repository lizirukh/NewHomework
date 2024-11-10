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
            return # და უბრალოდ ვწერთ return-ს რომ გამოვიდეს if-იდან 
        
        last_node = self.head  # არ ვიცით ბოლო ელემენტი რა არის, ამიტომ last_node-ს ვანიჭებთ head-ს
        while last_node.next: # სანამ last_node-ის next-ი none არ არის
            last_node = last_node.next # last_node-ს ვანიჭებთ last_node-ის next-ს
        last_node.next = new_node # ესე ვპოულობთ ბოლო ელემენტს, რომლის next-იც ცარიელია ანუ none-ია, და იქ ვამატებთ new node-ს

    def remove_at(self, index):
        if index < 0 or self.head is None:
            return 
        
        if index == 0:
            self.head = self.head.next
            return 

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

linked_list = LinkedList()

linked_list.append(50)
linked_list.append(87)
linked_list.append(20)
linked_list.append(25)
linked_list.append(11)
linked_list.append(5)

linked_list.display()