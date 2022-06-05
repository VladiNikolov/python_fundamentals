names_of_the_gifts = input().split()

command = input()
command_list = command.split()
new_list = []
while command != "No Money":
    if command_list[0] == "OutOfStock":
        gifts = command_list[1]
        for element in range(len(names_of_the_gifts)):
            if names_of_the_gifts[element] == gifts:
                names_of_the_gifts[element] = "None"
    if command_list[0] == "Required":
        gifts = command_list[1]
        if 0 <= int(command_list[2]) < len(names_of_the_gifts):
            names_of_the_gifts[int(command_list[2])] = gifts

    if command_list[0] == "JustInCase":
        gifts = command_list[1]

        names_of_the_gifts[-1] = gifts

    command = input()
    command_list = command.split()
for element in names_of_the_gifts:
    if "None" in names_of_the_gifts:
        names_of_the_gifts.remove("None")
print(" ".join(names_of_the_gifts))