# number = int(input())
#
# first_list = list()
#
# for i in range(number):
#     current_input = int(input())
#     first_list.append(current_input)
#
# command = input()
# filtered_list = list()
#
# for current_number in first_list:
#     if command == "even":
#         if current_number % 2 == 0:
#             filtered_list.append(current_number)
#     if command == "odd":
#         if current_number % 2 != 0:
#             filtered_list.append(current_number)
#     if command == "negative":
#         if current_number < 0:
#             filtered_list.append(current_number)
#     if command == "positive":
#         if current_number >= 0:
#             filtered_list.append(current_number)
# print(filtered_list)

#------------------------------------------------------
#
number = int(input())

even_list = list()
odd_list = list()
positive_list = list()
negative_list = list()

for current_number in range(number):
    current_input = int(input())
    if current_input % 2 == 0:
        even_list.append(current_input)
    else:
        odd_list.append(current_input)
    if current_input >= 0:
        positive_list.append(current_input)
    else:
        negative_list.append(current_input)

command = input()

if command == "even":
    print(even_list)
if command == "odd":
    print(odd_list)
if command == "positive":
    print(positive_list)
if command == "negative":
    print(negative_list)


