phonebook_dict = {}

current_input = input()
while "-" in current_input:
    name, phone = current_input.split("-")
    phonebook_dict[name] = phone

    current_input = input()
for checking in range(int(current_input)):
    searched_contact = input()
    if searched_contact in phonebook_dict.keys():
        print(f"{searched_contact} -> {phonebook_dict[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
