input_string = input().split()
count_of_shuffle = int(input())
shuffled_cards = []

for shuffle in range(count_of_shuffle):
    shuffled_cards = []
    middle_of_cards = len(input_string) // 2
    left_cards = input_string[0:middle_of_cards]
    right_cards = input_string[middle_of_cards::]
    for index in range(len(left_cards)):
        shuffled_cards.append(left_cards[index])
        shuffled_cards.append(right_cards[index])
        input_string = shuffled_cards
print(shuffled_cards)


