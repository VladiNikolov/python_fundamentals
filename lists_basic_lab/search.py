# number = int(input())
# input_text = input()
#
# current_list = list()
# filter_list = list()
#
# for current_number in range(number):
#     current_input = input()
#     current_list.append(current_input)
#     if input_text in current_input:
#         filter_list.append(current_input)
# print(current_list)
# print(filter_list)
#
#-----------------------------------------
#
number = int(input())
searched_word = input()

current_list = []

for current_string in range(1, number + 1):
    current_list.append(input())
print(current_list)

filter_list = []

for current_string in current_list:
    if searched_word in current_string:
        filter_list.append(current_string)
print(filter_list)

