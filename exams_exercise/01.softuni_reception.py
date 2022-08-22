first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())
count_hours = 0

while number_of_students > 0:
    count_hours += 1
    if count_hours % 4 == 0:
        count_hours += 1
    number_of_students -= first_employee + second_employee + third_employee
print(f"Time needed: {count_hours}h.")