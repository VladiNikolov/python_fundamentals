# input_str = input().split()
# number = int(input())
#
# for index in range(len(input_str)):
#     input_str[index] = int(input_str[index])
# for num in range(number):
#     temp = min(input_str)
#     input_str.remove(temp)
#
# print(", ".join(map(str, input_str)))
#
#-----------------------------------------------
#
input_str = input().split()
number = int(input())
new_list_with_int = []

for index in range(len(input_str)):
    new_list_with_int.append(int(input_str[index]))

for num in range(number):
    temp = min(new_list_with_int)
    new_list_with_int.remove(temp)

print(", ".join(map(str, new_list_with_int)))
