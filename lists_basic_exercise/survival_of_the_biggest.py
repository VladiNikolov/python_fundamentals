input_lines = input().split(" ")
copy_input_lines = list(map(int, input_lines))
count = int(input())

for _ in range(count):
    current_min_elements = min(copy_input_lines)
    input_lines.remove(str(current_min_elements))
    copy_input_lines.remove(current_min_elements)


print(", ".join(input_lines))

