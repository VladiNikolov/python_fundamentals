username_diary = {}
student_diary = {}
command = input()

while command != "exam finished":
    current_command = command.split("-")
    if current_command[1] == 'banned':
        user = current_command[0]
        del username_diary[user]
    else:
        user, language, points = current_command
        points = int(points)
        if user in username_diary:
            if username_diary[user] < points:
                username_diary[user] = points
        else:
            username_diary[user] = points

        if language not in student_diary:
            student_diary[language] = 0
        student_diary[language] += 1

    command = input()
print("Results:")
for key, value in username_diary.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in student_diary.items():
    print(f'{key} - {value}')


