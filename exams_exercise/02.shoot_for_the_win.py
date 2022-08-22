targets_sequence = input().split()
targets_sequence = list(map(int, targets_sequence))
count_shoot = 0
command = input()
while command != "End":
    index = int(command)
    if 0 <= index < len(targets_sequence):
        element = targets_sequence[index]
        targets_sequence[index] = -1
        count_shoot += 1

        for index_element in range(len(targets_sequence)):
            if targets_sequence[index_element] == -1:
                continue

            elif targets_sequence[index_element] > element:
                targets_sequence[index_element] -= element

            elif targets_sequence[index_element] <= element:
                targets_sequence[index_element] += element
        pass
    command = input()
targets_sequence = [str(i) for i in targets_sequence]
print(f"Shot targets: {count_shoot} -> {' '.join(targets_sequence)}")