quantity_food_kg = float(input())
quantity_hay_kg = float(input())
quantity_cover_kg = float(input())
pig_kg = float(input())
is_food_enough = True

quantity_food_grams = quantity_food_kg * 1000
quantity_hay_grams = quantity_hay_kg * 1000
quantity_cover_grams = quantity_cover_kg * 1000
pig_grams = pig_kg * 1000

for day in range(1, 30 + 1):
    quantity_food_grams -= 300
    if quantity_food_grams <= 0 or quantity_hay_grams <= 0 or quantity_cover_grams <= 0:
        print("Merry must go to the pet store!")
        is_food_enough = False
        break

    if day % 2 == 0:
        used_hay = (quantity_food_grams * 5) / 100
        quantity_hay_grams -= used_hay
    if day % 3 == 0:
        quantity_cover_grams -= (pig_grams / 1/3)
        quantity_cover_grams = round(quantity_cover_grams, 2)
if is_food_enough:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_grams / 1000:.2f}, "
          f"Hay: {quantity_hay_grams / 1000:.2f}, Cover: {quantity_cover_grams / 1000:.2f}.")


