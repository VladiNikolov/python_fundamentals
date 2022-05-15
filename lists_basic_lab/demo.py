# number = int(input())
# even_list = []
# odd_list = []
# negative_list = []
# positive_list = []
# for _ in range(number):
#     current_input = int(input())
#
#     if current_input % 2 == 0:
#         even_list.append(current_input)
#     else:
#         odd_list.append(current_input)
#     if current_input < 0:
#         negative_list.append(current_input)
#     else:
#         positive_list.append(current_input)
# command = input()
#
# if command == "even":
#     print(even_list)
# elif command == "odd":
#     print(odd_list)
# elif command == "negative":
#     print(negative_list)
# elif command == "positive":
#     print(positive_list)

number = int(input())

my_list = []
for _ in range(number):
    current_input = int(input())
    my_list.append(current_input)

new_list = []
command = input()
for current_number in my_list:
    if command == "even" and current_number % 2 == 0:
        new_list.append(current_number)
    elif command == "odd" and current_number % 2 != 0:
        new_list.append(current_number)
    elif command == "negative" and current_number < 0:
        new_list.append(current_number)
    elif command == "positive" and current_number >= 0:
        new_list.append(current_number)
print(new_list)

