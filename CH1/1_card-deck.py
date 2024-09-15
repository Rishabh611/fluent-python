import collections
from random import choice


Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11) ] + list("JQKA")
    suits = 'spades hearts diamond club'.split()
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f'Card(rank=\'{self.rank}\', suit=\'{self.suit}\')'

beer_card = Card("7", 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(choice(deck))