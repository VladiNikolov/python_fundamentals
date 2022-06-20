notes = [0] * 10

command = input()

while not command == "End":
    number, text = command.split("-")
    current_index = int(number) - 1
    notes[current_index] = text

    command = input()
print([el for el in notes if el != 0])