fires_with_their_cells = input().split("#")
water = int(input())
total_fire = 0

print("Cells:")
for current_element in fires_with_their_cells:
    info_cells = current_element.split(" = ")
    type_of_fire = info_cells[0]
    needed_water = int(info_cells[1])

    if type_of_fire == "High" and 81 <= needed_water <= 125 and water >= needed_water:
        water -= needed_water
        total_fire += needed_water
        print(f" - {needed_water}")
    elif type_of_fire == "Medium" and 51 <= needed_water <= 80 and water >= needed_water:
        water -= needed_water
        total_fire += needed_water
        print(f" - {needed_water}")
    elif type_of_fire == "Low" and 1 <= needed_water <= 50 and water >= needed_water:
        water -= needed_water
        total_fire += needed_water
        print(f" - {needed_water}")

print(f"Effort: {total_fire * 0.25:.2f}")
print(f"Total Fire: {total_fire}")
