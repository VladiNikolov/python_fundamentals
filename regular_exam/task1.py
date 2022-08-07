input_string = input()

command_list = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration", "Abracadabra"]
while True:
    command = input().split()
    if command[0] not in command_list:
        print("The spell did not work!")

    elif command[0] == "Abracadabra":
        break

    elif command[0] == "Abjuration":
        input_string = input_string.upper()
        print(input_string)

    elif command[0] == "Necromancy":
        input_string = input_string.lower()
        print(input_string)

    elif command[0] == "Illusion":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(input_string):
            input_string = input_string[:index] + letter + input_string[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")
        # if index < 0 or index >= len(input_string):
        #
        # else:
        #     input_string = input_string.replace(input_string[index], letter)


    elif command[0] == "Divination":
        first_substring = command[1]
        second_substring = command[2]

        if first_substring in input_string:
            input_string = input_string.replace(first_substring, second_substring)
            print(input_string)

    elif command[0] == "Alteration":
        substring = command[1]

        if substring in input_string:
            input_string = input_string.replace(substring, "")
            print(input_string)