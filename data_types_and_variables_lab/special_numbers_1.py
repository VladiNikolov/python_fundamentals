number = int(input())

for num in range(1, number + 1):
    sum_digits = 0
    digit = num
    if digit > 0:
        sum_digits += digit % 10
        digit = int(digit / 10)
    if sum_digits + digit == 5 or sum_digits + digit == 7 or sum_digits + digit == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

