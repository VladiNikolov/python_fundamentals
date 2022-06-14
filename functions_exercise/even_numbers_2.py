input_line = list(map(int, input().split()))
my_list = []
for current_number in input_line:
    if current_number % 2 == 0:
        my_list.append(current_number)
print(my_list)