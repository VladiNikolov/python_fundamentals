dungeon_rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
count = 0
is_killed = False

for room in dungeon_rooms:
    element_info = room.split()
    command = element_info[0]
    number = int(element_info[1])
    count += 1
    if command == "potion":
        current_health = number
        if initial_health + number > 100:
            current_health = 100 - initial_health
        initial_health += current_health
        print(f"You healed for {current_health} hp.")
        print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count}")
            is_killed = True
            break
if not is_killed:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
