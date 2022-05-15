# animals = input()
# animals_list = animals.split(', ')
# animals_list.reverse()
# for index, animal in enumerate(animals_list):
#     if animal == 'wolf' and index == 0:
#         print('Please go away and stop eating my sheep')
#     elif animal == 'wolf':
#         print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
#

animals = input()
animals_list = []

for animal in animals.split(","):
    animals_list.append(str(animal).strip())

farmer_position = len(animals_list) + 1
if animals_list[-1].strip() == "wolf":
    print("Please go away and stop eating my sheep")
else:
    animal_position = len(animals_list) - animals_list.index("wolf") - 1
    print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")
