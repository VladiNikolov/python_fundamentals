input_line = input()
input_line = input_line.lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for current_letter in my_list:
    if current_letter in input_line:
        word_count = input_line.count(current_letter)
        counter += word_count
print(counter)

