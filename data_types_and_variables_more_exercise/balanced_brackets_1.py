number_of_lines = int(input())

count_open_bracket = 0
count_close_bracket = 0

for _ in range(number_of_lines):
    current_input = input()
    if current_input != "(" and current_input != ")":
        continue

    if current_input == "(":
        count_open_bracket += 1
    else:
        count_close_bracket += 1

if count_open_bracket == count_close_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
