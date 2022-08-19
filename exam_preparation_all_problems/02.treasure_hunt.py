input_line = input().split("|")

steal_elements = []

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        for element in range(1, len(command)):
            if command[element] not in input_line:
                input_line.insert(0, command[element])

    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(input_line):
            item = input_line.pop(index)
            input_line.append(item)

    elif command[0] == "Steal":
        count = int(command[1])
        if count >= len(input_line):
            steal_elements = input_line
            print(", ".join(steal_elements))
            print("Failed treasure hunt.")
            exit()
        else:
            steal_elements = input_line[-count:]
            del input_line[-count:]
            print(", ".join(steal_elements))

[len(i) for i in input_line]
sum = sum(len(i) for i in input_line)

if len(input_line) > 0:
    sum_items = 0
    for item in input_line:
        sum_items += len(item)
    print(f"Average treasure gain: {(sum_items/len(input_line)):.2f} pirate credits.")








