import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
GAME_BACK =  (134, 200, 152)

class Button:
    def __init__(self, x, y, width, height, text, color, font_size, text_color=BLACK, hover_color=GAME_BACK, border_radius=14):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color = color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font = pygame.font.SysFont("BLANKA Font\\Blanka-Regular.otf", font_size)
        self.border_radius = border_radius
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=self.border_radius)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False
