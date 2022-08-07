number = int(input())

courses_list = []

for _ in range(number):
    name_of_courses = input()
    courses_list += [name_of_courses]
print(courses_list)