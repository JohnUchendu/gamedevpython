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
        # self.questions.append(question)
        # self.answers.append((options, correct_answer))
        pass
    @abstractmethod
    def get_question(self, index):
        pass
        # return self.questions[index]

    @abstractmethod
    def get_options(self, index):
        pass
        # return self.answers[index][0]
    @abstractmethod
    def get_correct_answer(self, index):
        # return self.answers[index][1]
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