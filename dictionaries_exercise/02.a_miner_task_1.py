command = input()
resource_dict = {}

while command != "stop":
    quantity = int(input())
    if command not in resource_dict:
        resource_dict[command] = quantity
    else:
        resource_dict[command] += quantity

    command = input()
for keys in resource_dict:
    print(f"{keys} -> {resource_dict[keys]}")

