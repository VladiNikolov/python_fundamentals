factor = int(input())
count = int(input())

my_list = []
while count > 0:
    current_element = count * factor
    my_list.append(current_element)
    count -= 1
my_list.reverse()
print(my_list)

