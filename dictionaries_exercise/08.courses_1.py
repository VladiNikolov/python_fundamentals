course_dict = {}

command = input()
while command != "end":
    data_info = command.split(" : ")
    course = data_info[0]
    student_name = data_info[1]

    if course not in course_dict:
        course_dict[course] = []
    course_dict[course] += [student_name]
    command = input()
for key, value in course_dict.items():
    print(f"{key}: {len(value)}")
    for element in value:
        print(f"-- {element}")