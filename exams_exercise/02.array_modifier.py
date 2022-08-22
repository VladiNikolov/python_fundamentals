elements = input().split()
elements = [int(i) for i in elements]

command = input()
while command != "end":
    current_command = command.split()
    if current_command[0] == "swap":
        index_1 = int(current_command[1])
        index_2 = int(current_command[2])
        temp = elements[index_1]
        elements[index_1] = elements[index_2]
        elements[index_2] = temp

    elif current_command[0] == "multiply":
        index_1 = int(current_command[1])
        index_2 = int(current_command[2])
        elements[index_1] = elements[index_1] * elements[index_2]

    elif current_command[0] == "decrease":
        for element in range(len(elements)):
            elements[element] -= 1

    command = input()
print(*elements, sep=", ")