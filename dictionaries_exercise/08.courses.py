course_dict = {}

while True:
    command = input()
    if command == "end":
        break
    else:
        data_info = command.split(" : ")
        courses = data_info[0]
        student_name = data_info[1]

        if courses not in course_dict:
            course_dict[courses] = []
            course_dict[courses].append(student_name)
        else:
            course_dict[courses].append(student_name)
for keys, value in course_dict.items():
    print(f"{keys}: {(len(value))}")
    for el in value:
        print(f"-- {el}")




