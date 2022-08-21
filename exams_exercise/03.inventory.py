input_items = input().split(", ")

command = input()
while command != "Craft!":
    current_command = command.split(" - ")

    if current_command[0] == "Collect":
        item = current_command[1]
        if item not in input_items:
            input_items.append(item)

    elif current_command[0] == "Drop":
        item = current_command[1]
        if item in input_items:
           input_items.remove(item)

    elif current_command[0] == "Combine Items":
        all_item = current_command[1].split(":")
        old_item = all_item[0]
        new_item = all_item[1]
        if old_item in input_items:
            index = input_items.index(old_item)
            input_items.insert(index + 1, new_item)

    elif current_command[0] == "Renew":
        item = current_command[1]
        if item in input_items:
            new_char = item
            input_items.remove(item)
            input_items.append(new_char)

    command = input()
print(", ".join(input_items))