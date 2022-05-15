number = int(input())

my_list = []

for num in range(number):
    current_input = int(input())
    my_list.append(current_input) # my_list.append(int(input))

new_list = []
command = input()
for num in my_list:
    if command == "even" and num % 2 == 0:
        new_list.append(num)
    elif command == "odd" and num % 2 != 0:
        new_list.append(num)
    elif command == "positive" and num >= 0:
        new_list.append(num)
    elif command == "negative" and num < 0:
        new_list.append(num)

print(new_list)
