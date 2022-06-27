input_line = input().split(", ")
phone_list = input_line.copy()

data = input()

while data != "End":

    data = data.split(" - ")
    command = data[0]
    model = data[1]

    if command == "Add":
        if model not in phone_list:
            phone_list.append(model)
    elif command == "Remove":
        if model in phone_list:
            phone_list.remove(model)
    elif command == "Bonus phone":
        bonus_model = model.split(":")
        old_phone = bonus_model[0]
        new_phone = bonus_model[1]
        if old_phone in phone_list:
            index = phone_list.index(old_phone)
            phone_list.insert(index +1, new_phone)
    elif command == "Last":
        if model in phone_list:
            phone_list.remove(model)
            phone_list.append(model)
    data = input()
print(", ".join(phone_list))