factor = int(input())
count = int(input())

my_list = []
for i in range(1, count + 1):
    current_number = i * factor
    my_list.append(current_number)
print(my_list)
