number = int(input())
special_word = input()

first_list = []

for current_word in range(number):
    current_input = input()
    first_list.append(current_input)
print(first_list)

second_list = []

for current_word in first_list:
    if special_word in current_word:
        second_list.append(current_word)

print(second_list)