import math

number = int(input())
students_dict = {}
sum = 0
for _ in range(number):
    student_name = input()
    grade = float(input())


    if student_name not in students_dict:
        students_dict[student_name] = []
        students_dict[student_name].append(grade)
    else:
        students_dict[student_name].append(grade)

for keys, value in students_dict.items():
    result = math.fsum(value) / len(value)
    if result >= 4.50:
        print(f"{keys} -> {result:.2f}")

