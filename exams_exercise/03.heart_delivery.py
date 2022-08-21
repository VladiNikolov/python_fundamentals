input_line = input().split("@")
input_line = list(map(int, input_line))
index = 0
count = len(input_line)
while True:
    command = input()
    if command == "Love!":
        break
    else:
        concurrent_command = command.split()
        if concurrent_command[0] == "Jump":
            length = int(concurrent_command[1])

            if index + length < len(input_line):
                index = length + index
            elif index + length >= len(input_line):
                index = 0

            if input_line[index] > 2:
                input_line[index] -= 2

            elif input_line[index] == 2:
                input_line[index] -= 2
                count -= 1
                print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")


print(f"Cupid's last position was {index}.")

if sum(input_line) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")