travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())
break_out = False

is_mission_failed = False
for i in range(len(travel_route)):
    data = travel_route[i].split()
    command = data[0]

    if command == "Travel":
        value = int(data[1])
        if fuel - value >= 0 and fuel >0:
            fuel -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            is_mission_failed = True
            break
    elif command == "Enemy":
        value = int(data[1])
        if ammunition - value >= 0:
            ammunition -= value
            print(f"An enemy with {value} armour is defeated.")
        else:
            if fuel >= value * 2:
                fuel -= value * 2
                print(f"An enemy with {value} armour is outmaneuvered.")
            else:
                is_mission_failed = True
                break_out = True
                break
        if break_out == True:
            break
    elif command == "Repair":
        value = int(data[1])
        fuel += value
        ammunition += value * 2
        print(f"Ammunitions added: {value * 2}.")
        print(f"Fuel added: {value}.")
    elif command == "Titan":
        break

if is_mission_failed:
    print("Mission failed.")
else:
    print("You have reached Titan, all passengers are safe.")
