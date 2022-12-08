import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.current_score = 0

    def update(self, game):
        self.current_score += 1
        if self.current_score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        message = font.render(f"Score: {self.current_score}", True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (1000, 50)
        screen.blit(message, message_rect)
