def type_func(command: str, string: str):


    if command == "int":
        result = int(string) * 2
        return result
    elif command == "real":
        result = float(string) * 1.5
        return  f"{result:.2f}"
    else:
        return f"${string}$"

input_command = input()
input_string = input()
print(type_func(input_command, input_string))




