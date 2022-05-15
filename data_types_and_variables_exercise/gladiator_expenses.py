lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

count_helmet = 0
count_sword = 0
count_shield = 0
count_armour = 0
for current_number in range(1, lost_fights + 1):
    if current_number % 2 == 0:
        count_helmet += 1
    if current_number % 3 == 0:
        count_sword += 1
    if current_number % 2 == 0 and current_number % 3 == 0:
        count_shield += 1
        if count_shield % 2 == 0:
            count_armour += 1
all_sum = (count_helmet * helmet_price) + (count_sword * sword_price) + (count_shield * shield_price) + \
          (count_armour * armor_price)
print(f"Gladiator expenses: {all_sum:.2f} aureus")