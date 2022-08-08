input_line = input().split()
input_line = [int(i) for i in input_line]

opposite_list = []
for i in input_line:
    current_element = i * -1
    opposite_list.append(current_element)

print(opposite_list)