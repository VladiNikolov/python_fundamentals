def absolute_values(some_list):
    abs_list = []
    for element in range(len(some_list)):
        abs_list.append(abs(some_list[element]))
    print(abs_list)

input_number = input().split()
input_number = [float(i) for i in input_number]
absolute_values(input_number)