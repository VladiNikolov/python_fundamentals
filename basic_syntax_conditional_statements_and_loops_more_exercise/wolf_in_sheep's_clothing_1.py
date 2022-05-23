input_string = input().split(", ")
input_string.reverse()
count_sheep = 0
for element in range(len(input_string)):
    if element == 0 and input_string[element] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if input_string[element] == "sheep":
        count_sheep += 1
        continue
    else:
        print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")

