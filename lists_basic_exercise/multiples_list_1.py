factor = int(input())
number = int(input())

my_list = []
for current_index in range(1, number + 1):
    current_number = current_index * factor
    my_list.append(current_number)
print(my_list)

