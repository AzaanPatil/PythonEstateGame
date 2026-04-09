# ui/board_renderer.py

import pygame

TILE_SIZE = 80
GRID_SIZE = 5

def render_board(screen, game):
    tiles = game.board.tiles

    for i, tile in enumerate(tiles):
        row = i // GRID_SIZE
        col = i % GRID_SIZE

        x = col * TILE_SIZE + 50
        y = row * TILE_SIZE + 50

        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

        # Color based on type
        if tile.tile_type == "property":
            color = (100, 200, 100)
        elif tile.tile_type == "tax":
            color = (200, 100, 100)
        elif tile.tile_type == "card":
            color = (100, 100, 200)
        else:
            color = (200, 200, 200)

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 2)

    draw_players(screen, game)


def draw_players(screen, game):
    for player in game.players:
        index = player.position

        row = index // GRID_SIZE
        col = index % GRID_SIZE

        x = col * TILE_SIZE + 90
        y = row * TILE_SIZE + 90

        pygame.draw.circle(screen, (255, 255, 0), (x, y), 10)