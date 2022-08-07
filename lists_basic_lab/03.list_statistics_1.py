number = int(input())

list_positive = []
list_negative = []

while number > 0:
    next_input = int(input())
    if next_input >= 0:
        list_positive += [next_input]
    else:
        list_negative += [next_input]
    number -= 1
print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")