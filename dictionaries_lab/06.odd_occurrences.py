input_line = input().lower().split()

courses_dict = {}
for element in input_line:
    if element not in courses_dict:
        courses_dict[element] = 1
    else:
        courses_dict[element] += 1
for keys, value in courses_dict.items():
    if value % 2 != 0:
        print(keys, end=" ")
