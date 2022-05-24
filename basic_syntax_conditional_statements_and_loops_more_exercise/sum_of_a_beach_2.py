user_input = str.lower(input())

counter = 0
beach_words = ["sand", "water", "fish", "sun"]
for n in beach_words:
    counter += user_input.count(n)
print(counter)