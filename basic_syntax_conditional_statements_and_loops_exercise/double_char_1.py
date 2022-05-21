current_command = input()

while current_command != "End":
    if current_command != "SoftUni":
        for char in current_command:
            print(f"{char * 2}", end ="")
        print()
    current_command = input()

