command = input()
while command != "Voldemort":
    if command == "Welcome!":
        print(f"Welcome to Hogwarts.")
        exit()
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()
print("You must not speak of that name!")
