# string_list = input().split(" ")
# new_string_list = list()
#
# for current_number in string_list:
#     if int(current_number) > 0:
#         new_string_list.append(-int(current_number))
#     else:
#         new_string_list.append(abs(int(current_number)))
#
# print(new_string_list)
#
#---------------------------------------------------------
#
# string_list = input().split(" ")
# new_string_list = list()
#
# for current_number in string_list:
#     new_number = int(current_number) * -1
#     new_string_list.append(new_number)
#
# print(new_string_list)
#
# -------------------------------------------------------
#
list_of_numbers = input().split(" ")

oposite_lists = []
for index in range(len(list_of_numbers)):
    oposite_list = -int(list_of_numbers[index])
    oposite_lists.append(oposite_list)

print(oposite_lists)

