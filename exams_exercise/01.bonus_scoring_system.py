number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
attendance = 0
max_element = 0

for _ in range(number_of_students):
    student_attendance = int(input())

    total_bonus = student_attendance / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_element:
        max_element = total_bonus
        attendance = student_attendance

print(f"Max Bonus: {round(max_element)}.")
print(f"The student has attended {attendance} lectures.")
