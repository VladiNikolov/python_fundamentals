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
# list_of_numbers = input().split(" ")
#
# opposite_lists = []
# for index in range(len(list_of_numbers)):
#     opposite_list = -int(list_of_numbers[index])
#     opposite_lists.append(opposite_list)
#
# print(opposite_lists)
#
#---------------------------------------------
#
# input_str = input().split()
# opposite_list = []
#
# for index in range(len(input_str)):
#     current_index = int(input_str[index])
#     if current_index < 0:
#         current_index = current_index * - 1
#         opposite_list.append(current_index)
#     elif current_index > 0:
#         current_index = current_index * -1
#         opposite_list.append(current_index)
#     else:
#         opposite_list.append(current_index)
# print(opposite_list)
#
#-----------------------------------------------
#
input_str = input().split()
opposite_list = []
for num in input_str:
    num = int(num) * - 1
    opposite_list.append(num)
print(opposite_list)