number_of_people = int(input())
capacity = int(input())
courses = number_of_people // capacity
if number_of_people < capacity:
    courses = 1
    print(courses)
elif number_of_people % courses == 0:
    print(courses)
else:
    print(f"{courses + 1}")
