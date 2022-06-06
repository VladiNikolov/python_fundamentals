working_day_events = input().split("|")
initial_energy = 100
initial_coins = 100

is_closed = False
for current_event in working_day_events:
    info_events = current_event.split("-")
    event = info_events[0]
    number = int(info_events[1])

    if event == "rest":
        temp_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - temp_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":
        if initial_energy >= 30:
            initial_coins += number
            initial_energy -= 30
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
            continue
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break
if not is_closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
