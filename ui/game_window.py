import pygame
from ui.button import Button
from ui.hud import draw_hud


class GameWindow:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.game = game
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.roll_button.draw(self.screen)

    def render(self):
        self.screen.fill((30, 30, 30))
        header = self.font.render("Estate Empire - Press SPACE to advance turn", True, (255, 255, 255))
        self.screen.blit(header, (20, 20))

        lines = [
            f"State: {self.game.state}",
            f"Current player: {self.game.get_current_player().name if self.game.get_current_player() else 'None'}",
            f"Pending property: {self.game.pending_property.name if self.game.pending_property else 'None'}",
        ]

        for index, player in enumerate(self.game.players):
            lines.append(
                f"{player.name}: ${player.balance} | Properties: {len(player.properties)}"
            )

        for i, line in enumerate(lines, start=1):
            text_surface = self.font.render(line, True, (220, 220, 220))
            self.screen.blit(text_surface, (20, 60 + i * 28))

        event_lines = self.game.events[-8:]
        for index, event in enumerate(event_lines):
            text_surface = self.font.render(event, True, (180, 180, 180))
            self.screen.blit(text_surface, (20, 320 + index * 26))

        pygame.display.flip()
