def add_and_subtract(number_one: int, number_two: int, number_three: int):
    sum_numbers = number_one + number_two
    result = sum_numbers - number_three
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))