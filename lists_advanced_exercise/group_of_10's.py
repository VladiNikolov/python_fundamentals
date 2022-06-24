input_numbers = input().split(", ")
input_numbers = [int(i) for i in input_numbers]

group = 10
max_number = max(input_numbers)

while input_numbers:
    nums_group = []

    for number in input_numbers:
        if number in range(group - 10, group + 1):
            nums_group.append(number)

    for number in nums_group:
        input_numbers.remove(number)
    print(f"Group of {group}'s: {nums_group}")
    group += 10

