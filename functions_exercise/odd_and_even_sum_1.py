def odd_and_even_sum(string):
    sum_even = 0
    sum_odd = 0
    for current_element in range(len(string)):
        if string[current_element] % 2 == 0:
            sum_even += string[current_element]
        else:
            sum_odd += string[current_element]
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

input_line = list(map(int, input()))
print(odd_and_even_sum(input_line))