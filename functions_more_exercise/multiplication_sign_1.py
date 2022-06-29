numbers = []
numbers.append(float(input()))
numbers.append(float(input()))
numbers.append(float(input()))

negative_numbers = [num for num in numbers if num < 0]

if numbers.count(0) >= 1:
    print("zero")
elif len(negative_numbers) % 2 == 0:
    print("positive")
else:
    print("negative")