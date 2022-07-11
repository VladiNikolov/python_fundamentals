courses_dict = {}

command = input()
while command != "end":
    current_command = command.split(" : ")
    courses = current_command[0]
    student_name = current_command[1]
    if courses not in courses_dict:
        courses_dict[courses] = []
        courses_dict[courses].append(student_name)
    else:
        courses_dict[courses].append(student_name)
    command = input()
for courses in courses_dict.keys():
    print(f"{courses}: {len(courses_dict[courses])}")
    for student_name in courses_dict[courses]:
        print(f"-- {student_name}")
