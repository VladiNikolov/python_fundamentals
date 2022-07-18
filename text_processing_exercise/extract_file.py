input_string = input().split("\\")

current_element = input_string[-1].split(".")
print(f"File name: {current_element[0]}")
print(f"File extension: {current_element[1]}")

