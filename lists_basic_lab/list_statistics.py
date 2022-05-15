# number = int(input())
#
# count_positives = 0
# sum_negatives = 0
# positives = list()
# negatives = list()
#
# for current_number in range(number):
#     current_input = int(input())
#     if current_input >= 0:
#         positives.append(current_input)
#         count_positives += 1
#     else:
#         negatives.append(current_input)
#         sum_negatives += current_input
# print(positives)
# print(negatives)
# print(f"Count of positives: {count_positives}")
# print(f"Sum of negatives: {sum_negatives}")
#
#-----------------------------------------------

number = int(input())

positives = []
negatives = []

for current_number in range(1, number + 1):
    current_input = int(input())
    if current_input >= 0:
        positives.append(current_input)
    else:
        negatives.append(current_input)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")