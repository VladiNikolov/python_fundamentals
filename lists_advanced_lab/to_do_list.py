my_list = []


while True:
    command = input().split("-")

    if command[0] == "End":
        break

    priority = int(command[0])
    task = command[1]
    my_list.append((priority, task))

sorted_list = [task_data[1] for task_data in sorted(my_list)]
print(sorted_list)
