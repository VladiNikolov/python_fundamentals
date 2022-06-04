input_lines = input().split()
count_remove_numbers = int(input())

new_list_as_integer = []
final_list_as_str = []
for element in input_lines:
    new_list_as_integer.append(int(element))
for i in range(count_remove_numbers):
    new_list_as_integer.remove(min(new_list_as_integer))
for elements in new_list_as_integer:
    final_list_as_str.append(str(elements))

print(", ".join(final_list_as_str))