students_dict = {}

while True:
    input_line = input()
    if ":" not in input_line:
        searched_course = input_line
        break

    info_data = input_line.split(":")
    name = info_data[0]
    id = info_data[1]
    course = info_data[2]

    course_in_snake_case = "_".join(course.split())
    if course_in_snake_case not in students_dict:
        students_dict[course_in_snake_case] = []
    students_dict[course_in_snake_case].append((name, id))

for name_key, id_value in students_dict[searched_course]:
    print(f"{name_key} - {id_value}" )


