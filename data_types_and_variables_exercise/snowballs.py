number_of_snowballs = int(input())

count_snowball_value = 0
best_snowball = ""
for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > count_snowball_value:
        count_snowball_value = snowball_value
        best_snowball = f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

print(best_snowball)