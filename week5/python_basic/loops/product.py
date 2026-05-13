products_list = []
while True:
    product = input("Enter a product (or 'done' to finish): ")
    if product.lower() == "done":
        break
    products_list.append(product)

print(products_list)
