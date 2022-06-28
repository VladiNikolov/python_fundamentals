numbers = list(map(int, input().split()))
removed_elements = []

while len(numbers) > 0:
    index = int(input())
    if index < 0:
        element = numbers.pop(0)
        removed_elements.append(element)
        last_element = numbers[-1]
        numbers.insert(0, last_element)
    elif index >= len(numbers):
        element = numbers.pop(-1)
        removed_elements.append(element)
        first_element = numbers[0]
        numbers.append(first_element)
    else:
        element = numbers.pop(index)
        removed_elements.append(element)

    numbers = [element + num if num <= element else num - element for num in numbers]

print(sum(removed_elements))