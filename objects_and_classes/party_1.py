class Party:
    def __init__(self):
        self.people = []
party = Party()

input_lines = input()
while input_lines != "End":
    party.people.append(input_lines)

    input_lines = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")