input_number = int(input())

command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"

first_list = [int(input()) for _ in range(input_number)]

second_list = []
command = input()

for num in first_list:
    filtered_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )
    if filtered_command:
        second_list.append(num)
print(second_list)