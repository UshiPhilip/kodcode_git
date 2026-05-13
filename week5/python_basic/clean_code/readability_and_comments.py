TAX = 0.17
def process_cart(prices, quantities, user_type):
    # total price of all the items
    total = 0
    for i in range(len(prices)):
        price = prices[i]
        quantity = quantities[i]
        total += price*quantity
    
    # add tax
    total += total*TAX

    # descount for special users
    if user_type == 'premium':
        total = total * 0.9
    elif user_type == 'vip':
        total = total * 0.8
    
    # shiping price
    if total > 500:
        shipping = 0
    elif total > 200:
        shipping = 25
    else:
        shipping = 50
    
    # total and shiping
    total += shipping
    return total
