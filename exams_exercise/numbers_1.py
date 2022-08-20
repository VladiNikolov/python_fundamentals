input_line = input().split()
input_line = [int(i) for i in input_line]
average_number = sum(input_line) / len(input_line)
list_top_five = []

for element in input_line:
    if element > average_number:
        list_top_five.append(element)

if list_top_five == []:
    print("No")

list_top_five.sort()
list_top_five.reverse()

print(*list_top_five[:5])
