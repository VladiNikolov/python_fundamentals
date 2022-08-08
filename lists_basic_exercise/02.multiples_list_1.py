factor = int(input())
count = int(input())

new_list = []
for i in range(count):
    current_element = (i + 1) * factor
    new_list.append(current_element)
print(new_list)
