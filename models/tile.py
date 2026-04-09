from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.game_engine import GameEngine

from models.property import Property
from models.player import Player


class Tile(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def on_land(self, player: Player, game: "GameEngine"):
        pass


class StartTile(Tile):
    def __init__(self, name="Start"):
        super().__init__(name)

    def on_land(self, player, game):
        player.receive(game.start_bonus)
        game.record_event(f"{player.name} landed on {self.name} and received ${game.start_bonus}.")


class TaxTile(Tile):
    def __init__(self, amount: int, name="Tax"):
        super().__init__(name)
        self.amount = amount

    def on_land(self, player, game):
        player.pay(self.amount)
        game.record_event(f"{player.name} paid ${self.amount} in taxes.")


class CardTile(Tile):
    def __init__(self, name="Card"):
        super().__init__(name)

    def on_land(self, player, game):
        card = game.card_deck.draw()
        card.apply(player, game)
        game.record_event(f"{player.name} drew a card: {card.description}")


class PropertyTile(Tile):
    def __init__(self, property: Property):
        super().__init__(property.name)
        self.property = property

    def on_land(self, player, game):
        if not self.property.is_owned():
            if player.is_cpu:
                game.handle_cpu_purchase(player, self.property)
            else:
                game.pending_property = self.property
                game.record_event(
                    f"{player.name} landed on {self.property.name}. It is available for ${self.property.price}."
                )
        elif self.property.owner != player:
            game.handle_rent(player, self.property)
        else:
            game.record_event(f"{player.name} landed on their own property {self.property.name}.")
