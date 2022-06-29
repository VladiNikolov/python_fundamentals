first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number == 0 or second_number == 0 or third_number == 0:
    print("zero")
elif first_number > 0 and second_number > 0 and third_number > 0:
    print("positive")
else:
    print("negative")