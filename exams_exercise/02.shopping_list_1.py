input_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    else:
        current_command = command.split()
        if current_command[0] == "Urgent":
            item = current_command[1]
            if item not in input_list:
                input_list.insert(0, item)

        elif current_command[0] == "Unnecessary":
            item = current_command[1]
            if item in input_list:
                input_list.remove(item)

        elif current_command[0] == "Correct":
            old_item = current_command[1]
            new_item = current_command[2]
            if old_item in input_list:
                index = input_list.index(old_item)
                input_list.remove(old_item)
                input_list.insert(index, new_item)

        elif current_command[0] == "Rearrange":
            item = current_command[1]
            if item in input_list:
                input_list.remove(item)
                input_list.append(item)
# print(", ".join(input_list))
# for element in input_list:
#     print(f"{element}, ", end="")
print(*input_list, sep=", ")
