input_line = input().split("!")

command = input()

while command != "Go Shopping!":
    current_command = command.split()
    if current_command[0] == "Urgent":
        item = current_command[1]
        if item not in input_line:
            input_line.insert(0, item)

    elif current_command[0] == "Unnecessary":
        item = current_command[1]
        if item in input_line:
            input_line.remove(item)

    elif current_command[0] == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in input_line:
            index = input_line.index(old_item)
            input_line.remove(old_item)
            input_line.insert(index, new_item)

    elif current_command[0] == "Rearrange":
        item = current_command[1]
        if item in input_line:
            input_line.remove(item)
            input_line.append(item)

    command = input()
print(", ".join(input_line))
