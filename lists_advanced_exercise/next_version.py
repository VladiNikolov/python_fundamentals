input_version = list(map(int, input().split(".")))

input_version[-1] += 1

for current_index in range(len(input_version)-1, -1,-1):
    if input_version[current_index] > 9:
        input_version[current_index] = 0
        input_version[current_index - 1] += 1
print(".".join(map(str, input_version)))

