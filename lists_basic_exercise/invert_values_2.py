input_string = input().split()

new_list = []
for num in input_string:
    current_number = int(num) * -1
    new_list.append(current_number)
print(new_list)