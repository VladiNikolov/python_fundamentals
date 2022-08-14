command = input()

phonebook_dict = {}

while "-" in command:
    command = command.split("-")
    name = command[0]
    number = command[1]
    if name not in phonebook_dict:
        phonebook_dict[name] = number

    command = input()
for i in range(int(command)):
    searched_name = input()
    if searched_name in phonebook_dict.keys():
        print(f"{searched_name} -> {phonebook_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
