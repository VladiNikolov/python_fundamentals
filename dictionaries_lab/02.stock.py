products = input().split()

product_dict = {}
for element in range(0, len(products), 2):
    key = products[element]
    value = products[element + 1]
    product_dict[key] = int(value)
searched_product = input().split()
for product in searched_product:
    if product in product_dict:
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


