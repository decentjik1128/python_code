import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def printinf(self):
        print(self._cards)

beer_card = Card('7', 'diamonds')
print(beer_card)

print(FrenchDeck.ranks)
print(FrenchDeck.suits)

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(deck.printinf())

from random import choice

print(choice(deck))
print(choice(deck))
print(choice(deck))
