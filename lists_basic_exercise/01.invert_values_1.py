input_line = input().split()

my_list = []
for element in input_line:
    my_list.append(int(element))
new_list = []
for el in my_list:
    if el > 0:
        new_list.append(-el)
    else:
        new_list.append(abs(el))
print(new_list)