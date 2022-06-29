input_integer = list(map(int, input().split()))

removed_element_sum = 0

while len(input_integer) > 1:
    number = int(input())
    if number < 0:
        input_integer.pop(0)
        last_element = input_integer[-1]
        input_integer.insert(0, last_element)
        removed_element_sum += last_element

        for i in range(len(input_integer)):
            if input_integer[i] <= last_element:
                input_integer[i] = last_element + input_integer[i]
            else:
                input_integer[i] = abs(last_element - input_integer[i])

    elif number >= len(input_integer):
        input_integer.pop(-1)
        first_element = input_integer[0]
        input_integer.append(first_element)
        removed_element_sum += first_element

        for i in range(len(input_integer)):
            if input_integer[i] <= first_element:
                input_integer[i] = first_element + input_integer[i]
            else:
                input_integer[i] = abs(first_element - input_integer[i])

    for index in range(len(input_integer)):
        if number == index:
            removed_element = input_integer.pop(number)
            removed_element_sum += removed_element
            for el in range(len(input_integer)):
                if input_integer[el] <= removed_element:
                    input_integer[el] = removed_element + input_integer[el]
                else:
                    input_integer[el] = abs(removed_element - input_integer[el])
removed_element_sum += input_integer[0]
print(removed_element_sum)
