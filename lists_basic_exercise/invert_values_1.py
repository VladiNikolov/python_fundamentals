# single_string = input().split(" ")
#
# new_list = []
# for num in single_string:
#     new_num = -int(num)
#     new_list.append(new_num)
# print(new_list)
#
# ----------------------------------------
#
# single_string = input().split(" ")
#
# invert_values_list = list()
#
# for num in single_string:
#     if int(num) > 0:
#         invert_values_list.append(-int(num))
#     else:
#         invert_values_list.append(abs(int(num)))
# print(invert_values_list)
#
#--------------------------------------------------
#
input_string = input().split(" ")

my_list = []
for num in input_string:
    my_list.append(-int(num))
print(my_list)
