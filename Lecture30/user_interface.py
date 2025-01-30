from homework_orm import cartItems, addToCart, viewCart

print(f'Pick a number: \n'
      f'1: View Cart \n'
      f'2: Add to cart \n'
      f'3: Delete products from cart \n'
      f'4: Make order \n'
      f'5: View Orders \n')

x = int(input("Enter number here: "))


def managingOrders(x):
    match x:
        case 1:
            viewCart()
        case 2:
            product_id = int(input("Enter product id: "))
            quantity = int(input("Enter quantity: "))
            addToCart(product_id, quantity)
        case 3:

            pass
        case 4:
            pass
        case 5:

            pass


managingOrders(x)