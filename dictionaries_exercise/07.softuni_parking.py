number = int(input())
parking_dict = {}

for _ in range(number):
    input_line = input().split()
    command = input_line[0]

    if command == "register":
        name = input_line[1]
        number = input_line[2]
        if name not in parking_dict:
            parking_dict[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif command == "unregister":
        name = input_line[1]
        if name not in parking_dict:
            print(f"ERROR: user {name} not found")
        else:
            del parking_dict[name]
            print(f"{name} unregistered successfully")
for key, values in parking_dict.items():
    print(f"{key} => {values}")





