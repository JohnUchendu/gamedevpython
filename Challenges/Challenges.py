from abc import ABC, abstractmethod

class Challenge:
    def __init__(self):
        # self.challenge_type = challenge_type
        # self.difficulty = difficulty
        # self.completed = False

        self.questions = []
        self.answers = []
    @abstractmethod
    def add_question(self, question, options, correct_answer):
        pass
    @abstractmethod
    def get_question(self, index):
        pass

    @abstractmethod
    def get_options(self, index):
        pass
    @abstractmethod
    def get_correct_answer(self, index):
        pass
    
    def generate_challenge(self):
        # This is where we will generate challenges based on challenge type and difficulty level
        pass

    def evaluate_answer(self, answer):
        # Here we will evaluate player's answer and update score,points or currency and or Power Up.
        pass

# Define challenges
# challenges = [
#     Challenge("Quiz", 1),
#     Challenge("Spelling", 2),
#     Challenge("Logic Puzzle", 3)
# ]