number = int(input())
string = input()

my_list = []
new_list = []
for word in range(number):
    current_word = input()
    my_list.append(current_word)
    if string in current_word:
        new_list.append(current_word)
print(my_list)
print(new_list)
