import pygame
import random
from Challenges.logic_quiz import QuizQuestions

# Initialize Pygame
pygame.init()

def question():
    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Quiz Game")
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    quiz = QuizQuestions

    font = pygame.font.SysFont("arial", 50)

    def display_question(screen, title, load_question_func, load_options_func, load_answers_func):
        global question_number  # Declare question_number as global
        # Set the window title
        pygame.display.set_caption(title)

        # Fill the screen with black color to clear previous content
        screen.fill(BLACK)

        # Load random question, options, and answers
        question_number = random.randint(0, 94)  # Update question_number
        question = load_random_question()
        options = load_random_options()
        correct_answer = load_correct_answer()
        score = 0

        # Display question
        question_text = font.render(question, True, WHITE)
        screen.blit(question_text, (50, 80))

        # Display options
        option_y = 150
        for option in options:
            option_text = font.render(option, True, WHITE)
            screen.blit(option_text, (100, option_y))
            option_y += 50

        pygame.display.flip()

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if any option is clicked
                    for i, option in enumerate(options):
                        option_rect = pygame.Rect(100, 150 + i*50, 600, 50)
                        if option_rect.collidepoint(mouse_pos):
                            print(correct_answer)
                            if option == correct_answer:
                                score += 1
                                print("Correct!")
                                # Add your logic for correct answer here
                            else:
                                print("Incorrect!")
                            # Load a new question
                            question_number = random.randint(0, 94)
                            question = load_random_question()
                            options = load_random_options()
                            correct_answer = load_correct_answer()
                            screen.fill(BLACK)  # Clear the screen

                            # Display new question
                            question_text = font.render(question, True, WHITE)
                            screen.blit(question_text, (50, 80))
                            # Display new options
                            option_y = 150
                            for option in options:
                                option_text = font.render(option, True, WHITE)
                                screen.blit(option_text, (100, option_y))
                                option_y += 50
                            pygame.display.flip()

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
    display_question(screen, "Quiz Game", load_random_question, load_random_options, load_correct_answer)

print(question())