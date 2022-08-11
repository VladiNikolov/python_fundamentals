input_line = input().split()

while True:
    commands = input()


    if commands == "No Money":
        break

    command_line = commands.split()

    if command_line[0] == "OutOfStock":
        gift = command_line[1]
        for index in range(len(input_line)):
            if input_line[index] == gift:
                input_line[index] = "None"

    if command_line[0] == "Required":
        gift = command_line[1]
        gift_index = int(command_line[2])
        if 0 <= gift_index < len(input_line):
            input_line[gift_index] = gift

    if command_line[0] == "JustInCase":
        gift = command_line[1]
        input_line[-1] = gift

for element in input_line:
    if element == "None":
        input_line.remove(element)
print(*input_line)
