def positive_numbers(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if int(number) % 2 != 0]

input_numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(input_numbers))}")
print(f"Negative: {', '.join(negative_numbers(input_numbers))}")
print(f"Even: {', '.join(even_numbers(input_numbers))}")
print(f"Odd: {', '.join(odd_numbers(input_numbers))}")