input_line = input().split()

count_won = 0
while True:
    command = input()
    if command == "end":
        break
    current_element = command.split()
    index_1 = int(current_element[0])
    index_2 = int(current_element[1])
    count_won += 1

    if index_1 < 0 or index_1 >= len(input_line) or index_2 < 0 or index_2 >= len(input_line) or index_1 == index_2:
        current_len = len(input_line) // 2
        input_line.insert(current_len, f"-{count_won}a")
        input_line.insert(current_len, f"-{count_won}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if input_line[index_1] == input_line[index_2]:
        print(f"Congrats! You have found matching elements - {input_line[index_1]}!")
        removed_element = input_line[index_1]
        input_line.remove(removed_element)
        input_line.remove(removed_element)


    elif input_line[index_1] != input_line[index_2]:
        print("Try again!")

    if len(input_line) == 0:
        print(f"You have won in {count_won} turns!")
        break

if len(input_line) > 0:
    print("Sorry you lose :(")
    print(" ".join(map(str, input_line)))




