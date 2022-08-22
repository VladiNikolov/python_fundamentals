initial_energy = int(input())
won_count = 0
no_energy = False
while True:
    command = input()
    if command == "End of battle":
        break
    else:
        current_command = int(command)
        if initial_energy < current_command:
            print(f"Not enough energy! Game ends with {won_count} won battles and {initial_energy} energy")
            no_energy = True
            break
        else:
            initial_energy -= current_command
            won_count += 1

        if won_count % 3 == 0:
            initial_energy += won_count
if not no_energy:
    print(f"Won battles: {won_count}. Energy left: {initial_energy}" )