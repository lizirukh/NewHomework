
class Node: 
    def __init__(self, data=None): 
        self.data = data # node კლასის ინიციალიზება
        self.next = None # next გვჭირდება იმისთვის რომ თითოეულმა ელემენტმა
        # იცოდეს მანამდე დამატებული ელემენტის ადგილმდებარეობა

class Stack: # აღვწერთ კლას Stack-ს
    def __init__(self): # საწყის ნოუდად ვქმნით top node-ს
        self.top_node = None
        self.length = 0 # სტექში შემოდის სიგრძეც და თავიდან ვანიჭებთ 0-ს

    def empty(self): # empty მეთოდი ამოწმებს stack-ის სიგრძის მიხედვით
        # ცარიელია თუ არა 
        return self.length == 0
    
    def size(self): # ეს მეთოდი უბრალოდ აბრუნებს სიგრძეს, ზომას
        return self.length
    
    def push(self, data): # ამ მეთოდს პარამეტრად გადაეცემა data, რომ ეს
        # მონაცემი ჩაამატოს 
        new_node = Node(data) # მეთოდის ამოქმედებისას ვქმნით ახალ ნოუდს
        new_node.next = self.top_node # 
        self.top_node = new_node
        self.length += 1 # ახალი ნოუდის დამატებით სიგრძე უნდა გაიზარდოს ერთით

    def pop(self):
        if not self.empty(): # თუ ცარიელი არ არის
            popped_item = self.top_node.data # ამოშლილი ინფორმაციის გამოსატანად
            # გვჭირდება მისი ცვლადში შენახვა, რომ არ დავკარგოთ 
            self.top_node = self.top_node.next 
            self.length -= 1 #როდესაც ელემენტს ამოვშლით, სიგრძესაც ვამცირებთ ერთით
            return popped_item # და ვაბრუნებთ წაშლილ ელემენტს
        else:
            raise IndexError("Stack is empty") # თუ სტექი ცარიელია, pop
        # მეთოდის გამოძახებისას გამოგვაქვს ერორი 
        
stack = Stack() # Stack ობიექტის შექმნა

print(stack.empty())
print(stack.length)

stack.push(200)
stack.push(50)
stack.push(75)
stack.push(25)
stack.push(30)

print(stack.empty())
print(stack.length)

print(stack.pop())
print(stack.empty())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.empty())
print(stack.length)
print(stack.pop())