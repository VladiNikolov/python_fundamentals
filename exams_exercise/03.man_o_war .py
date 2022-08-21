status_pirate_ship = input().split(">")
status_pirate_ship = [int(i) for i in status_pirate_ship]
status_warship = input().split(">")
status_warship = [int(i) for i in status_warship]
maximum_health = int(input())

while True:
    command = input().split()
    if command[0] == "Retire":
        break

    elif command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_warship):
            if status_warship[index] - damage <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
            else:
                status_warship[index] = status_warship[index] - damage

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(status_pirate_ship) and 0 <= end_index < len(status_pirate_ship):
            for i in range(start_index, end_index + 1):
                if status_pirate_ship[i] - damage <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
                else:
                    status_pirate_ship[i] = status_pirate_ship[i] - damage

    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            if status_pirate_ship[index] + health <= maximum_health:
                status_pirate_ship[index] = status_pirate_ship[index] + health
            else:
                status_pirate_ship[index] = maximum_health

    elif command[0] == "Status":
        count = 0
        repair_sections = maximum_health * 0.20
        for element in status_pirate_ship:
            if element < int(repair_sections):
                count += 1
        print(f"{count} sections need repair.")

print(f"Pirate ship status: {sum(status_pirate_ship)}")
print(f"Warship status: {sum(status_warship)}")
