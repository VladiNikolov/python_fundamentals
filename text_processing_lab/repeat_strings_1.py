input_string = input().split()

repeated_list = []
for word in input_string:
    repeat_string = word * len(word)
    repeated_list.append(repeat_string)
print("".join(repeated_list))
