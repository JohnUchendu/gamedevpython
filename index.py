import pygame
import sys
from Button import Button
from Player.Player import Player
from GameState.GameState import GameState

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DeepSkyBlue = (0, 191, 255)
GREEN = (0, 255, 0)


pygame.init()

# The SetUp of our Game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Habit Hero Game")


player = Player("Player 1")
name = "Hanson"
game_state = GameState()




start_button = Button(300, 200, 200, 50, "START", BLACK, 30, GREEN)
select_player_button = Button(550, 250, 200, 50, "Select Player >>", BLACK, 30, DeepSkyBlue)
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
        select_player_button.draw(screen)
        exit_button.draw(screen)

        # This is for either playing or exiting our game (HOME SCREEN)
        font = pygame.font.SysFont("arial", 50)
        text_surface = font.render(f"Welcome {name}!, let's get you Started", True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(text_surface, text_rect)

        pygame.display.update()

def gameplay():
    # Define challenge buttons
    select_level_button = Button(150, 20, 500, 50, "Please Select a level to Play", BLACK, 30, WHITE)
    logic_button = Button(100, 100, 200, 50, "Leve 1 Logic", BLACK, 30, GREEN)
    puzzle_button = Button(100, 200, 200, 50, "Puzzle", BLACK, 30, GREEN)
    quantitative_button = Button(100, 300, 200, 50, "Quantitative", BLACK, 30, GREEN)
    rational_button = Button(100, 400, 200, 50, "Rational", BLACK, 30, GREEN)
    current_affairs_button = Button(500, 100, 200, 50, "Current Affairs", BLACK, 30, GREEN)
    spelling_button = Button(500, 200, 200, 50, "Spelling", BLACK, 30, GREEN)
    poem_button = Button(500, 300, 200, 50, "Poem", BLACK, 30, GREEN)
    misc_button = Button(500, 400, 200, 50, "Msic", BLACK, 30, GREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # We are going to add more event handling here for user input in challenges
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if logic_button.is_clicked(mouse_pos):
                    # Implement logic challenge
                    pass
                elif puzzle_button.is_clicked(mouse_pos):
                    # Implement puzzle challenge
                    pass
                elif quantitative_button.is_clicked(mouse_pos):
                    # Implement quantitative challenge
                    pass
                elif rational_button.is_clicked(mouse_pos):
                    # Implement rational challenge
                    pass
                elif current_affairs_button.is_clicked(mouse_pos):
                    # Implement current affairs challenge
                    pass
                elif spelling_button.is_clicked(mouse_pos):
                    # Implement spelling challenge
                    pass
                # Add more elif conditions for other buttons


        screen.fill(DeepSkyBlue)
        # We may draw challenges elements here
         # Draw challenge buttons
        select_level_button.draw(screen)
        logic_button.draw(screen)
        puzzle_button.draw(screen)
        quantitative_button.draw(screen)
        rational_button.draw(screen)
        current_affairs_button.draw(screen)
        spelling_button.draw(screen)
        misc_button.draw(screen)
        poem_button.draw(screen)


        # Draw more buttons as needed
        # We will implement back  like this
        back_button = Button(20, 20, 100, 50, "Go Back", BLACK, 30, GREEN)
        # back_button = Button(20, 20, 100, 50, "Back", BLACK, 20)
        # back_button.draw(screen)

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
