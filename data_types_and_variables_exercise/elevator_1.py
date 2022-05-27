from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())
result = 0
if number_of_people <= elevator_capacity:
    result = 1
else:
    result = ceil(number_of_people / elevator_capacity)
print(result)