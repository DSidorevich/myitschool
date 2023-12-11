number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
card_deck = []

for item in number:
    for item1 in suit:
        card_deck.append(item + ' ' + item1)
# print(card_deck)

# card_deck = [n + ' ' + s for n in number for s in suit]
# print(card_deck)

card_deck_iter = iter(card_deck)
while True:
    try:
        print(next(card_deck_iter))
    except StopIteration:
        break





