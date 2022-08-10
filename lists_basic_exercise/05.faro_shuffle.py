deck_of_cards = input().split()
number_of_shuffle = int(input())

for shuffle in range(number_of_shuffle):
    final_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    left_middle = deck_of_cards[0:middle_of_deck]
    right_middle = deck_of_cards[middle_of_deck::]
    for index_in_card in range(len(left_middle)):
        final_deck.append(left_middle[index_in_card])
        final_deck.append(right_middle[index_in_card])
    deck_of_cards = final_deck
print(deck_of_cards)
        

