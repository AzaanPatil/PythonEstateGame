import random


class CardDeck:
    def __init__(self, cards):
        self.cards = list(cards)
        self.reset()

    def draw(self):
        if not self.deck:
            self.reset()
        return self.deck.pop()

    def reset(self):
        self.deck = list(self.cards)
        random.shuffle(self.deck)
