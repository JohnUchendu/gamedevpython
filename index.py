import pygame
import sys
from Button import Button
from Player.Player import Player
from GameState.GameState import GameState
from Challenges.logic_quiz import QuizQuestions
from Challenges.puzzle_quiz import PuzzleQuestions
from Challenges.current_affair import CURRENTAFFAIRS
import random


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
# The SetUp of our Game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Habit Hero Game")


player = Player("")
name = player.name

# List of registered player names
# Function to read player names from file
def read_players_from_file(filename):
    with open(filename, "r") as file:
        players = [line.strip() for line in file]
    return players

# Read player names from file
registered_players = read_players_from_file("Player\\players.txt")
# Create buttons for registered players
player_buttons = []
for i, player_name in enumerate(registered_players):
    button = Button(250, 150 + i * 50, 300, 40, player_name, WELCOME_SCREEN, 30, WHITE, WELCOME_SCREEN1)
    player_buttons.append(button)

# Input box for creating a new player
input_box = pygame.Rect(250, 150 + len(registered_players) * 50, 300, 40)
input_text = ""
input_active = False

game_state = GameState()

start_button = Button(50, 300, 150, 50, "START", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)
select_player_button = Button(250, 300, 330, 50, "SELECT PLAYER >>", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)
exit_button = Button(600, 300, 150, 50, "EXIT", WELCOME_SCREEN, 45, WHITE, WELCOME_SCREEN1)

yes_button = Button(600, 300, 150, 50, "NO", WELCOME_SCREEN, 45, RED, RED)
no_button = Button(600, 300, 150, 50, "YES", WELCOME_SCREEN, 45, RED, RED)

QUIT = pygame.image.load('assets\\images\\quit.jpeg')
LOADING = pygame.image.load('assets\\images\\loading.jpeg')
ZERO_HERO = pygame.image.load('assets\\images\\zero_to_hero.jpeg')
MUSIC = pygame.mixer.music.load('assets\\audio\\superhero-trailer-110450.mp3')
# Set the window icon
icon = pygame.image.load('assets\\images\\icon.jpeg')
pygame.display.set_icon(icon)

def menu_screen():
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Main Menu")
    quit_confirmation = False  # Flag to track whether the quit confirmation is active
    

    screen.blit(LOADING, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(ZERO_HERO, (0, 0))
    pygame.mixer.music.play(-1)  # -1 loops the music indefinitely
    pygame.display.update()
    pygame.time.delay(1500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for button in [start_button,select_player_button,exit_button]:  # Assuming buttons_list contains instances of your Button class
                    button.update_hover(mouse_pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    game_state.change_state("gameplay")
                    gameplay()
                elif exit_button.is_clicked(mouse_pos):
                    quit_confirmation = True 
                elif select_player_button.is_clicked(mouse_pos):
                    game_state.change_state("select_player")
                    player_selection_screen() # Return mouse position when select_player_button is clicked

                        

        screen.fill(WELCOME_SCREEN)
        start_button.draw(screen)
        select_player_button.draw(screen)
        exit_button.draw(screen)

        # This is for either playing or exiting our game (HOME SCREEN)
        font = pygame.font.SysFont(FAMILY, 120)
        text1_surface = font.render(f"WELCOME BACK", True, WHITE)
        text2_surface = font.render(f"{name}", True, WHITE)
        
        # Get the rects of the rendered texts
        text1_rect = text1_surface.get_rect(midtop=(SCREEN_WIDTH // 2, 100))
        text2_rect = text2_surface.get_rect(midtop=(SCREEN_WIDTH // 2, text1_rect.bottom + 10))

        # Blit the text surfaces onto the screen
        screen.blit(text1_surface, text1_rect)
        screen.blit(text2_surface, text2_rect)

        # Quit confirmation logic
        if quit_confirmation:
            screen.blit(QUIT, (0, 0))  # Display the QUIT image
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(mouse_pos)
                    # Check if the mouse click is within the specified area on the QUIT image
                    if 246 <= mouse_pos[0] <= 428 and 436 <= mouse_pos[1] <= 491:
                        pygame.quit()
                        sys.exit()
                    elif 446 <= mouse_pos[0] <= 466 and 436 <= mouse_pos[1] <= 491:
                        return
                    else:
                        quit_confirmation = False  # Deactivate quit confirmation
        # Stop playing background music
        
        pygame.display.update()

def gameplay():
    pygame.display.set_caption("Game Menu")
    back_button = Button(100, 450, 100, 50, "BACK", SELECT_GAME, 30, WHITE, GRAY, 10) 
    # Define challenge buttons
    hero_button = Button(150, 60, 500, 50, "BE THE HERO TODAY", SELECT_GAME, 40, WHITE, SELECT_GAME, 16)
    select_level_button = Button(150, 100, 500, 50, "SELECT TO PLAY", SELECT_GAME, 40, WHITE, SELECT_GAME, 16)

    logic_quiz_button = Button(100, 200, 135, 60, "Logic", GAME_BACK, 30, WHITE)
    puzzle_button = Button(250, 200, 135, 60, "Puzzle", GAME_BACK, 30, WHITE)
    current_affairs_button = Button(400, 200, 135, 60, "Affairs", GAME_BACK, 30, WHITE)
    spelling_button = Button(550, 200, 135, 60, "Spelling", GAME_BACK, 30, WHITE)

    quantitative_button = Button(100, 280, 135, 60, "Quntitative", GAME_BACK, 30, WHITE)
    poem_button = Button(250, 280, 135, 60, "Poem", GAME_BACK, 30, WHITE)
    rational_button = Button(400, 280, 135, 60, "Rational", GAME_BACK, 30, WHITE)
    misc_button = Button(550, 280, 135, 60, "Msic", GAME_BACK, 30, WHITE)

    verbal_button = Button(100, 360, 135, 60, "Verbal", GAME_BACK, 30, WHITE)
    recitation_button = Button(250, 360, 135, 60, "Recite", GAME_BACK, 30, WHITE)
    personal_button = Button(400, 360, 135, 60, "Personal", GAME_BACK, 30, WHITE)
    nig_button = Button(550, 360, 135, 60, "Nigeria", GAME_BACK, 30, WHITE)
    
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # We are going to add more event handling here for user input in challenges
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for button in [hero_button,back_button, select_level_button,logic_quiz_button,puzzle_button,current_affairs_button,spelling_button,quantitative_button,poem_button,rational_button,misc_button,verbal_button,recitation_button,personal_button,nig_button]:  # Assuming buttons_list contains instances of your Button class
                    button.update_hover(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.is_clicked(mouse_pos):
                    game_state.change_state("menu")  # Change game state to "menu"
                    return  # Return from the gameplay function
                
                if logic_quiz_button.is_clicked(mouse_pos):
                    print("You have selected to do logic quiz")
                    questions("level: logic Quiz", QuizQuestions)
                
                elif puzzle_button.is_clicked(mouse_pos):
                    print("You have selected to do logic quiz")
                    questions("level: Puzzle Quiz", PuzzleQuestions)
                    
                elif quantitative_button.is_clicked(mouse_pos):
                    # Implement quantitative challenge
                    pass
                elif rational_button.is_clicked(mouse_pos):
                    # Implement rational challenge
                    pass
                elif current_affairs_button.is_clicked(mouse_pos):
                    print("You have selected to do current affairs quiz")
                    questions("level: Puzzle Quiz", CURRENTAFFAIRS)
                elif spelling_button.is_clicked(mouse_pos):
                    # Implement spelling challenge
                    pass
                # Add more elif conditions for other buttons


        screen.fill(SELECT_GAME)
        # We may draw challenges elements here
         # Draw challenge buttons
        select_level_button.draw(screen)
        hero_button.draw(screen)
        logic_quiz_button.draw(screen)
        puzzle_button.draw(screen)
        quantitative_button.draw(screen)
        rational_button.draw(screen)
        current_affairs_button.draw(screen)
        spelling_button.draw(screen)
        misc_button.draw(screen)
        poem_button.draw(screen)

        verbal_button.draw(screen)
        recitation_button.draw(screen) 
        personal_button.draw(screen) 
        nig_button.draw(screen)

        back_button.draw(screen)

        pygame.display.update()
   

def questions(title, quiz):
    pygame.display.set_caption(title)
    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(title)
    WHITE = (255, 255, 255)
    TITLE = title
    QUESTION_TEXT =  (25, 62, 54)
    QUESTION_BACHGROUND = (134, 180, 152)
    score = 0

    # Hangman images
    hangman_images = [
        pygame.image.load('assets\\hangman\\hangman0.png'),
        pygame.image.load('assets\\hangman\\hangman1.png'),
        pygame.image.load('assets\\hangman\\hangman2.png'),
        pygame.image.load('assets\\hangman\\hangman3.png'),
        pygame.image.load('assets\\hangman\\hangman4.png'),
        pygame.image.load('assets\\hangman\\hangman5.png'),
        pygame.image.load('assets\\hangman\\hangman6.png')
    ]

    line = pygame.image.load('assets\\lines\\line.png')
    colored_line = line.copy()
    colored_line.fill(QUESTION_TEXT)

    font = pygame.font.SysFont(FAMILY, 50)

    def draw_hangman(screen, hangman_stage):
        screen.blit(pygame.transform.scale(colored_line, (15, 400)), (300, 130))
        screen.blit(pygame.transform.scale(hangman_images[hangman_stage], (200, 300)), (20, 200))

    def wrap_text(text, width, font):
        """Wrap text to fit within a specified width."""
        lines = []
        words = text.split()
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            test_width, _ = font.size(test_line)
            if test_width <= width:
                current_line = test_line
            else:
                lines.append(current_line.rstrip())
                current_line = word + ' '
        lines.append(current_line.rstrip())
        return lines
    
    def display_question(screen, title):
        pygame.display.set_caption(title)
        global question_number  # Declare question_number as global

        back_button = Button(650, 530, 130, 50, "Quit", (150,180,140), 65, QUESTION_TEXT) 
        restart_button = Button(450, 530, 165, 50, "Restart", (150,180,140), 65, QUESTION_TEXT) 
        # Set the window title
        pygame.display.set_caption(title)
        
        screen.fill(QUESTION_BACHGROUND)
        back_button.draw(screen)
        restart_button.draw(screen)
        
        # Load random question, options, and answers
        question_number = random.randint(0, 94)  # Update question_number
        question = load_random_question()
        options = load_random_options()
        correct_answer = load_correct_answer()
        score = 0
        hangman_stage = 0

        draw_hangman(screen, hangman_stage)

        # Display question
        font = pygame.font.SysFont(FAMILY, 50)
        question_lines = wrap_text(question, 400, font)
        question_height = len(question_lines) * 30  # Height per line
        question_y = 150  # Adjusted position for question text
        for line in question_lines:
            question_text = font.render(line, True, QUESTION_TEXT)
            screen.blit(question_text, (360, question_y))
            question_y += 30

        # Display "Hangman" text
        font = pygame.font.SysFont(FAMILY, 70)
        hangman_text = font.render("HANGMAN", True, QUESTION_TEXT)
        screen.blit(hangman_text, (20, 80))
        font = pygame.font.SysFont(FAMILY, 50)
        # Display options
        option_y = 300
        for option in options:
            option_text = font.render(option, True, QUESTION_TEXT)
            screen.blit(option_text, (350, option_y))
            option_y += 50

        pygame.display.flip()

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in [restart_button,back_button]:  # Assuming buttons_list contains instances of your Button class
                        button.update_hover(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button.is_clicked(mouse_pos):
                        game_state.change_state("menu")  # Change game state to "menu"
                        return  # Return from the gameplay function
                    elif restart_button.is_clicked(mouse_pos):
                        print('Game restarted')
                        questions(title, quiz)
                        return
                    # Restart the game by resetting the game state and reloading a new question
                    # Check if any option is clicked
                    for i, option in enumerate(options):
                        option_rect = pygame.Rect(350, 300 + i*50, 600, 50)
                        if option_rect.collidepoint(mouse_pos):
                            print(correct_answer)
                            if option != correct_answer:
                                hangman_stage += 1
                                print("InCorrect!")
                            if hangman_stage == len(hangman_images) - 1:
                                # End game if hangman is fully built
                                print("You lost!")
                                return
                            # Load a new question
                            question_number = random.randint(0, 94)
                            question = load_random_question()
                            options = load_random_options()
                            correct_answer = load_correct_answer()
                            screen.fill(QUESTION_BACHGROUND)  # Clear the screen

                            back_button.draw(screen)
                            restart_button.draw(screen)
                            # Display new question  Wrap the question text
                            question_font = pygame.font.SysFont(FAMILY, 50)
                            question_lines = wrap_text(question, 400, question_font)
                            question_height = len(question_lines) * 30  # Height per line
                            question_y = 150  # Adjusted position for question text
                            for line in question_lines:
                                question_text = question_font.render(line, True, QUESTION_TEXT)
                                screen.blit(question_text, (360, question_y))
                                question_y += 30
                            
                            # Display new options
                            option_y = 300
                            for option in options:
                                option_text = font.render(option, True, QUESTION_TEXT)
                                screen.blit(option_text, (350, option_y))
                                option_y += 50

                            # Draw hangman
                            hangman_text = font.render("HANGMAN", True, QUESTION_TEXT)
                            screen.blit(hangman_text, (20, 80))
                            
                            draw_hangman(screen, hangman_stage)
                            pygame.display.flip()

    print(score)

    def load_random_question():
        question = quiz.get_question(question_number)
        print(question)
        return question

    def load_random_options():
        options =  quiz.get_options(question_number)
        print(options)
        return options

    def load_correct_answer():
        return quiz.get_correct_answer(question_number)

    # Call the function to display the question
    display_question(screen, TITLE)


def player_selection_screen():
    pygame.display.set_caption("Select Player")
    global input_active, input_text, player, name, registered_players, player_buttons


    screen.fill(WELCOME_SCREEN)
    font = pygame.font.SysFont(FAMILY, 60)
    text_surface = font.render("Select Player", True, WHITE)
    text_rect = text_surface.get_rect(midtop=(SCREEN_WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

    registered_players = (read_players_from_file("Player\\players.txt"))
    # Create buttons for registered players
    player_buttons = []
    for i, player_name in enumerate(set(registered_players)):
        button = Button(250, 150 + i * 50, 300, 40, player_name, WELCOME_SCREEN, 30, WHITE, WELCOME_SCREEN1)
        player_buttons.append(button)

    for button in player_buttons:
        button.draw(screen)

    # Input box for creating a new player
    pygame.draw.rect(screen, WHITE, input_box, 2)
    font = pygame.font.Font(None, 32)
    text_surface = font.render(input_text, True, WHITE)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.update()
    input_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in player_buttons:
                    if button.is_clicked(mouse_pos):
                        input_text = button.text
                        screen.fill(WELCOME_SCREEN)
                        for b in player_buttons:
                            b.draw(screen)
                        pygame.draw.rect(screen, WHITE, input_box, 2)
                        text_surface = font.render(input_text, True, WHITE)
                        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
                        pygame.display.update()
                        # Return the selected player's name
                        
                        name = Player(button.text).name
                        
                        return name
                if input_box.collidepoint(event.pos):
                    # Toggle input box active
                    input_active = not input_active
                else:
                    input_active = False
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        # Add the new player and clear the input box
                        registered_players.append(input_text)
                        
                        input_text = ""
                        # Move the input box down to make space for the new player button
                        input_box.y += 50
                        input_active = False
                        # Return the entered player's name
                        print(f"Just create a player {input_text}")
                        write_players_to_file(input_text)
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    # Update the screen to reflect the changes in input text
                    screen.fill(WELCOME_SCREEN)
                    for button in player_buttons:
                        button.draw(screen)
                    pygame.draw.rect(screen, WHITE, input_box, 2)
                    text_surface = font.render(input_text, True, WHITE)
                    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
                    pygame.display.update()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def write_players_to_file(player, filename ="Player\\players.txt"):
    with open(filename, "w") as file:
        for player in registered_players:
            file.write(player + "\n")

def main():
    global player, name
    while True:
        if game_state.state == "menu":
            print(game_state.state)
            mouse_pos = menu_screen()
            print(mouse_pos)  # Check if mouse position is returned
        elif game_state.state == "gameplay":
            print(game_state.state)
            # gameplay()
            
            
        # Player selection screen
        if game_state.state == "select_player":
            selected_player_name = player_selection_screen()
            print("We just finished executing the player_selection_screen function")
            if selected_player_name:
                player = Player(selected_player_name)
                name = player.name
                print(f"Hello {name} from me")
            else:
                name = "Unknown Player"
            game_state.change_state("gameplay")

if __name__ == "__main__":
    main()