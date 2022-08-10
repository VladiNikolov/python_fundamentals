input_lines = input().split()

command_lines = input()

while command_lines != "No Money":
    command = command_lines.split()
    if command[0] == "OutOfStock":
        gift = command[1]
        for i in range(len(input_lines)):
            if input_lines[i] == gift:
                input_lines[i] = "None"

    if command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(input_lines):
            input_lines[index] = gift

    if command[0] == "JustInCase":
        gift = command[1]
        input_lines[-1] = gift

    command_lines = input()


for element in input_lines:
    if "None" in input_lines:
        input_lines.remove("None")
print(*input_lines)