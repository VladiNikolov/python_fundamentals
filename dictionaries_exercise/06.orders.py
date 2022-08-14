product_dict = {}

while True:
    command = input()
    if command == "buy":
        break
    else:
        data_info = command.split()
        product_name = data_info[0]
        product_price = float(data_info[1])
        product_quantity = int(data_info[2])

        if product_name not in product_dict:
            product_dict[product_name] = []
            product_dict[product_name].append(product_price)
            product_dict[product_name].append(product_quantity)
        else:
            product_dict[product_name][0] = product_price
            product_dict[product_name][1] += product_quantity


for key, value in product_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

