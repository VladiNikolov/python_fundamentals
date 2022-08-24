number_of_people = int(input())
lift_state = input().split()
lift_state = [int(i) for i in lift_state]

for index in range(len(lift_state)):
    if number_of_people > 3:
        current_people = abs(4 - int(lift_state[index]))
        number_of_people -= current_people
        lift_state[index] += current_people
    else:
        lift_state[index] += number_of_people
        number_of_people = 0

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
elif sum(lift_state) != len(lift_state) * 4:
    print(f"The lift has empty spots!")
print(" ".join([str(num) for num in lift_state]))

