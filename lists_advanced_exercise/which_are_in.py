first_strings = input().split(", ")
second_strings = input().split(", ")

new_list = []

for el in first_strings:
    for element in second_strings:
        if el in element:
            new_list.append(el)

new_list = list(dict.fromkeys(new_list))
print(new_list)