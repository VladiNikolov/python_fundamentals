input_lines = input().split(", ")

comprehension_dict = {element: ord(element) for element in input_lines}
print(comprehension_dict)