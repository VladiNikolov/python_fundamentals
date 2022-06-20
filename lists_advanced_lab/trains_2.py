number_of_wagons = int(input())
train = []

for _ in range(number_of_wagons):
    train.append(0)
command = input()
while not command == "End":
    data = command.split()
    if data[0] == "add":
        train[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        n_people = int(data[2])
        train[index] += n_people
    elif data[0] == "leave":
        index = int(data[1])
        n_people = int(data[2])
        train[index] -= n_people
    command = input()

print(train)