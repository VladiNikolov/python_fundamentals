number = int(input())

command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"

my_list = []
filtered_list = []

for _ in range(number):
    current_number = int(input())
    my_list.append(current_number)

command = input()
for num in my_list:
    filtered_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )
    if filtered_command:
        filtered_list.append(num)
print(filtered_list)
