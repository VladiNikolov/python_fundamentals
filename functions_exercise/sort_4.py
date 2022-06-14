def sort(input_list):
    return f"{sorted(input_list)}"

input_line = input().split()
input_line = [int(i) for i in input_line]
print(sort(input_line))