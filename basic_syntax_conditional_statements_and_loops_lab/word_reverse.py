# text = input()
# length = len(text)
# sliced_string = text[length::-1]
# print(sliced_string)

text = input()
for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")