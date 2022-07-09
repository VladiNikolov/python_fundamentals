phonebook_dict = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    something = entry.split("-")   # name, phone = entry.split("-")
    name = something[0]
    phone = something[1]
    phonebook_dict[name] = phone

for checking in range(int(entry)):
    searched_contact = input()
    if searched_contact not in phonebook_dict.keys():
        print(f"Contact {searched_contact} does not exist.")
    else:
        print(f"{searched_contact} -> {phonebook_dict[searched_contact]}")






