numbers = input().split(" ")

abs_numbers = []

for num in numbers:
    abs_numbers.append(abs(float(num)))
print(abs_numbers)