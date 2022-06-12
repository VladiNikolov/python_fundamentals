def josephus_permutation(elements, k):
    index = 0
    result = []

    while len(elements) > 0:
        index = (index + k - 1) % len(elements)
        result.append(elements[index])
        elements.pop(index)
    return result


numbers = input()
k = int(input())

numbers_list = numbers.split()

list_after_permutation = josephus_permutation(numbers_list, k)
string = ','.join(list_after_permutation)
print(f'[{string}]')
