import pygame
import sys
from Button import Button
from Player.Player import Player
from GameState.GameState import GameState

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


pygame.init()

# The SetUp of our Game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Habit Hero Game")


player = Player("Player 1")
game_state = GameState()



start_button = Button(300, 200, 200, 50, "START", BLACK, 30, GREEN)
exit_button = Button(300, 300, 200, 50, "EXIT", BLACK, 30, RED)

def menu_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    game_state.change_state("gameplay")
                    gameplay()
                elif exit_button.is_clicked(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        start_button.draw(screen)
        exit_button.draw(screen)

        # This is for either playing or exiting our game (HOME SCREEN)
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Wanna to Play, let's get you Started", True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(text_surface, text_rect)

        pygame.display.update()

def gameplay():
    print('Game Play started')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # We are going to add more event handling here for user input in challenges

        screen.fill(RED)
        # We may draw challenges elements here

        # We will implement back  like this
        back_button = Button(20, 20, 100, 50, "Go Back", BLACK, 30, GREEN)
        # back_button = Button(20, 20, 100, 50, "Back", BLACK, 20)
        back_button.draw(screen)

        pygame.display.update()

def main():
    while True:
        if game_state.state == "menu":
            print(game_state.state)
            menu_screen()
        elif game_state.state == "gameplay":
            print(game_state.state)
            gameplay()

if __name__ == "__main__":
    main()
