courses_as_dict = {}

current_line = input()

while True:
    if ':' not in current_line:
        course_of_interest = current_line
        break

    student_name, student_id, course = current_line.split(':')
    course_in_snake_case = '_'.join(course.split())
    if course_in_snake_case not in courses_as_dict:
        courses_as_dict[course_in_snake_case] = []
    courses_as_dict[course_in_snake_case].append((student_name, student_id))

    current_line = input()

result = []

for s_name, s_id in courses_as_dict[course_of_interest]:
    result.append(f'{s_name} - {s_id}')

print('\n'.join(result))