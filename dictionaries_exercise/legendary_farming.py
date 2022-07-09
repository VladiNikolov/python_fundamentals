items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}

obtained = False
command = input().split()

while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key == "shards" or key == "fragments" or key == "motes":
            items_dict[key] += value
        else:
            if key not in junk_dict.keys():
                junk_dict[key] = 0
            junk_dict[key] += value

        if items_dict["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items_dict["shards"] -= 250
            obtained = True
        elif items_dict["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items_dict["fragments"] -= 250
            obtained = True
        elif items_dict["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items_dict["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()

for material, quantity in items_dict.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_dict.items():
    print(f"{material}: {quantity}")