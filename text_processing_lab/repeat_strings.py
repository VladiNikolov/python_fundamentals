input_strings = input().split()

for word in input_strings:
    result = word * len(word)
    print(result, end="")