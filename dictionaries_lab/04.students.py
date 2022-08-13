input_line = input()
students_dict = {}

while ":" in input_line:
    data_info = input_line.split(":")
    name = data_info[0]
    ID = data_info[1]
    course = data_info[2]

    if course not in students_dict.keys():
        students_dict[course] = {}
    students_dict[course][ID] = name

    input_line = input()
input_line = input_line.replace("_", " ")
print(students_dict[input_line])
for ID in students_dict[input_line]:
    print(f"{students_dict[input_line][ID]} - {ID}")
