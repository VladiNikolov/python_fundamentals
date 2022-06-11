def rounding_func(number):
    my_list = []
    for element in range(len(number)):
        my_list.append(round(number[element]))
    return my_list

input_numbers = input().split()
input_numbers = [float(i) for i in input_numbers]
print(rounding_func(input_numbers))