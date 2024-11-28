# დავალება 1
import json
import threading

products = {
    'technology': {
        'laptops': {
            1001: {'brand': 'Apple', 'price': 6000, 'quantity': 2},
            1002: {'brand': 'HP', 'price': 2000, 'quantity': 10}
        },
        'phones': {
            2001: {'brand': 'Apple', 'price': 5000, 'quantity': 5},
            2002: {'brand': 'Samsung', 'price': 3000, 'quantity': 5}
        }
    }
}

products1 = {
    'clothes': {
        'pants': {
            3001: {'brand': 'Levi\'s', 'price': 1000, 'quantity': 2},
            3002: {'brand': 'Lee', 'price': 1000, 'quantity': 2}
        },
        'shirts': {
            4001: {'brand': 'Adidas', 'price': 5000, 'quantity': 5},
            4002: {'brand': 'Nike', 'price': 5000, 'quantity': 5}
        }
    }
}

products2 = {
    'shoes': {
        'sneakers': {
            5001: {'brand': 'Converse', 'price': 75, 'quantity': 5},
            5002: {'brand': 'Adidas', 'price': 100, 'quantity': 10}
        },
        'heels': {
            6001: {'brand': 'Steve Madden', 'price': 80, 'quantity': 5},
            6002: {'brand': 'Alohas', 'price': 250, 'quantity': 8}
        }
    }
}


def serialization_and_reading(filename, dct):
    filename = filename + '.json'
    with open(filename, 'w') as json_file:
        json_products = json.dump(dct, json_file, indent=4)
        # print(f'The filename is: {filename} n/ ')

    with open(filename, 'r') as json_file1:
        print(f'The file name is: {filename}\n{json_file1.read()}')

technology = threading.Thread(target=serialization_and_reading, args=('products', products))
clothes = threading.Thread(target=serialization_and_reading, args=('products1', products1))
shoes = threading.Thread(target=serialization_and_reading, args=('products2', products2))

technology.start()
clothes.start()
shoes.start()

technology.join()
clothes.join()
shoes.join()