input_line = input()
new_string = input_line

while True:
    command = input().split()
    if command[0] == "Easter":
        break

    elif command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        for i in input_line:
            input_line = input_line.replace(current_char, new_char)
        print(input_line)

    elif command[0] == "Remove":
        substring = command[1]
        if substring in input_line:
            input_line = input_line.replace(substring, "")
        print(input_line)


    elif command[0] == "Includes":
        string = command[1]
        if string in input_line:
            print(True)
        else:
            print(False)

    elif command[0] == "Change":
        upper_lower = command[1]
        if upper_lower == "Lower":
            input_line = input_line.lower()
        else:
            input_line = input_line.upper()
        print(input_line)


    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index >= 0 and end_index < len(input_line):
            new_string = input_line[start_index:end_index + 1][::-1]
            print(new_string)

