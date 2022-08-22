input_line = list(map(int, input().split()))
average_number = sum(input_line) // len(input_line)
new_list = []
for index in range(len(input_line)):
    if input_line[index] > average_number:
        new_list.append(input_line[index])

if new_list == []:
    print("No")
new_list.sort()
new_list.reverse()
print(*new_list[0:5])