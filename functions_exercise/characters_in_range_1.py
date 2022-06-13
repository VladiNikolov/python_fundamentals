def characters_in_range(start: str, end: str):
    for elements in range(ord(start) + 1, ord(end)):
        print(f"{chr(elements)}", end =" " )


first_input = input()
second_input = input()
characters_in_range(first_input, second_input)
