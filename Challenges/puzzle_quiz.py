class PuzzleQuestions:
    questions = []
    answers = []

    @staticmethod
    def add_question(question, options, correct_answer):
        PuzzleQuestions.questions.append(question)
        PuzzleQuestions.answers.append((options, correct_answer))

    def get_question(index):
        return PuzzleQuestions.questions[index]

    @staticmethod
    def get_options(index):
        return PuzzleQuestions.answers[index][0]

    @staticmethod
    def get_correct_answer(index):
        return PuzzleQuestions.answers[index][1]

quiz = PuzzleQuestions


quiz.add_question("What is 20% of 80?", ["A) 10", "B) 12", "C) 16", "D) 18"], "C) 16")
quiz.add_question("If a rectangle has a length of 8 units and a width of 4 units, what is its area?", ["A) 16 square units", "B) 24 square units", "C) 32 square units", "D) 36 square units"], "A) 32 square units")
quiz.add_question("What is the value of 3 to the power of 4?", ["A) 64", "B) 81", "C) 27", "D) 256"], "D) 81")
quiz.add_question("If a pizza is divided into 8 equal slices and you eat 3 slices, what fraction of the pizza have you eaten?", ["A) 1/3", "B) 3/8", "C) 3/5", "D) 5/8"], "B) 3/8")
quiz.add_question("What is the square root of 144?", ["A) 12", "B) 14", "C) 16", "D) 18"], "A) 12")
quiz.add_question("If x + 5 = 12, what is the value of x?", ["A) 5", "B) 6", "C) 7", "D) 8"], "B) 7")
quiz.add_question("If a triangle has a base of 6 units and a height of 4 units, what is its area?", ["A) 10 square units", "B) 12 square units", "C) 14 square units", "D) 16 square units"], "B) 12 square units")
quiz.add_question("What is the sum of the first 10 prime numbers?", ["A) 129", "B) 133", "C) 139", "D) 143"], "C) 139")
quiz.add_question("If 2x - 3 = 7, what is the value of x?", ["A) 5", "B) 6", "C) 7", "D) 8"], "D) 5")
quiz.add_question("If a box contains 24 candies and you take out 3, what fraction of the candies remain?", ["A) 1/6", "B) 1/4", "C) 1/5", "D) 1/8"], "C) 5/6")
quiz.add_question("What is the cube root of 27?", ["A) 3", "B) 4", "C) 5", "D) 6"], "A) 3")
quiz.add_question("If 3x + 4 = 16, what is the value of x?", ["A) 4", "B) 5", "C) 6", "D) 7"], "D) 4")
quiz.add_question("What is the perimeter of a square with sides of length 5 units?", ["A) 15 units", "B) 20 units", "C) 25 units", "D) 30 units"], "B) 20 units")
quiz.add_question("What is the value of 2 times the quantity 3 plus 5?", ["A) 10", "B) 12", "C) 14", "D) 16"], "B) 16")
quiz.add_question("If a car travels at a speed of 60 miles per hour, how far will it travel in 3 hours?", ["A) 120 miles", "B) 150 miles", "C) 180 miles", "D) 210 miles"], "C) 180 miles")
quiz.add_question("What is the area of a circle with a radius of 6 units?", ["A) 36π square units", "B) 72π square units", "C) 108π square units", "D) 144π square units"], "A) 36π square units")
quiz.add_question("What is the product of the first 5 even numbers?", ["A) 120", "B) 240", "C) 360", "D) 480"], "A) 120")
quiz.add_question("If 4x - 7 = 17, what is the value of x?", ["A) 6", "B) 7", "C) 8", "D) 9"], "D) 6")
quiz.add_question("What is the value of 12 divided by 3 times 2?", ["A) 4", "B) 6", "C) 8", "D) 10"], "B) 8")
quiz.add_question("If a rectangle has a perimeter of 30 units and a length of 8 units, what is its width?", ["A) 5 units", "B) 6 units", "C) 7 units", "D) 8 units"], "B) 7 units")
quiz.add_question("What is the sum of the angles in a triangle?", ["A) 90 degrees", "B) 180 degrees", "C) 270 degrees", "D) 360 degrees"], "B) 180 degrees")
quiz.add_question("If a box contains 36 pencils and you take out 12, what fraction of the pencils remain?", ["A) 1/3", "B) 1/2", "C) 2/3", "D) 3/4"], "C) 2/3")
quiz.add_question("What is the value of 5 factorial?", ["A) 120", "B) 240", "C) 360", "D) 720"], "D) 120")
quiz.add_question("If 3x + 5 = 20, what is the value of x?", ["A) 5", "B) 6", "C) 7", "D) 8"], "A) 5")
quiz.add_question("What is the volume of a cube with edges of length 4 units?", ["A) 16 cubic units", "B) 32 cubic units", "C) 64 cubic units", "D) 128 cubic units"], "B) 64 cubic units")
quiz.add_question("What is the value of 7 to the power of 2?", ["A) 49", "B) 50", "C) 51", "D) 52"], "A) 49")
quiz.add_question("If a circle has a radius of 8 units, what is its circumference?", ["A) 16π units", "B) 24π units", "C) 32π units", "D) 40π units"], "C) 16π units")
quiz.add_question("What is the value of 15 divided by 0.5?", ["A) 7.5", "B) 15", "C) 30", "D) 60"], "C) 30")
quiz.add_question("If a triangle has sides of lengths 3 units, 4 units, and 5 units, is it a right triangle?", ["A) Yes", "B) No"], "A) Yes")
quiz.add_question("What is the value of 4 times the quantity 2 plus 3?", ["A) 10", "B) 11", "C) 12", "D) 13"], "C) 11")
quiz.add_question("If 2x - 1 = 9, what is the value of x?", ["A) 4", "B) 5", "C) 6", "D) 7"], "D) 5")
quiz.add_question("What is the area of a rectangle with length 10 units and width 6 units?", ["A) 36 square units", "B) 48 square units", "C) 54 square units", "D) 60 square units"], "B) 60 square units")
quiz.add_question("What is the value of 2 to the power of 5?", ["A) 24", "B) 32", "C) 40", "D) 48"], "B) 32")
quiz.add_question("If a triangle has sides of lengths 4 units, 4 units, and 6 units, is it an equilateral triangle?", ["A) Yes", "B) No"], "B) No")
quiz.add_question("What is the value of (3\N{SUPERSCRIPT THREE} - 2\N{SUPERSCRIPT THREE})?", ["A) 7", "B) 9", "C) 17", "D) 19"], "B) 19")
quiz.add_question("If (5x + 8 = 23), what is the value of (x)?", ["A) 3", "B) 4", "C) 5", "D) 6"], "A) 3")
quiz.add_question("What is the surface area of a cube with edges of length 5 units?", ["A) 100 square units", "B) 125 square units", "C) 150 square units", "D) 175 square units"], "C) 150 square units")
quiz.add_question("What is the sum of the first 15 Fibonacci numbers?", ["A) 217", "B) 235", "C) 259", "D) 377"], "D) 377")
quiz.add_question("If a square has an area of 81 square units, what is the length of each side?", ["A) 7 units", "B) 8 units", "C) 9 units", "D) 10 units"], "C) 9 units")
quiz.add_question("What is the value of (sqrt(100) + sqrt(16))?", ["A) 12", "B) 14", "C) 18", "D) 20"], "A) 12")
quiz.add_question("If (3x + 4 = 16), what is the value of (x)?", ["A) 4", "B) 5", "C) 6", "D) 7"], "D) 4")
quiz.add_question("What is the volume of a rectangular prism with dimensions 7 units by 8 units by 9 units?", ["A) 504 cubic units", "B) 546 cubic units", "C) 588 cubic units", "D) 630 cubic units"], "C) 504 cubic units")
quiz.add_question("What is the sum of the first 20 even numbers?", ["A) 200", "B) 220", "C) 240", "D) 260"], "C) 240")
quiz.add_question("If (4x - 7 = 17), what is the value of (x)?", ["A) 6", "B) 7", "C) 8", "D) 9"], "D) 6")
quiz.add_question("What is the circumference of a circle with a radius of 10 units?", ["A) 20π units", "B) 25π units", "C) 30π units", "D) 35π units"], "C) 20π units")
quiz.add_question("What is the value of (8 times (6 - 3))?", ["A) 18", "B) 24", "C) 30", "D) 36"], "C) 24")
quiz.add_question("If a triangle has a perimeter of 30 units and sides of lengths 12 units, 10 units, and 8 units, is it an equilateral triangle?", ["A) Yes", "B) No"], "B) No")
quiz.add_question("What is the value of 2/5 times 3/4?", ["A) 3/10", "B) 3/8", "C) 3/5", "D) 3/2"], "B) 3/10")
quiz.add_question("If a square has a perimeter of 36 units, what is the length of each side?", ["A) 6 units", "B) 8 units", "C) 9 units", "D) 12 units"], "C) 9 units")
quiz.add_question("What is the sum of the first 25 multiples of 4?", ["A) 1250", "B) 1300", "C) 1350", "D) 1400"], "B) 1300")
quiz.add_question("If (2^x = 16), what is the value of (x)?", ["A) 2", "B) 3", "C) 4", "D) 5"], "C) 4")
quiz.add_question("What is the area of a triangle with base 10 units and height 8 units?", ["A) 40 square units", "B) 48 square units", "C) 56 square units", "D) 64 square units"], "B) 40 square units")
quiz.add_question("What is the value of 6\N{SUPERSCRIPT TWO} + 7\N{SUPERSCRIPT TWO} - 8\N{SUPERSCRIPT TWO})?", ["A) 7", "B) 36", "C) 49", "D) 64"], "B) 49")
quiz.add_question("If (3x - 2 = 13), what is the value of (x)?", ["A) 5", "B) 6", "C) 7", "D) 8"], "B) 5")
quiz.add_question("What is the surface area of a rectangular prism with dimensions 4 units by 5 units by 6 units?", ["A) 100 square units", "B) 120 square units", "C) 140 square units", "D) 160 square units"], "B) 148 square units")
quiz.add_question("What is the value of (5/6) / (2/3)?", ["A) (5/12", "B) (5/8", "C) (15/12", "D) (15/8"], "D) (5}{4")
quiz.add_question("If a rectangle has a length of 12 units and a width of 5 units, what is its perimeter?", ["A) 22 units", "B) 34 units", "C) 44 units", "D) 60 units"], "C) 34 units")
quiz.add_question("What is the sum of the first 30 prime numbers?", ["A) 462", "B) 590", "C) 682", "D) 792"], "B) 590")
quiz.add_question("If (2^ x = 64), what is the value of (x)?", ["A) 2", "B) 3", "C) 4", "D) 5"], "C) 3")
quiz.add_question("What is the area of a circle with diameter 10 units?", ["A) 25π square units", "B) 50π square units", "C) 75π square units", "D) 100π square units"], "A) 25π square units")
quiz.add_question("What is the value of (15 times (8 - 6))?", ["A) 15", "B) 20", "C) 25", "D) 30"], "D) 30")
quiz.add_question("If a triangle has sides of lengths 7 units, 10 units, and 13 units, is it a right triangle?", ["A) Yes", "B) No"], "A) Yes")
quiz.add_question("What is the value of 3/4 times 5/6?", ["A) 5/8", "B) 5/9", "C) 5/12", "D) 5/18"], "B) 5/8")
quiz.add_question("What is the value of (10 times (3 + 4))?", ["A) 20", "B) 30", "C) 40", "D) 50"], "D) 50")
quiz.add_question("If a rectangle has a perimeter of 50 units and a length of 18 units, what is its width?", ["A) 7 units", "B) 8 units", "C) 11 units", "D) 13 units"], "B) 8 units")
quiz.add_question("What is the value of 5/6 times 2/3?", ["A) 1/2", "B) 5/9", "C) 5/6", "D) 5/18"], "B) 5/9")
quiz.add_question("If a square has an area of 144 square units, what is the length of each side?", ["A) 8 units", "B) 10 units", "C) 12 units", "D) 16 units"], "C) 12 units")
quiz.add_question("What is the sum of the first 20 Fibonacci numbers?", ["A) 17710", "B) 28657", "C) 46368", "D) 75025"], "C) 46368")
quiz.add_question("What is the value of (3x - 5 = 16), what is the value of (x)?", ["A) 7", "B) 8", "C) 9", "D) 10"], "D) 10")
quiz.add_question("What is the area of a rectangle with length 12 units and width 7 units?", ["A) 72 square units", "B) 84 square units", "C) 96 square units", "D) 108 square units"], "B) 84 square units")
quiz.add_question("What is the value of (6^2 - 3^2)?", ["A) 27", "B) 33", "C) 36", "D) 39"], "A) 27")
quiz.add_question("If (2x + 7 = 15), what is the value of (x)?", ["A) 4", "B) 5", "C) 6", "D) 7"], "B) 5")
quiz.add_question("What is the volume of a cylinder with a radius of 4 units and a height of 10 units?", ["A) (40pi) cubic units", "B) (80pi) cubic units", "C) (160pi) cubic units", "D) (320pi) cubic units"], "B) (80pi) cubic units")
quiz.add_question("What is the sum of the first 10 prime numbers?", ["A) 129", "B) 142", "C) 150", "D) 160"], "A) 129")
quiz.add_question("If a triangle has sides of lengths 5 units, 12 units, and 13 units, is it a right triangle?", ["A) Yes", "B) No"], "A) Yes")
quiz.add_question("What is the value of 1/3 - 1/6})?", ["A) (1/3})", "B) (1/6})", "C) (1/12})", "D) (1/18})"], "C) (1/12")
quiz.add_question("If (4x + 9 = 25), what is the value of (x)?", ["A) 4", "B) 5", "C) 6", "D) 7"], "A) 4")
quiz.add_question("What is the perimeter of a square with sides of length 15 units?", ["A) 45 units", "B) 60 units", "C) 75 units", "D) 90 units"], "C) 75 units")
quiz.add_question("What is the value of (10 times (3 + 4))?", ["A) 20", "B) 30", "C) 40", "D) 50"], "D) 50")
quiz.add_question("If a rectangle has a perimeter of 50 units and a length of 18 units, what is its width?", ["A) 7 units", "B) 8 units", "C) 11 units", "D) 13 units"], "B) 8 units")
quiz.add_question("What is the value of 5/6 times 2/3?", ["A) 1/2", "B) 5/9", "C) 5/6", "D) 5/18"], "B) 5/9")
quiz.add_question("If a square has an area of 144 square units, what is the length of each side?", ["A) 8 units", "B) 10 units", "C) 12 units", "D) 16 units"], "C) 12 units")
quiz.add_question("What is the sum of the first 20 Fibonacci numbers?", ["A) 17710", "B) 28657", "C) 46368", "D) 75025"], "C) 46368")
quiz.add_question("What is the value of (3x - 5 = 16), what is the value of (x)?", ["A) 7", "B) 8", "C) 9", "D) 10"], "D) 10")
quiz.add_question("What is the area of a rectangle with length 12 units and width 7 units?", ["A) 72 square units", "B) 84 square units", "C) 96 square units", "D) 108 square units"], "B) 84 square units")
quiz.add_question("What is the value of (6^2 - 3^2)?", ["A) 27", "B) 33", "C) 36", "D) 39"], "A) 27")
quiz.add_question("If (2x + 7 = 15), what is the value of (x)?", ["A) 4", "B) 5", "C) 6", "D) 7"], "B) 5")
quiz.add_question("What is the volume of a cylinder with a radius of 4 units and a height of 10 units?", ["A) (40pi) cubic units", "B) (80pi) cubic units", "C) (160pi) cubic units", "D) (320pi) cubic units"], "B) (80pi) cubic units")
quiz.add_question("What is the sum of the first 10 prime numbers?", ["A) 129", "B) 142", "C) 150", "D) 160"], "A) 129")
quiz.add_question("If a triangle has sides of lengths 5 units, 12 units, and 13 units, is it a right triangle?", ["A) Yes", "B) No"], "A) Yes")
quiz.add_question("What is the value of 1/3 - 1/6 ?", ["A) 1/3", "B) 1/6", "C) 1/12", "D) 1/18"], "C) 1/12")
quiz.add_question("If (4x + 9 = 25), what is the value of (x)?", ["A) 4", "B) 5", "C) 6", "D) 7"], "A) 4")
quiz.add_question("What is the perimeter of a square with sides of length 15 units?", ["A) 45 units", "B) 60 units", "C) 75 units", "D) 90 units"], "C) 75 units")
quiz.add_question("What is the value of (10 times (3 + 4))?", ["A) 20", "B) 30", "C) 40", "D) 50"], "D) 50")
quiz.add_question("If a rectangle has a perimeter of 50 units and a length of 18 units, what is its width?", ["A) 7 units", "B) 8 units", "C) 11 units", "D) 13 units"], "B) 8 units")
quiz.add_question("What is the value of 5/6 times 2/3?", ["A) 1/2", "B) 5/9", "C) 5/6", "D) 5/18"], "B) 5/9")
quiz.add_question("If a square has an area of 144 square units, what is the length of each side?", ["A) 8 units", "B) 10 units", "C) 12 units", "D) 16 units"], "C) 12 units")
quiz.add_question("What is the sum of the first 20 Fibonacci numbers?", ["A) 17710", "B) 28657", "C) 46368", "D) 75025"], "C) 46368")
