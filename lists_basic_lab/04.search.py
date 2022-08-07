number = int(input())
word = input()

first_list = []
for _ in range(number):
    current_word = input()
    first_list.append(current_word)

filtered_list = []
for element in first_list:
    if word in element:
        filtered_list.append(element)
print(first_list)
print(filtered_list)
