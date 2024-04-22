from Challenges.Challenges import Challenge
# from Challenges.Challenges import Challenge
import random

class QuizQuestions(Challenge):
    questions = []
    answers = []
    def __init__(self):
        # self.questions = []
        # self.answers = []
        pass

    def add_question(question, options, correct_answer):
        QuizQuestions.questions.append(question)
        QuizQuestions.answers.append((options, correct_answer))

    def get_question(index):
        return QuizQuestions.questions[index]

    def get_options(index):
        return QuizQuestions.answers[index][0]

    def get_correct_answer(index):
        return QuizQuestions.answers[index][1]

quiz = QuizQuestions

quiz.add_question("What comes next in the sequence: 2, 4, 6, 8, ...?", ["A) 10", "B) 12", "C) 14", "D) 16"], "A) 10")
quiz.add_question("Which shape does not belong in the group?", ["A) Circle", "B) Triangle", "C) Square", "D) Oval"], "D) Oval")
quiz.add_question("If a cat has four legs and a bird has two legs, how many legs do two cats and three birds have altogether?", ["A) 10", "B) 12", "C) 14", "D) 16"], "B) 12")
quiz.add_question("What comes next in the pattern: apple, banana, orange, ...?", ["A) Pear", "B) Grapes", "C) Mango", "D) Pineapple"], "A) Pear")
quiz.add_question("Which number is the odd one out: 12, 18, 24, 30, 36?", ["A) 12", "B) 18", "C) 24", "D) 30"], "D) 30")
quiz.add_question("If all the windows in a house are closed, what's the first thing you should open to let fresh air in?", ["A) Door", "B) Curtains", "C) Chimney", "D) Roof"], "A) Door")
quiz.add_question("Which animal is not like the others: Dog, Cat, Rabbit, Elephant?", ["A) Dog", "B) Cat", "C) Rabbit", "D) Elephant"], "D) Elephant")
quiz.add_question("If today is Monday, what will be the day after tomorrow?", ["A) Tuesday", "B) Wednesday", "C) Thursday", "D) Friday"], "C) Thursday")
quiz.add_question("How many sides does a square have?", ["A) 2", "B) 3", "C) 4", "D) 5"], "C) 4")
quiz.add_question("Which shape has three sides?", ["A) Circle", "B) Square", "C) Triangle", "D) Rectangle"], "C) Triangle")
quiz.add_question("If you have 5 apples and you give 2 to your friend, how many apples do you have left?", ["A) 2", "B) 3", "C) 4", "D) 5"], "B) 3")
quiz.add_question("What is the opposite of 'big'?", ["A) Small", "B) Large", "C) Huge", "D) Tall"], "A) Small")
quiz.add_question("Which of these is not a primary color?", ["A) Red", "B) Yellow", "C) Green", "D) Blue"], "C) Green")
quiz.add_question("What color do you get when you mix blue and yellow?", ["A) Red", "B) Green", "C) Purple", "D) Orange"], "B) Green")
quiz.add_question("Which animal is cold-blooded?", ["A) Dog", "B) Snake", "C) Cat", "D) Rabbit"], "B) Snake")
quiz.add_question("What is the result of adding 5 and 3?", ["A) 7", "B) 8", "C) 9", "D) 10"], "B) 8")
quiz.add_question("Which of these shapes has the most sides?", ["A) Triangle", "B) Square", "C) Pentagon", "D) Hexagon"], "D) Hexagon")
quiz.add_question("If today is January 1st, what will be the date after 5 days?", ["A) January 6th", "B) January 5th", "C) January 7th", "D) January 8th"], "B) January 5th")
quiz.add_question("Which of these is a season?", ["A) Day", "B) Month", "C) Winter", "D) Hour"], "C) Winter")
quiz.add_question("Which planet is closest to the Sun?", ["A) Mars", "B) Venus", "C) Earth", "D) Jupiter"], "B) Venus")
quiz.add_question("What shape is a traffic sign that indicates 'Stop'?", ["A) Circle", "B) Square", "C) Triangle", "D) Rectangle"], "A) Circle")
quiz.add_question("What do you use to measure time?", ["A) Thermometer", "B) Ruler", "C) Clock", "D) Scale"], "C) Clock")
quiz.add_question("What do you call a baby cat?", ["A) Puppy", "B) Kitten", "C) Cub", "D) Calf"], "B) Kitten")
quiz.add_question("How many days are there in a week?", ["A) 5", "B) 6", "C) 7", "D) 8"], "C) 7")
quiz.add_question("What is the capital of France?", ["A) London", "B) Berlin", "C) Paris", "D) Rome"], "C) Paris")
quiz.add_question("Which of these is not a fruit?", ["A) Apple", "B) Carrot", "C) Banana", "D) Grape"], "B) Carrot")
quiz.add_question("What is the opposite of 'day'?", ["A) Sun", "B) Night", "C) Moon", "D) Morning"], "B) Night")
quiz.add_question("How many legs does a spider have?", ["A) 4", "B) 6", "C) 8", "D) 10"], "C) 8")
quiz.add_question("What color is the sky during the day?", ["A) Green", "B) Blue", "C) Yellow", "D) Red"], "B) Blue")
quiz.add_question("Which animal can fly?", ["A) Dog", "B) Cat", "C) Bird", "D) Elephant"], "C) Bird")
quiz.add_question("If you have 3 apples and you eat 2, how many apples do you have left?", ["A) 0", "B) 1", "C) 2", "D) 3"], "B) 1")
quiz.add_question("What is the opposite of 'happy'?", ["A) Sad", "B) Angry", "C) Excited", "D) Joyful"], "A) Sad")
quiz.add_question("Which of these is not a mode of transportation?", ["A) Car", "B) Bicycle", "C) Boat", "D) Television"], "D) Television")
quiz.add_question("What is the sum of 2 and 3?", ["A) 4", "B) 5", "C) 6", "D) 7"], "B) 5")
quiz.add_question("How many continents are there in the world?", ["A) 5","B) 6", "C) 7", "D) 8"], "C) 7")
quiz.add_question("Which of these is not a shape?", ["A) Circle", "B) Square", "C) Line", "D) Oval"], "C) Line")
quiz.add_question("What do you use to write with?", ["A) Pencil", "B) Eraser", "C) Ruler", "D) Sharpener"], "A) Pencil")
quiz.add_question("What do you call a young cow?", ["A) Calf", "B) Foal", "C) Piglet", "D) Lamb"], "A) Calf")
quiz.add_question("Which animal lives in water?", ["A) Lion", "B) Tiger", "C) Fish", "D) Bear"], "C) Fish")
quiz.add_question("What is the capital of the United States?", ["A) Washington D.C.", "B) New York City", "C) Los Angeles", "D) Chicago"], "A) Washington D.C.")
quiz.add_question("What is the opposite of 'slow'?", ["A) Fast", "B) Quick", "C) Rapid", "D) Speedy"], "A) Fast")
quiz.add_question("Which of these is not a primary shape?", ["A) Circle", "B) Triangle", "C) Square", "D) Rectangle"], "D) Rectangle")
quiz.add_question("What comes after spring?", ["A) Winter", "B) Summer", "C) Fall", "D) Autumn"], "B) Summer")
quiz.add_question("How many legs does a spider have?", ["A) 4", "B) 6", "C) 8", "D) 10"], "C) 8")
quiz.add_question("What is the opposite of 'light'?", ["A) Heavy", "B) Dark", "C) Bright", "D) Shiny"], "A) Heavy")
quiz.add_question("Which of these is not a color?", ["A) Red", "B) Green", "C) Tall", "D) Blue"], "C) Tall")
quiz.add_question("What shape is a pizza?", ["A) Circle", "B) Square", "C) Triangle", "D) Oval"], "A) Circle")
quiz.add_question("What do you use to measure temperature?", ["A) Clock", "B) Scale", "C) Thermometer", "D) Ruler"], "C) Thermometer")
quiz.add_question("Which animal has a trunk?", ["A) Lion", "B) Tiger", "C) Elephant", "D) Giraffe"], "C) Elephant")
quiz.add_question("What is the largest planet in our solar system?", ["A) Mars", "B) Venus", "C) Earth", "D) Jupiter"], "D) Jupiter")
quiz.add_question("What is the opposite of 'wet'?", ["A) Dry", "B) Moist", "C) Damp", "D) Soaked"], "A) Dry")
quiz.add_question("Which of these is not a shape?", ["A) Circle", "B) Triangle", "C) Oval", "D) Square"], "C) Oval")
quiz.add_question("What comes after Monday?", ["A) Tuesday", "B) Wednesday", "C) Thursday", "D) Friday"], "A) Tuesday")
quiz.add_question("How many eyes does a human have?", ["A) 1", "B) 2", "C) 3", "D) 4"], "B) 2")
quiz.add_question("What is the opposite of 'fast'?", ["A) Slow", "B) Quick", "C) Rapid", "D) Speedy"], "A) Slow")
quiz.add_question("Which of these is not a planet?", ["A) Mars", "B) Jupiter", "C) Moon", "D) Neptune"], "C) Moon")
quiz.add_question("What shape is a clock?", ["A) Circle", "B) Square", "C) Triangle", "D) Rectangle"], "A) Circle")
quiz.add_question("What do you use to brush your teeth?", ["A) Comb", "B) Toothbrush", "C) Hairbrush", "D) Paintbrush"], "B) Toothbrush")
quiz.add_question("Which animal is known for its stripes?", ["A) Lion", "B) Tiger", "C) Elephant", "D) Giraffe"], "B) Tiger")
quiz.add_question("What is the capital of England?", ["A) London", "B) Paris", "C) Berlin", "D) Rome"], "A) London")
quiz.add_question("What is the opposite of 'short'?", ["A) Tall", "B) Small", "C) Little", "D) Low"], "A) Tall")
quiz.add_question("Which of these is not a mode of transport?", ["A) Car", "B) Bicycle", "C) Ship", "D) Plane"], "C) Ship")
quiz.add_question("What color is a ripe banana?", ["A) Red", "B) Yellow", "C) Green", "D) Orange"], "B) Yellow")
quiz.add_question("How many legs does a cat have?", ["A) 2", "B) 4", "C) 6", "D) 8"], "B) 4")
quiz.add_question("What is the opposite of 'fast'?", ["A) Slow", "B) Quick", "C) Rapid", "D) Speedy"], "A) Slow")
quiz.add_question("Which of these is not a planet?", ["A) Mars", "B) Jupiter", "C) Moon", "D) Neptune"], "C) Moon")
quiz.add_question("What shape is a pizza?", ["A) Circle", "B) Square", "C) Triangle", "D) Oval"], "A) Circle")
quiz.add_question("What do you use to brush your teeth?", ["A) Comb", "B) Toothbrush", "C) Hairbrush", "D) Paintbrush"], "B) Toothbrush")
quiz.add_question("Which animal is known for its stripes?", ["A) Lion", "B) Tiger", "C) Elephant", "D) Giraffe"], "B) Tiger")
quiz.add_question("What is the capital of England?", ["A) London", "B) Paris", "C) Berlin", "D) Rome"], "A) London")
quiz.add_question("What is the opposite of 'short'?", ["A) Tall", "B) Small", "C) Little", "D) Low"], "A) Tall")
quiz.add_question("Which of these is not a mode of transport?", ["A) Car", "B) Bicycle", "C) Ship", "D) Plane"], "C) Ship")
quiz.add_question("What color is a ripe banana?", ["A) Red", "B) Yellow", "C) Green", "D) Orange"], "B) Yellow")
quiz.add_question("What do you use to cut paper?", ["A) Scissors", "B) Knife", "C) Fork", "D) Spoon"], "A) Scissors")
quiz.add_question("Which animal lives in a hive?", ["A) Bee", "B) Ant", "C) Spider", "D) Butterfly"], "A) Bee")
quiz.add_question("What is the opposite of 'high'?", ["A) Low", "B) Tall", "C) Small", "D) Short"], "A) Low")
quiz.add_question("Which of these is not a fruit?", ["A) Apple", "B) Banana", "C) Carrot", "D) Orange"], "C) Carrot")
quiz.add_question("What shape is a stop sign?", ["A) Circle", "B) Square", "C) Octagon", "D) Triangle"], "C) Octagon")
quiz.add_question("What comes after December?", ["A) November", "B) January", "C) February", "D) March"], "B) January")
quiz.add_question("How many legs does a cat have?", ["A) 2", "B) 4", "C) 6", "D) 8"], "B) 4")
quiz.add_question("What is the opposite of 'fast'?", ["A) Slow", "B) Quick", "C) Rapid", "D) Speedy"], "A) Slow")
quiz.add_question("Which of these is not a planet?", ["A) Mars", "B) Jupiter", "C) Moon", "D) Neptune"], "C) Moon")
quiz.add_question("What shape is a pizza?", ["A) Circle", "B) Square", "C) Triangle", "D) Oval"], "A) Circle")
quiz.add_question("What do you use to brush your teeth?", ["A) Comb", "B) Toothbrush", "C) Hairbrush", "D) Paintbrush"], "B) Toothbrush")
quiz.add_question("Which animal is known for its stripes?", ["A) Lion", "B) Tiger", "C) Elephant", "D) Giraffe"], "B) Tiger")
quiz.add_question("What is the capital of England?", ["A) London", "B) Paris", "C) Berlin", "D) Rome"], "A) London")
quiz.add_question("What is the opposite of 'short'?", ["A) Tall", "B) Small", "C) Little", "D) Low"], "A) Tall")
quiz.add_question("Which of these is not a mode of transport?", ["A) Car", "B) Bicycle", "C) Ship", "D) Plane"], "C) Ship")
quiz.add_question("What color is a ripe banana?", ["A) Red", "B) Yellow", "C) Green", "D) Orange"], "B) Yellow")
quiz.add_question("What do you use to cut paper?", ["A) Scissors", "B) Knife", "C) Fork", "D) Spoon"], "A) Scissors")
quiz.add_question("Which animal lives in a hive?", ["A) Bee", "B) Ant", "C) Spider", "D) Butterfly"], "A) Bee")
quiz.add_question("What is the opposite of 'high'?", ["A) Low", "B) Tall", "C) Small", "D) Short"], "A) Low")
quiz.add_question("Which of these is not a fruit?", ["A) Apple", "B) Banana", "C) Carrot", "D) Orange"], "C) Carrot")
quiz.add_question("What shape is a stop sign?", ["A) Circle", "B) Square", "C) Octagon", "D) Triangle"], "C) Octagon")
quiz.add_question("What comes after December?", ["A) November", "B) January", "C) February", "D) March"], "B) January")



# question_number = random.randint(0,95)
# print(f"Question number: {question_number}")
# print("Question 1:", quiz.get_question(question_number))
# Accessing the options for the first question
# print("Options:", quiz.get_options(question_number))
# Accessing the correct answer for the first question
# print("Correct Answer:", quiz.get_correct_answer(question_number))
# print(f"There are {len(quiz1.questions)} questions available")
# print(f"There are also {len(quiz1.answers)} correct answers available")

# if "__name __" == "__main__":
#     quiz = QuizQuestions()