flag = False
materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
input_materials = input().split()
while True:
    for index in range (0, len(input_materials), 2):
        value_quantity = int(input_materials[index])
        key_name = input_materials[index + 1].lower()


        if key_name == "shards" or key_name == "fragments" or key_name == "motes":
            materials_dict[key_name] += value_quantity
        else:
            if key_name not in junk_dict:
                junk_dict[key_name] = value_quantity
            else:
                junk_dict[key_name] += value_quantity


        if materials_dict["shards"] >= 250:
            materials_dict["shards"] -= 250
            print("Shadowmourne obtained!")
            flag = True
            break

        elif materials_dict["fragments"] >= 250:
            materials_dict["fragments"] -= 250
            print("Valanyr obtained!")
            flag = True
            break

        elif materials_dict["motes"] >= 250:
            materials_dict["motes"] -= 250
            print("Dragonwrath obtained!")
            flag = True
        if flag == True:
            break
    if flag == True:
        break
    input_materials = input().split()
for key, value in materials_dict.items():
    print(f"{key}: {value}")
for key, value in junk_dict.items():
    print(f"{key}: {value}")