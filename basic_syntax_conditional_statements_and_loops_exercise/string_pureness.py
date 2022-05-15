number_of_lines = int(input())
is_string_pure = True
string = ""
for _ in range(number_of_lines):
    current_string = input()
    string = current_string
    for character in range(len(current_string)):
        is_string_pure = True
        if current_string[character] == "," or current_string[character] == "." or current_string[character] == "_":
            is_string_pure = False
            print(f"{string} is not pure!")
            break
    if is_string_pure:
        print(f"{string} is pure.")

