command = input()

while command != "End":
    if command != "SoftUni":
        for char in command:
            print(f"{char * 2}", end="")
        print()
    command = input()