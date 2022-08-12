
product_dict = {}
sum_values = 0
command = input()
while command != "statistics":
    data_info = command.split(": ")
    product = data_info[0]
    quantity = int(data_info[1])

    if product not in product_dict:
        product_dict[product] = quantity
    else:
        product_dict[product] += quantity
    command = input()

print("Products in stock:")
for key, values in product_dict.items():
    sum_values += int(values)
    print(f"- {key}: {values}")
print(f"Total Products: {len(product_dict)}")
print(f"Total Quantity: {sum_values}")
