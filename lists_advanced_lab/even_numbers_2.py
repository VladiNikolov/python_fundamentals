numbers_list = list(map(int, input().split(", ")))

list_with_index = []
for index, element in enumerate(numbers_list):
    if element % 2 == 0:
        list_with_index.append(index)
print(list_with_index)

