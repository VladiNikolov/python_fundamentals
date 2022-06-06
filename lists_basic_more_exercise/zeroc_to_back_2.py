single_string = input().split(", ")

first_list = []
second_list = []
for element in single_string:
    if element == "0":
        first_list.append(int(element))
    else:
        second_list.append(int(element))
print(second_list + first_list)



