# factor = int(input())
# number = int(input())
#
# my_list = []
# for current_index in range(1, number + 1):
#     current_number = current_index * factor
#     my_list.append(current_number)
# print(my_list)
#
#----------------------------------------------
#
factor = int(input())
count = int(input())

my_list = []
number = factor * count
for _ in range(count):
    number = number - factor
    my_list.append(number)
new_list = []
for num in my_list:
    new_list.append(num + factor)
new_list.reverse()
print(new_list)