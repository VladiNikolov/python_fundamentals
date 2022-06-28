def type_func(command: str, string: str):


    if command == "int":
        result = int(string) * 2
        print(f"{result}")
    elif command == "real":
        result = float(string) * 1.5
        print(f"{result:.2f}")
    elif command == "string":
        result = f"${string}$"
        print(result)

input_command = input()
input_string = input()
type_func(input_command, input_string)