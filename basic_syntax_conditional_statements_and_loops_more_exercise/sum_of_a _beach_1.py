input_string = input()
input_string = input_string.lower()

count_word = 0
beach_word = ["sand", "water", "fish", "sun"]
for word in beach_word:
    if word in beach_word:
        count_word += input_string.count(word)
print(count_word)
