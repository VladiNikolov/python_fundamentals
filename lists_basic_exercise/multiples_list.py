# factor_number = int(input())
# count_number = int(input())
#
# my_list = []
#
# for num in range(1, count_number + 1):
#     my_list.append(num * factor_number)
# print(my_list)


factor_number = int(input())
count_number = int(input())

my_list = []
new_number = factor_number * count_number
for num in range(1, count_number + 1):
    new_number = new_number - factor_number
    my_list.append(new_number + factor_number)
    my_list.sort()
print(my_list)