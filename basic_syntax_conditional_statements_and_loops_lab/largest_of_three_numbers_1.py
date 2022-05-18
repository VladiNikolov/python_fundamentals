number_one = int(input())
number_two = int(input())
number_three = int(input())

if number_one > number_two and number_one > number_three:
    print(number_one)
elif number_two > number_one and number_two > number_three:
    print(number_two)
else:
    print(number_three)
