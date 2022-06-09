input_string = input()
number_of_repeats = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(input_string, number_of_repeats)

print(result)
