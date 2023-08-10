import pygame
from settings import *

class GameOverScreen:
    def __init__(self, display_surface, score):
        self.display_surface = display_surface
        self.font = pygame.font.Font(None, 36)
        self.text_color = LINE_COLOR
        self.background_color = GRAY
        self.score = score

    def draw(self):
        self.display_surface.fill(self.background_color)
        text = self.font.render("Game Over", True, self.text_color)
        text_rect = text.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 30))
        self.display_surface.blit(text, text_rect)

        score_text = self.font.render(f"Score: {self.score}", True, self.text_color)
        score_rect = score_text.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 30))
        self.display_surface.blit(score_text, score_rect)
