input_line = input().split()

bakery_dict = {}

for i in range(0, len(input_line), 2):
    bakery_dict[input_line[i]] = int(input_line[i + 1])

print(bakery_dict)