import sys


def is_valid_index(collection: list, index: int):
    if 0 <= index < len(collection):
        return True

    return False


def exchange_list_at_index(collection: list, index: int):
    exchanged_list = []

    if not is_valid_index(collection, index):
        print("Invalid index")
        exchanged_list = collection
    else:
        left_sub_list = collection[:index + 1]
        right_sub_list = collection[index + 1:]

        for el in right_sub_list:
            exchanged_list.append(el)

        for el in left_sub_list:
            exchanged_list.append(el)

    return exchanged_list

def max_num_by_criteria(collection: list, custom_filter):
    max_element = float("-inf")
    max_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if custom_filter(num) and num >= max_element:
            max_element = num
            max_element_index = i
    if max_element_index == -1:
        print("No matches")

    return max_element_index

def min_num_by_criteria(collection: list, custom_filter):
    min_element = sys.maxsize
    min_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if custom_filter(num) and num <= min_element:
            min_element = num
            min_element_index = i

    if min_element_index == -1:
        print("No matches")

    return min_element_index

def first_count_elements_by_criteria(collection: list, count: int, custom_filter):
    if count > len(collection):
        print("Invalid count")
    else:
        matching_elements = []

        for num in collection:
            if custom_filter(num) and len(matching_elements) < count:
                matching_elements.append(num)
        print(matching_elements)


def last_count_element_by_criteria(collection: list, count: int, custom_filter):
    if count > len(collection):
        print("Invalid count")
    else:
        matching_elements = []

        for i in range(len(collection) - 1, -1 , -1):
            num = collection[i]

            if custom_filter(num) and len(matching_elements) < count:
                matching_elements.append(num)
        print(matching_elements[::-1])


def parse_collection_to_int(collection: list):
    parsed_collection = []

    for el in collection:
        parsed_collection.append(int(el))

    return parsed_collection

def stringify_collection(collection: list, delimiter: str):
    parsed_collection = []

    for num in collection:
        parsed_collection.append(str(num))

    return delimiter.join(parsed_collection)


elements = input().split()
numbers = parse_collection_to_int(elements)

command = input()
while command != "end":
    cmd_args = command.split()
    cmd_type = cmd_args[0]

    if cmd_type == "exchange":
        index = int(cmd_args[1])

        numbers = exchange_list_at_index(numbers, index)
    elif cmd_type == "max":
        cmd_filter = cmd_args[1]

        max_index = -1

        if cmd_filter == "even":
            max_index = max_num_by_criteria(numbers, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            max_index = max_num_by_criteria(numbers, lambda n: n % 2 != 0)

        if max_index != -1:
            print(max_index)

    elif cmd_type == "min":
        cmd_filter = cmd_args[1]

        min_index = -1

        if cmd_filter == "even":
            min_index = min_num_by_criteria(numbers, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            min_index = min_num_by_criteria(numbers, lambda n: n % 2 != 0)

        if min_index != -1:
            print(min_index)

    elif cmd_type == "first":
        count = int(cmd_args[1])
        cmd_filter = cmd_args[2]

        if cmd_filter == "even":
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 != 0)

    elif cmd_type == "last":
        count = int(cmd_args[1])
        cmd_filter = cmd_args[2]

        if cmd_filter == "even":
            last_count_element_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            last_count_element_by_criteria(numbers, count, lambda n: n % 2 != 0)

    command = input()

print(f"[{stringify_collection(numbers, ', ')}]")