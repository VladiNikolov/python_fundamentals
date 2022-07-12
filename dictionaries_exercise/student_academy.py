number = int(input())
student_diary = {}

sum = 0
count = 0
result = 0
for _ in range(number):
    student_name = input()
    student_result = float(input())
    if student_name not in student_diary:
        student_diary[student_name] = []
        student_diary[student_name].append(student_result)
    else:
        student_diary[student_name].append(student_result)
for key, value in student_diary.items():
    sum = 0
    count = 0
    for i in value:
        count += 1
        sum += i
        result = sum / count
    if result >= 4.50:
        print(f'{key} -> {result:.2f}')

