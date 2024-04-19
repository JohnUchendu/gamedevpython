import pygame
BLACK = (0, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text, color, font_size, text_color = BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color = color
        self.font_size = font_size
        self.font = pygame.font.SysFont("arial", font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)