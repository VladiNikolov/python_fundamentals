# text = input()
# text = text.lower()
#
# my_list = ["sand", "water", "fish", "sun"]
# counter = 0
#
# for item in my_list:
#     if item in text:
#         word_count_txt = text.count(item)
#         counter += word_count_txt
#
# print(counter)

# input_line = input()
# input_line = input_line.lower()
#
# my_list = ["sand", "water", "fish", "sun"]
# counter = 0
#
# for current_letter in my_list:
#     if current_letter in input_line:
#         word_count = input_line.count(current_letter)
#         counter += word_count
# print(counter)

user_input = str.lower(input())
counter = 0
index = 0
beach_words = ["sand", "water", "fish", "sun"]
for n in beach_words:
    counter += user_input.count(n)
print(counter)