def odd_and_even_sum_of_digits(number: str):

    sum_even = 0
    sum_odd = 0
    for character in number:
        digit = int(character)

        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

input_number = input()
print(odd_and_even_sum_of_digits(input_number))

