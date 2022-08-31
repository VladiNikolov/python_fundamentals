concert_dict = {}
time_dict = {}

while True:
    command = input()
    if command == "Start!":
        break
    else:
        data_info = command.split("; ")
        current_command = data_info[0]
        group_name = data_info[1]

        if current_command == "Add":
            member_name = data_info[2].split(", ")

            if group_name not in concert_dict:
                concert_dict[group_name] = member_name
            else:
                for element in member_name:
                    if element not in concert_dict[group_name]:
                        concert_dict[group_name].append(element)

        elif current_command == "Play":
            time = int(data_info[2])
            if group_name not in time_dict:
                time_dict[group_name] = time
            else:
                time_dict[group_name] += time
sum = 0
for key, value in time_dict.items():
    sum += value
print(f"Total time: {sum}")
for key, value in time_dict.items():
    print(f"{key} -> {value}")
for key,value in concert_dict.items():
    print(f"{key}")
    for el in value:
        print(f"=> {el}")
    break