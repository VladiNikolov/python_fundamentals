population = input().split(", ")
population = [int(i) for i in population]
minimum_wealth = int(input())
no_equal = False

if len(population) * minimum_wealth > sum(population):
    no_equal = True
else:
    for element in range(len(population)):
        index_max_element = population.index(max(population))
        if population[element] < minimum_wealth:
            result = minimum_wealth - population[element]
            population[index_max_element] -= result
            population[element] += result
if no_equal:
    print(f"No equal distribution possible")
else:
    print(population)

