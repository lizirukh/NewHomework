# დავალება 1
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         num = args[0]
#         if num > 0:
#             func(num)
#         else:
#             raise ValueError(f'Please, enter positive number.')
#     return wrapper


# @decorator
# def print_num(x):
#     print(f'Entered number: {x}')

# print_num(200)


# დავალება 2
# class Functor:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwds):
#         x = args[0]
#         # return [self.func(item) for item in args]
#         return self.func(x)

# def print_num(x):
#     return f'The given number is: {x}'

# functor = Functor(print_num)
# print(functor(300))

# დავალება 3
# import time

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func()
#         return "--- %s seconds ---" % (time.time() - start_time)
#     return wrapper

# @decorator 
# def print_time():
#     x = 0
#     while x < 100:
#         print(f'X is {x} and is less than 10')
#         x+=2

# print(print_time())

# დავალება 4
class LoggingMeta(type):
    def __new__(self, cls, bases, dct):
        
        instance = super().__new__(self, cls, bases, dct)
        print(f'The class name is {cls} and methods are: {dct}')
        return instance  
    
# print(type(LoggingMeta))
class Dog(metaclass=LoggingMeta):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def show_info(self):
        return f'{self.name} - {self.breed}'

    
dog1 = Dog('Jay', 'English Cocker Spaniel')
dog2 = Dog('Tulio', 'Siberian Husky')
dog3 = Dog("Molly", 'English Lab')

print(dog1.show_info())
print(dog2.show_info())
print(dog3.show_info())