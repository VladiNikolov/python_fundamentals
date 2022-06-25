strings_input = input().split()
result = []
instructions = input()
while not instructions == "3:1":
    instructions = instructions.split()
    command = instructions[0]
    if command == 'merge':
        start = int(instructions[1])
        end = int(instructions[2])
        if start < 0:
            start = 0
        if end > len(strings_input) - 1:
            end = len(strings_input) - 1
        for index, string in enumerate(strings_input):
            if index in range(start + 1, end + 1):
                strings_input[start] += strings_input[index]
        for index in range(end, start, - 1):
            strings_input.pop(index)
    elif command == 'divide':
        index = int(instructions[1])
        partitions = int(instructions[2])
        if partitions > len(strings_input[index]):
            step = 1
        else:
            step = len(strings_input[index]) // partitions
        divide_part = strings_input.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                strings_input.insert(index, divide_part[start::])
                break
            else:
                strings_input.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    instructions = input()
print(' '.join(strings_input))
