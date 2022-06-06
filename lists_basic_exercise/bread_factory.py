working_day_events = input().split("|")
initial_energy = 100
initial_coins = 100
condition_close = False
for curr_event in working_day_events:
    events_info = curr_event.split("-")
    event = events_info[0]
    number = int(events_info[1])
    if event == "rest":
        energy_gained = number
        if initial_energy + number > 100:
            energy_gained = 100 - initial_energy
        initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            condition_close = True
            break
if not condition_close:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")