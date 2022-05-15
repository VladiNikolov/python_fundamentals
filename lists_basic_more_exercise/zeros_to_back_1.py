string = input().split(", ")
first_list = []
second_list = []

for num in string:
    if int(num) > 0:
        first_list.append(int(num))
    else:
        second_list.append(int(num))
first_list.extend(second_list)
print(first_list)
