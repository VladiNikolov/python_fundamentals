orders_dict = {}
sum = 1
command = input()
while command != "buy":
    current_command = command.split()
    name = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])
    if name in orders_dict:
        orders_dict[name][0]= price
        orders_dict[name][1] += quantity
    else:
        orders_dict[name] = []
        orders_dict[name].append(price)
        orders_dict[name].append(quantity)

    command = input()
for key, value in orders_dict.items():
    sum = 1
    for i in value:
        sum *= i
    print(f'{key} -> {sum:.2f}')


