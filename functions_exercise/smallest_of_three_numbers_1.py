def smallest_of_three_numbers(elements_in_list: list):
    return min(elements_in_list)

first_number = int(input())
second_number = int(input())
third_number = int(input())

my_list = []
my_list.append(first_number)
my_list.append(second_number)
my_list.append(third_number)
min_element_in_list = min(my_list)
print(min_element_in_list)
