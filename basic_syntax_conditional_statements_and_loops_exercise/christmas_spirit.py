quantity = int(input())
days = int(input())

total_sum = 0
total_spirit = 0
condition_5th_day = False

for current_day in range(1, days + 1):
    condition_5th_day = False

    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_sum += quantity * 2
        total_spirit += 5

    if current_day % 3 == 0:
        total_sum += (quantity * 3) + (quantity * 5)
        total_spirit += 13
        condition_5th_day = True

    if current_day % 5 == 0:
        total_sum += quantity * 15
        total_spirit += 17
        if condition_5th_day:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_sum += 23

        if current_day == days:
            total_spirit -= 30
print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")



