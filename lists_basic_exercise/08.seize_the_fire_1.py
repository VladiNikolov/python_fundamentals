fire_cells = input().split("#")
water = int(input())
sum_water = 0

print("Cells:")
for cells in range(len(fire_cells)):
    info_cells = fire_cells[cells].split(" = ")
    type_of_fire = info_cells[0]
    value = int(info_cells[1])

    if type_of_fire == "High" and 81 <= value <= 125 and water - value >= 0:
        water -= value
        sum_water += value
        print(f"- {value}")

    elif type_of_fire == "Medium" and 51 <= value <= 80 and water - value >= 0:
        water -= value
        sum_water += value
        print(f"- {value}")

    elif type_of_fire == "Low" and 1 <= value <= 50 and water - value >= 0:
        water -= value
        sum_water += value
        print(f"- {value}")
print(f"Effort: {sum_water * 0.25:.2f}")
print(f"Total Fire: {sum_water}")