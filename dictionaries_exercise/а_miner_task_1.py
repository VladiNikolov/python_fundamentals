resource_dict = {}

command = input()
while command != "stop":
    current_resource = command
    quantity = int(input())
    if current_resource not in resource_dict:
        resource_dict[current_resource] = quantity
    else:
        resource_dict[current_resource] += quantity
    command = input()

for key in resource_dict.keys():
    print(f"{key} -> {resource_dict[key]}")
