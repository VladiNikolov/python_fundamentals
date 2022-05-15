number = int(input())

is_balanced = True
has_open_bracket = False

for _ in range(1, number + 1):
    current_input = input()
    if current_input != "(" and current_input != ")":
        continue

    is_open_bracket = current_input == "("
    if has_open_bracket == is_open_bracket:
        is_balanced = False
        break

    has_open_bracket = is_open_bracket

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
