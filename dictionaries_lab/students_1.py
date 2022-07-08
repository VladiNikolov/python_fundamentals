text = input()
courses_dict = {}

while ':' in text:

    data = text.split(':')
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses_dict.keys():
        courses_dict[course] = {}

    courses_dict[course][id] = name

    text = input()

text = text.replace('_', ' ')

for id in courses_dict[text]:
    print(f'{courses_dict[text][id]} - {id}')