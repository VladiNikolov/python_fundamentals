animal_dict = {}
area_dict = {}

while True:
    line = input().split(": ")
    command = line[0]

    if command == "EndDay":
        break

    if command == "Add":
        animal_info = line[1].split("-")
        animal_name = animal_info[0]
        food = int(animal_info[1])
        area = animal_info[2]

        if animal_name in animal_dict:
            animal_dict[animal_name][1] += food
        else:
            animal_dict[animal_name] = [area, food]

            if area in area_dict:
                area_dict[area] += 1
            else:
                area_dict[area] = 1

    elif command == "Feed":
        animal_info = line[1].split("-")
        animal_name = animal_info[0]
        food = int(animal_info[1])

        if animal_name in animal_dict:
            animal_dict[animal_name][1] -= food
            if animal_dict[animal_name][1] <= 0:
                animal_area = animal_dict[animal_name][0]
                print(f"{animal_name} was successfully fed")
                area_dict[animal_area] -= 1
                if area_dict[animal_area] <= 0:
                    del area_dict[animal_area]
                del animal_dict[animal_name]

print("Animals:")
for animal in animal_dict:
    print(f" {animal} -> {animal_dict[animal][1]}g")
print("Areas with hungry animals:")
for areas, count in area_dict.items():

    print(f" {areas}: {count}")

