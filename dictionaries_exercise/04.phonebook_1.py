phonebook_dict = {}

while True:
    input_lines = input()
    if not "-" in input_lines:
        break
    name, phone = input_lines.split("-")
    phonebook_dict[name] = phone

for checking in range(int(input_lines)):
    searched_name = input()
    if searched_name in phonebook_dict:
        print(f"{searched_name} -> {phonebook_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
