number = int(input())

wagons = [0] * number

while True:
    command = input()

    if command == "End":
        break

    data = command.split()
    type_of_command = data[0]

    if type_of_command == "add":
        numbers = data[1]
        wagons[-1] += int(numbers)
    elif type_of_command == "insert":
        index = int(data[1])
        numbers = data[2]
        wagons[index] += int(numbers)
    elif type_of_command == "leave":
        index = int(data[1])
        numbers = data[2]
        wagons[index] -= int(numbers)

print(wagons)