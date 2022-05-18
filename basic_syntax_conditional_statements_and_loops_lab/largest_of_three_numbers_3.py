my_list = []

my_list.append(int(input()))
my_list.append(int(input()))
my_list.append(int(input()))
for num in range(0, len(my_list) - 1):
    my_list.remove(min(my_list))
print("".join(map(str, my_list)))