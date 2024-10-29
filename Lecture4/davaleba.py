# davaleba 1
text = input("შეიყვანეთ ტექსტი:")  

x = -1

for i in range(len(text) // 2):
    if text[i] != text[x]:
        is_palindrome = False
        break
    else:
        x -= 1
        is_palindrome = True
        continue
print("Text is palindrome" if is_palindrome else 'Text is not palindrome')      
#---------------------------------------------------------------

#davaleba 2

text = input('Enter text:')

for i in range(len(text)-1):
    print(ord(text[i]))



