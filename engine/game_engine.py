from engine.turn_manager import TurnManager
from systems.card_deck import CardDeck
from systems.cpu import CPUAI
from systems.economy import buy_property, pay_rent


class GameEngine:
    def __init__(self, start_bonus=2000):
        self.players = []
        self.board = None
        self.turn_manager = None
        self.card_deck = None
        self.start_bonus = start_bonus
        self.pending_property = None
        self.events = []
        self.cpu_ai = CPUAI()
        self.state = "MENU"

    def start_game(self, players, board, card_deck: CardDeck):
        self.players = list(players)
        self.board = board
        self.turn_manager = TurnManager(self.players)
        self.card_deck = card_deck
        self.pending_property = None
        self.events = []
        self.state = "PLAYING"
        self.record_event("Game started.")

    def record_event(self, message):
        self.events.append(message)

    def get_current_player(self):
        return self.turn_manager.get_current_player()

    def play_turn(self):
        if self.state != "PLAYING":
            return

        player = self.get_current_player()
        if player is None or player.is_bankrupt:
            return

        self.pending_property = None
        steps = player.roll_dice()
        self.record_event(f"{player.name} rolled {steps}.")

        tile, passed_start = self.board.move_player(player, steps)
        if passed_start:
            player.receive(self.start_bonus)
            self.record_event(f"{player.name} passed Start and received ${self.start_bonus}.")

        self.record_event(f"{player.name} landed on {tile.name}.")
        tile.on_land(player, self)
        self.check_bankruptcy(player)

        if not self.is_game_over():
            self.turn_manager.advance()
        else:
            self.state = "ENDED"
            winner = self.get_winner()
            if winner:
                self.record_event(f"{winner.name} wins the game!")

    def handle_cpu_purchase(self, player, property):
        if self.cpu_ai.decide_purchase(player, property):
            buy_property(player, property)
            self.record_event(f"{player.name} bought {property.name} for ${property.price}.")
        else:
            self.record_event(f"{player.name} declined to buy {property.name}.")

    def purchase_pending_property(self):
        player = self.get_current_player()
        if self.pending_property and player.can_afford(self.pending_property.price):
            buy_property(player, self.pending_property)
            self.record_event(
                f"{player.name} purchased {self.pending_property.name} for ${self.pending_property.price}."
            )
        self.pending_property = None

    def skip_purchase(self):
        self.pending_property = None

    def handle_rent(self, player, property):
        if pay_rent(player, property):
            self.record_event(
                f"{player.name} paid ${property.rent} in rent to {property.owner.name}."
            )

    def check_bankruptcy(self, player):
        if player.balance < 0:
            player.is_bankrupt = True
            self.turn_manager.remove_player(player)
            self.record_event(f"{player.name} is bankrupt and eliminated.")

    def is_game_over(self):
        return len(self.turn_manager.players) <= 1

    def get_winner(self):
        players = self.turn_manager.players
        return players[0] if len(players) == 1 else None
