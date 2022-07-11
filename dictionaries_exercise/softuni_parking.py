number_of_commands = int(input())
parking_dict = {}

for _ in range(number_of_commands):
    command_line = input().split()
    command = command_line[0]
    user = command_line[1]

    if command == "register":
        plate_number = command_line[2]
        if user not in parking_dict:
            parking_dict[user] = plate_number
            print(f"{user} registered {parking_dict[user]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_dict[user]}")

    elif command == "unregister":
        if user not in parking_dict:
            print(f"ERROR: user {user} not found")
        else:
            parking_dict.pop(user)
            print(f"{user} unregistered successfully")

for key, value in parking_dict.items():
    print(f"{key} => {value}")