first_list = input().split(", ")
second_list = input().split(", ")

substrings = []
for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in substrings:
            substrings.append(first_word)
            break
print(substrings)