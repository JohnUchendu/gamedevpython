import pygame
import sys
from Button import Button
from Player.Player import Player
from GameState.GameState import GameState
from Challenges.logic_quiz import QuizQuestions
from Challenges.puzzle_quiz import PuzzleQuestions

QUIT = pygame.image.load('images\\images\\quit.jpeg')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DeepSkyBlue = (0, 191, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
GRAY1 = (140, 140, 140)
LIGHTBLUE = (134, 180, 152)
SELECT_GAME = (26,  60,  62)
WELCOME_SCREEN = (26,60,62)
WELCOME_SCREEN1 = (26,50,62)
GAME_BACK =  (134, 180, 152)
FAMILY = "BLANKA Font\\Blanka-Regular.otf"


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Habit Hero Game")


player = Player("")
name = player.name
game_state = GameState()

start_button = Button(50, 300, 150, 50, "START", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)
select_player_button = Button(250, 300, 330, 50, "SELECT PLAYER >>", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)
exit_button = Button(600, 300, 150, 50, "EXIT", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)



def menu_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for button in [start_button, select_player_button, exit_button]:
                    button.update_hover(mouse_pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    game_state.change_state("gameplay")
                elif exit_button.is_clicked(mouse_pos):
                    screen.blit(QUIT, (0, 0))  # Display the QUIT image
                    pygame.display.update()
                    pygame.time.delay(10000)  # Delay for 2 seconds
                    # pygame.quit()
                    # sys.exit()

        screen.fill(WELCOME_SCREEN)
        start_button.draw(screen)
        select_player_button.draw(screen)
        exit_button.draw(screen)

        font = pygame.font.SysFont(FAMILY, 120)
        text1_surface = font.render(f"WELCOME BACK", True, WHITE)
        text2_surface = font.render(f"{name}", True, WHITE)
        
        text1_rect = text1_surface.get_rect(midtop=(SCREEN_WIDTH // 2, 100))
        text2_rect = text2_surface.get_rect(midtop=(SCREEN_WIDTH // 2, text1_rect.bottom + 10))

        screen.blit(text1_surface, text1_rect)
        screen.blit(text2_surface, text2_rect)

        pygame.display.update()


def main():
    while True:
        if game_state.state == "menu":
            print(game_state.state)
            menu_screen()
        elif game_state.state == "gameplay":
            print(game_state.state)

if __name__ == "__main__":
    main()
