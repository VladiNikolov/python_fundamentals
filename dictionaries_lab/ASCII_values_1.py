input_words = input().split(", ")
my_list = {}
for word in input_words:
    key = word
    value = ord(word)
    my_list[key] = value
print(my_list)
