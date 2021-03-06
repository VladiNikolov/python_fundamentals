input_string = input().split("|")
energy = 100
coins = 100
gained_energy = 0
is_closed = False
for current_input in input_string:
    argument = current_input.split("-")
    event = argument[0]
    quantity = int(argument[1])

    if event == "rest":
        energy_gained = quantity
        if energy + quantity > 100:
            energy_gained = 100 - energy
        energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy - 30 >= 0:
            print(f"You earned {quantity} coins.")
            coins += quantity
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - quantity >= 0:
            print(f"You bought {event}.")
            coins -= quantity
        else:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break
if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
