class Card:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect

    def apply(self, player, game):
        self.effect(player, game)
