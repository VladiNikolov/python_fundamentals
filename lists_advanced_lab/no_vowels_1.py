input_line = input()
vowels = ['a', 'o', 'u', 'e', 'i']

new_list = []
for current_element in input_line:
    if current_element.lower() not in vowels:
        new_list.append(current_element)
print("".join(new_list))