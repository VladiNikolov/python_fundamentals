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
    if command == "odd" and current_number % 2 != 0:
        new_list.append(current_number)
    if command == "positive" and current_number >= 0:
        new_list.append(current_number)
    if command == "negative" and current_number < 0:
        new_list.append(current_number)
print(new_list)

