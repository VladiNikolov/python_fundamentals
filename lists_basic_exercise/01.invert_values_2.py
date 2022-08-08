input_line = input().split()

my_list = []
for element in input_line:
    if int(element) > 0:
        my_list.append(-int(element))
    else:
        my_list.append(abs(int(element)))


print(my_list)