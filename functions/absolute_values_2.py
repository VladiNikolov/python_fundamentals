def absolute_values(some_list):
    abs_list = []
    for element in range(len(some_list)):
        if some_list[element] < 0:
            abs_list.append(abs(some_list[element]))
        else:
            abs_list.append(float(some_list[element]))
    return abs_list

input_number = input().split()
input_number = [float(i) for i in input_number]
print(absolute_values(input_number))