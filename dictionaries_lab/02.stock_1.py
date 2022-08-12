products = input().split()

products_dict = {}
for element in range(0, len(products), 2):
    products_dict[products[element]] = int(products[element + 1])

searched_product = input().split()

for searched_element in searched_product:
    if searched_element in products_dict:
        print(f"We have {products_dict[searched_element]} of {searched_element} left")
    else:
        print(f"Sorry, we don't have {searched_element}")