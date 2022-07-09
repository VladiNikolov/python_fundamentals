resource_dict = {}

command = input()
while not command == "stop":
    quantity = int(input())
    if command in resource_dict.keys():
        resource_dict[command] += quantity
    else:
        resource_dict[command] = quantity

    command = input()
for key, value in resource_dict.items():
    print(f"{key} -> {value}")
