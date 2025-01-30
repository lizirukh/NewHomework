from homework import session, Product, CartItems, Order, OrderItem
from datetime import datetime

products = session.query(Product).all()
#
# print(products)

for product in products:
    print(product.id, product.name, product.price)

# product1 = Product("Cap", 15.0, 15)
# product2 = Product("Shirt", 22.0, 12)
# product3 = Product("Magnet", 4.0, 25)
# product4 = Product("Hoodie", 27.0, 10)
# product5 = Product("Poster", 3.0, 20)
# product6 = Product("Sticker", 1.5, 50)
#
#
# products = [product1, product2, product3, product4, product5]
#
# session.add_all(products)
# session.commit()


cartItems = session.query(CartItems).all()
#
# print(cartItems)

def addToCart(product_id, quantity):
    session.add(CartItems(product_id, quantity))
    session.commit()

def viewCart():
    join_products = session.query(CartItems, Product).join(Product, CartItems.product_id == Product.id).all()
    # print(join_products)
    for cart_items, product, in join_products:
        print(f'{cart_items.id}. Product name - {product.name} Quantity - {cart_items.quantity}')


