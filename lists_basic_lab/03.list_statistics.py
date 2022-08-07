number = int(input())

positive_list = []
negative_list = []

for _ in range(number):
    current_input = int(input())
    if current_input >= 0:
        positive_list.append(current_input)
    else:
        negative_list.append(current_input)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")