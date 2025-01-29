from homework import session, Product, CartItems, Order, OrderItem
from datetime import datetime

# products = session.query(Product)
#
# print(products)

product1 = Product("Cap", 15.0, 15)
product2 = Product("Shirt", 22.0, 12)
product3 = Product("Magnet", 4.0, 25)
product4 = Product("Hoodie", 27.0, 10)
product5 = Product("Poster", 3.0, 20)

products = [product1, product2, product3, product4, product5]

session.add_all(products)
session.commit()



