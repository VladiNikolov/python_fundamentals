item_dict = {}

while True:
    command = input()
    if command == "Sail":
        break
    else:
        data_info = command.split("||")
        town = data_info[0]
        people = int(data_info[1])
        gold = int(data_info[2])

        if town not in item_dict:
            item_dict[town] = []
            item_dict[town].append(people)
            item_dict[town].append(gold)
        else:
            item_dict[town][0] += people
            item_dict[town][1] += gold

while True:
    input_command = input()
    if input_command == 'End':
        break
    else:
        input_command = input_command.split("=>")
        name_command = input_command[0]
        town = input_command[1]

        if name_command == "Plunder":
            people = int(input_command[2])
            gold = int(input_command[3])
            if town in item_dict:
                item_dict[town][0] -= people
                item_dict[town][1] -= gold
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

            if item_dict[town][0] <= 0 or item_dict[town][1] <= 0:
                del item_dict[town]
                print(f"{town} has been wiped off the map!")
        elif name_command == "Prosper":
            gold = int(input_command[2])

            if gold <= 0:
                print("Gold added cannot be a negative number!")
                continue
            else:
                item_dict[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {item_dict[town][1]} gold.")

if len(item_dict) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(item_dict)} wealthy settlements to go to:")
    for key, value in item_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
