animals = input()
animals_list = animals.split(', ')
animals_list.reverse()
for index, animal in enumerate(animals_list):
    if animal == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
    elif animal == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')


