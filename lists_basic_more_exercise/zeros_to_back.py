# input_string = input().split(", ")
# my_list_1 = []
# my_list_2 = []
#
# for string in input_string:
#     if int(string) != 0:
#         my_list_1.append(int(string))
#     else:
#         my_list_2.append(int(string))
# print(my_list_1 + my_list_2 )
#
#--------------------------------------
#
input_string = input().split(", ")
my_list_1 = []
my_list_2 = []

for string in input_string:
    if int(string) != 0:
        my_list_1.append(int(string))
    else:
        my_list_2.append(int(string))
my_list_1.extend(my_list_2)
print(my_list_1)
