number = int(input())
courses_list = []

while number > 0:
    name_courses = input()
    courses_list.append(name_courses)
    number -= 1
print(courses_list)