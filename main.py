from engine.game_engine import GameEngine
from models.board import Board
from models.card import Card
from models.property import Property
from models.player import Player
from models.tile import StartTile, TaxTile, CardTile, PropertyTile
from systems.card_deck import CardDeck
from ui.game_window import GameWindow
from data.dataset_loader import load_properties


def create_sample_cards():
    return [
        Card("Collect a rent rebate.", lambda player, game: player.receive(500)),
        Card("Pay city insurance.", lambda player, game: player.pay(300)),
        Card("You won a local contest! Collect prize money.", lambda player, game: player.receive(700)),
        Card("Repair fees are due.", lambda player, game: player.pay(400)),
    ]


def create_default_board():
    # Load properties from the dataset using ML predictions
    properties = load_properties()
    
    # Create tiles: Start, Property, Tax, Card, Property, Tax, Property, Card, Property, Tax
    tiles = [
        StartTile(),
        PropertyTile(properties[0]) if len(properties) > 0 else PropertyTile(Property("Default Property", 1000, 100)),
        TaxTile(200, "City maintenance fee"),
        CardTile(),
        PropertyTile(properties[1]) if len(properties) > 1 else PropertyTile(Property("Default Property 2", 1500, 150)),
        TaxTile(300, "Property tax"),
        PropertyTile(properties[2]) if len(properties) > 2 else PropertyTile(Property("Default Property 3", 2000, 200)),
        CardTile(),
        PropertyTile(properties[3]) if len(properties) > 3 else PropertyTile(Property("Default Property 4", 2500, 250)),
        TaxTile(400, "Luxury tax"),
    ]
    return Board(tiles)


def create_default_players():
    return [
        Player("You", is_cpu=False, difficulty="medium"),
        Player("Estate Bot", is_cpu=True, difficulty="medium"),
    ]


def main():
    engine = GameEngine()
    board = create_default_board()
    card_deck = CardDeck(create_sample_cards())
    players = create_default_players()
    engine.start_game(players, board, card_deck)

    window = GameWindow(engine)
    window.run()


if __name__ == "__main__":
    main()
