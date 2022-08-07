number = int(input())
number_list = []
filtered_list = []

for _ in range(number):
    input_number = int(input())
    number_list.append(input_number)

command = input()
if command == "even":
    for element in number_list:
        if element % 2 == 0:
            filtered_list.append(element)
elif command == "odd":
    for element in number_list:
        if element % 2 != 0:
            filtered_list.append(element)
elif command == "negative":
    for element in number_list:
        if element < 0:
            filtered_list.append(element)
elif command == "positive":
    for element in number_list:
        if element >= 0:
            filtered_list.append(element)
print(filtered_list)
