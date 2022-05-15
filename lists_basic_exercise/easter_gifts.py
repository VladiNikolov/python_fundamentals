gift_names = input()
gift_names_list = gift_names.split()
is_no_money = False

command = input()
command_list = command.split()
while not is_no_money:
    if command_list[0] == 'OutOfStock':

        gift = command_list[1]

        for index, g in enumerate(gift_names_list):
            if g == gift:
                gift_names_list[index] = 'None'

    if command_list[0] == 'Required' and 0 <= int(command_list[2]) < len(gift_names_list):
        gift = command_list[1]

        gift_names_list[int(command_list[2])] = gift

    if command_list[0] == 'JustInCase':
        gift = command_list[1]

        gift_names_list[-1] = gift

    command = input()

    command_list = command.split()

    if command == 'No Money':

        is_no_money = True

        while 'None' in gift_names_list:
            gift_names_list.remove('None')

        break

print(' '.join(gift_names_list))
