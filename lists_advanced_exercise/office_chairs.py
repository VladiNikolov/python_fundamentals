number_of_rooms = int(input())

count_current_room = 0
free_chairs = 0
needed_chairs = 0

while number_of_rooms > 0:
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])

    difference = chairs - visitors
    if difference >= 0:
        free_chairs += difference
        count_current_room += 1
    else:
        needed_chairs += abs(difference)
        count_current_room += 1
        print(f"{abs(difference)} more chairs needed in room {count_current_room}")
    number_of_rooms -= 1
if free_chairs >= needed_chairs:
    print(f"Game On, {abs(free_chairs)} free chairs left")
