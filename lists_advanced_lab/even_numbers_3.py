input_list = input().split(", ")
input_list = [int(i) for i in input_list]

even_index = [el for el in range(len(input_list)) if input_list[el] % 2 == 0]
print(even_index)