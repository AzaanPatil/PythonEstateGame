# ui/hud.py

import pygame

def draw_hud(screen, game):
    font = pygame.font.SysFont(None, 28)

    y_offset = 500

    for i, player in enumerate(game.players):
        text = f"{player.name}: ${player.balance}"
        surface = font.render(text, True, (255, 255, 255))
        screen.blit(surface, (50, y_offset + i * 30))

    current = game.get_current_player()
    turn_text = f"Turn: {current.name}"
    turn_surface = font.render(turn_text, True, (255, 255, 0))
    screen.blit(turn_surface, (50, 450))