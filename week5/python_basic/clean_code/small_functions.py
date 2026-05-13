def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not valid_user_email(user_email):
        print("Invalid email")
        return None
    
    if not positive_quantity(quantity) or not exsist_in_stock(quantity, stock):
        if not positive_quantity(quantity):
            print("You must enter a positive value")
        else:
            print(f"No more {product_name} in our stock")
        return None

    price = product_price * quantity
    if quantity >= 50:
        price = discount(quantity, price)

    stock -= quantity

    order_status = "confirmed"
    
    print(f"Order {order_status}: {user_email} bought {quantity}x {product_name} for ${price}")
    return user_email, product_name, quantity, price, order_status

def valid_user_email(user_email):
    return bool(user_email)

def positive_quantity(quantity):
    return quantity > 0

def exsist_in_stock(quantity, stock):
    return quantity < stock

def discount(quantity, price):
    return price * 0.9 if quantity >= 10 else price * 0.85