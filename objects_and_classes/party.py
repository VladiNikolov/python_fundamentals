class Party:
    def __init__(self):
        self.people = []
party = Party()

total_people_going = 0
input_lines = input()
while input_lines != "End":
    party.people.append(input_lines)
    total_people_going += 1
    input_lines = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people_going}")
