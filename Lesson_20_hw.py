number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
card_deck = []

for item in number:   # Создание итерируемого объекта. Вариант 1
    for item1 in suit:
        card_deck.append(item + ' ' + item1)
# print(card_deck)

# card_deck = [n + ' ' + s for n in number for s in suit]  # Создание итерируемого объекта. Вариант 2
# print(card_deck)

# card_deck_iter = iter(card_deck)  # Вариант 1. Создание итератора.
# while True:
#     try:
#         print(next(card_deck_iter))
#     except StopIteration:
#         break


class MyIterator:    # Вариант 2. Создание итератора через класс.

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        itm = self.data[self.index]
        self.index += 1
        return itm


CardDeck = MyIterator(card_deck)  # создаем объект класса итератора

CardDeck_iter = iter(CardDeck)  # проход по объекту итератора c помощью метода iter

while True:
    try:
        print(next(CardDeck_iter))  # вызываем элемент итерируемого объекта
    except StopIteration:
        break

