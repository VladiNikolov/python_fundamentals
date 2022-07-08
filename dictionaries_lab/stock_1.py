products = input().split()
products_dict = {}

for element in range(0, len(products), 2):
    key = products[element]
    value = products[element + 1]
    products_dict[key] = value

searcher_product = input().split()

for current_product in searcher_product:
    if current_product not in products_dict:
        print(f"Sorry, we don't have {current_product}")
    else:
        print(f"We have {products_dict[current_product]} of {current_product} left")
