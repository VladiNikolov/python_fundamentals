input_number = float(input())

if input_number == 0:
    print("zero")
elif 0 < input_number < 1:
    print("small positive")
elif 1 <= input_number <= 1000000:
    print("positive")
elif input_number > 1000000:
    print("large positive")
elif 0 > input_number > -1:
    print("small negative")
elif -1 >= input_number >= -100000:
    print("negative")
elif input_number < 1000000:
    print("large negative")