def min_number(numbers):
    print(f"The minimum number is {min(input_numbers)}")

def max_number(numbers):
    print(f"The maximum number is {max(input_numbers)}")

def sum_numbers(numbers):
    print(f"The sum number is: {sum(input_numbers)}")

input_numbers = list(map(int, input().split()))

result = min_number(input_numbers), max_number(input_numbers), sum_numbers(input_numbers)
