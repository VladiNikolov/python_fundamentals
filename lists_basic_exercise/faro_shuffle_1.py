cards = input().split()
number_of_shuffles = int(input())
final_deck = []

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    left_half = cards[0:middle_of_the_deck]
    right_half = cards[middle_of_the_deck::]
    for index_of_the_card in range(len(left_half)):
        final_deck.append(left_half[index_of_the_card])
        final_deck.append(right_half[index_of_the_card])

    cards = final_deck
print(final_deck)


