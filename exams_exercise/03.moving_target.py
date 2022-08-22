targets = input().split()
targets = [int(i) for i in targets]

while True:
    command = input()
    if command == "End":
        break
    else:
        current_command = command.split()
        if current_command[0] == "Shoot":
            index = int(current_command[1])
            power = int(current_command[2])
            if 0 <= index <= len(targets):
                if targets[index] - power <= 0:
                    del targets[index]
                else:
                    targets[index] -= power

        elif current_command[0] == "Add":
            index = int(current_command[1])
            value = int(current_command[2])
            if 0 <= index <= len(targets) - 1:
                targets.insert(index, value)
            else:
                print("Invalid placement!")

        elif current_command[0] == "Strike":
            index = int(current_command[1])
            radius = int(current_command[2])
            if index - radius >= 0 and index + radius <= len(targets):
                del targets[index - radius: index + radius + 1]
            else:
                print("Strike missed!")

print(*targets, sep="|")
