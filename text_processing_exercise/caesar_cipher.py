input_string = input()

for character in range(len(input_string)):
    current_element = ord(input_string[character]) + 3
    print(f"{chr(current_element)}", end= "")