product_dict = {}

while True:
    command = input()
    if command == "statistics":
        break

    data_info = command.split(": ")
    product_name = data_info[0]
    product_quantity = int(data_info[1])

    if product_name not in product_dict:
        product_dict[product_name] = product_quantity
    else:
        product_dict[product_name] += product_quantity

print(f"Products in stock:")
for key, value in product_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(product_dict.keys())}")
print(f"Total Quantity: {sum(product_dict.values())}")