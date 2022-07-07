input_products = input().split()

bakery_dict = {}

for i in range(0, len(input_products), 2):
    key = input_products[i]
    value = int(input_products[i + 1])
    bakery_dict[key] = value
print(bakery_dict)