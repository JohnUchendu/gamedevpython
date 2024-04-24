from Challenges.Challenges import Challenge
# from Challenges.Challenges import Challenge
import random


class CURRENTAFFAIRS(Challenge):
    questions = []
    answers = []
    def _init_(self):
        # self.questions = []
        # self.answers = []
        pass


    def add_question(question, options, correct_answer):
        CURRENTAFFAIRS.questions.append(question)
        CURRENTAFFAIRS.answers.append((options, correct_answer))


    def get_question(index):
        return CURRENTAFFAIRS.questions[index]


    def get_options(index):
        return CURRENTAFFAIRS.answers[index][0]


    def get_correct_answer(index):
        return CURRENTAFFAIRS.answers[index][1]


quiz = CURRENTAFFAIRS
quiz.add_question("Which country recently hosted the G20 summit, where leaders discussed global economic issues and cooperation?", ["A) Japan", "B) Saudi Arabia", "C) France", "D) Brazil"], "B) Saudi Arabia")
quiz.add_question("What is the name of the new COVID-19 variant that emerged in late 2021, causing concerns among health officials worldwide?", ["A) Delta", "B) Omicron", "C) Gamma", "D) Epsilon"], "B) Omicron")
quiz.add_question("Which country recently became the first in the world to approve a COVID-19 vaccine for children aged 5 to 11 years?", ["A) United States", "B) United Kingdom", "C) China", "D) Germany"], "A) United States")
quiz.add_question("What major sporting event took place in Beijing, China, attracting athletes from around the world despite controversy over human rights issues?", ["A) FIFA World Cup", "B) UEFA European Championship", "C) Winter Olympics", "D) Commonwealth Games"], "C) Winter Olympics")
quiz.add_question("Which country recently experienced widespread protests and unrest following disputed presidential elections, resulting in a government crackdown on dissent?", ["A) Belarus", "B) Venezuela", "C) Ethiopia", "D) Myanmar"], "A) Belarus")
quiz.add_question("What landmark agreement was reached between the United States, United Kingdom, and Australia, known as AUKUS, aimed at strengthening defense and security cooperation in the Indo-Pacific region?", ["A) Paris Agreement", "B) NATO Treaty", "C) AUKUS Pact", "D) Shanghai Cooperation Organization"], "C) AUKUS Pact")
quiz.add_question("Who won the Nobel Prize in Literature in 2022 for their extraordinary storytelling and narrative craftsmanship?", ["A) Kazuo Ishiguro", "B) Louise Glück", "C) Olga Tokarczuk", "D) Abdulrazak Gurnah"], "A) Kazuo Ishiguro")
quiz.add_question("Which tech company recently faced scrutiny over its handling of user data and privacy concerns, leading to calls for increased regulation?", ["A) Facebook", "B) Google", "C) Apple", "D) Amazon"], "A) Facebook")
quiz.add_question("Which country recently launched a mission to explore the far side of the Moon, marking a significant milestone in its space program?", ["A) Russia", "B) India", "C) China", "D) United States"], "C) China")
quiz.add_question("What historic event took place in Glasgow, Scotland, in 2021, bringing together world leaders to discuss urgent action on climate change?", ["A) Earth Summit", "B) Paris Agreement", "C) Kyoto Protocol", "D) COP26"], "D) COP26")
quiz.add_question("Which global organization recently issued a report warning of the urgent need for drastic reductions in greenhouse gas emissions to avoid catastrophic climate change?", ["A) World Health Organization", "B) International Monetary Fund", "C) United Nations", "D) World Meteorological Organization"], "C) United Nations")
quiz.add_question("Who won the 2022 FIFA Men's World Cup, held in Qatar, after defeating Argentina in the final?", ["A) Germany", "B) Brazil", "C) France", "D) Italy"], "D) Italy")
quiz.add_question("Which country recently experienced a surge in COVID-19 cases due to the spread of the Omicron variant, leading to new lockdown measures and travel restrictions?", ["A) South Africa", "B) Australia", "C) Canada", "D) South Korea"], "A) South Africa")
quiz.add_question("What major infrastructure project, connecting Europe and Asia, was officially opened in 2021, providing a new route for trade and transportation?", ["A) Trans-Siberian Railway", "B) Suez Canal Expansion", "C) Silk Road", "D) Nord Stream Pipeline"], "C) Silk Road")
quiz.add_question("Which country recently announced plans to phase out coal-fired power plants and transition to renewable energy sources by 2030?", ["A) Germany", "B) United States", "C) Japan", "D) China"], "A) Germany")
quiz.add_question("What was the theme of the recent United Nations Climate Change Conference (COP26)?", ["A) Renewable Energy Solutions", "B) Climate Justice", "C) Sustainable Agriculture", "D) Fossil Fuel Expansion"], "D) Fossil Fuel Expansion")
quiz.add_question("Which country recently launched its first-ever digital currency, becoming the first major economy to do so?", ["A) China", "B) United States", "C) Russia", "D) India"], "C) Russia")
quiz.add_question("Who won the Nobel Peace Prize in 2023 for their efforts in promoting peace and reconciliation in a conflict zone?", ["A) Greta Thunberg", "B) Malala Yousafzai", "C) Abiy Ahmed", "D) Angela Merkel"], "C) Abiy Ahmed")
quiz.add_question("Which country recently faced controversy over its new social media regulations, criticized for limiting free speech?", ["A) United States", "B) Russia", "C) Australia", "D) Brazil"], "A) United States")
quiz.add_question("Which tech company announced plans to build its first electric car manufacturing plant in the United States?", ["A) Tesla", "B) Google", "C) Apple", "D) Amazon"], "C) Apple")
quiz.add_question("Which African nation recently experienced a military coup, leading to widespread protests and international condemnation?", ["A) Ethiopia", "B) Nigeria", "C) Sudan", "D) Burkina Faso"], "D) Burkina Faso")
quiz.add_question("What landmark climate agreement was signed by over 100 countries at the recent Earth Summit?", ["A) Paris Agreement", "B) Kyoto Protocol", "C) Montreal Protocol", "D) Copenhagen Accord"], "A) Paris Agreement")
quiz.add_question("Which country recently made headlines for successfully landing a rover on Mars, becoming the third nation to do so?", ["A) China", "B) India", "C) United Arab Emirates", "D) Japan"], "D) Japan")
quiz.add_question("Who won the 2023 Pulitzer Prize for Journalism for their investigative reporting on government corruption?", ["A) Glenn Greenwald", "B) Bob Woodward", "C) Ida B. Wells", "D) Ronan Farrow"], "C) Ida B. Wells")
quiz.add_question("Which city was chosen as the host for the 2032 Summer Olympics, sparking both excitement and controversy?", ["A) Tokyo", "B) Brisbane", "C) Paris", "D) Los Angeles"], "B) Brisbane")
quiz.add_question("Who is the current President of the United States?", ["A) Joe Biden", "B) Donald Trump", "C) Barack Obama", "D) Hillary Clinton"], "A) Joe Biden")
quiz.add_question("Which country recently experienced a volcanic eruption, causing widespread destruction and displacement of residents?", ["A) Japan", "B) Italy", "C) Indonesia", "D) Greece"], "C) Indonesia")
quiz.add_question("What is the capital city of Australia?", ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"], "C) Canberra")
quiz.add_question("Who won the FIFA Men's World Cup in 2018?", ["A) France", "B) Brazil", "C) Germany", "D) Argentina"], "A) France")
quiz.add_question("Which technology company is known for its iPhone, iPad, and MacBook products?", ["A) Microsoft", "B) Samsung", "C) Apple", "D) Google"], "C) Apple")
quiz.add_question("What is the currency of Japan?", ["A) Yen", "B) Euro", "C) Dollar", "D) Yuan"], "A) Yen")
quiz.add_question("Who is the author of the Harry Potter book series?", ["A) J.K. Rowling", "B) Stephen King", "C) George R.R. Martin", "D) Dan Brown"], "A) J.K. Rowling")
quiz.add_question("Which planet is known as the Red Planet?", ["A) Jupiter", "B) Mars", "C) Venus", "D) Saturn"], "B) Mars")
quiz.add_question("Who was the first person to step on the Moon?", ["A) Neil Armstrong", "B) Buzz Aldrin", "C) Yuri Gagarin", "D) Alan Shepard"], "A) Neil Armstrong")
quiz.add_question("Which river is the longest in the world?", ["A) Nile", "B) Amazon", "C) Mississippi", "D) Yangtze"], "A) Nile")
quiz.add_question("Who painted the Mona Lisa?", ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"], "C) Leonardo da Vinci")
quiz.add_question("Which element has the chemical symbol 'H'?", ["A) Hydrogen", "B) Helium", "C) Carbon", "D) Oxygen"], "A) Hydrogen")
quiz.add_question("What is the chemical formula for water?", ["A) H2O2", "B) CO2", "C) H2O", "D) CH4"], "C) H2O")
quiz.add_question("Who wrote the play 'Romeo and Juliet'?", ["A) William Shakespeare", "B) George Bernard Shaw", "C) Oscar Wilde", "D) Tennessee Williams"], "A) William Shakespeare")
quiz.add_question("What is the tallest mountain in the world?", ["A) K2", "B) Mount Everest", "C) Kilimanjaro", "D) Mount McKinley"], "B) Mount Everest")
quiz.add_question("Who is the CEO of Facebook?", ["A) Tim Cook", "B) Elon Musk", "C) Mark Zuckerberg", "D) Jeff Bezos"], "C) Mark Zuckerberg")
quiz.add_question("Which country is famous for its tulips and windmills?", ["A) France", "B) Italy", "C) Netherlands", "D) Germany"], "C) Netherlands")
quiz.add_question("What is the chemical symbol for gold?", ["A) Ag", "B) Au", "C) Fe", "D) Pb"], "B) Au")
quiz.add_question("Who discovered penicillin?", ["A) Alexander Fleming", "B) Louis Pasteur", "C) Jonas Salk", "D) Marie Curie"], "A) Alexander Fleming")
quiz.add_question("What is the primary function of the mitochondria?", ["A) Protein synthesis", "B) Energy production", "C) Cellular respiration", "D) DNA replication"], "B) Energy production")
quiz.add_question("Which planet is known as the 'Morning Star' and the 'Evening Star'?", ["A) Mercury", "B) Venus", "C) Mars", "D) Jupiter"], "B) Venus")
quiz.add_question("Who painted 'Starry Night'?", ["A) Claude Monet", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Salvador Dalí"], "B) Vincent van Gogh")
quiz.add_question("What is the chemical symbol for sodium?", ["A) Na", "B) S", "C) Sn", "D) Fe"], "A) Na")
quiz.add_question("Which mammal can fly?", ["A) Bat", "B) Rat", "C) Mouse", "D) Dog"], "A) Bat")
quiz.add_question("What is the largest organ in the human body?", ["A) Liver", "B) Brain", "C) Skin", "D) Heart"], "C) Skin")
quiz.add_question("Who was the first woman to win a Nobel Prize?", ["A) Marie Curie", "B) Mother Teresa", "C) Ada Lovelace", "D) Amelia Earhart"], "A) Marie Curie")
quiz.add_question("What is the capital city of Brazil?", ["A) Buenos Aires", "B) Rio de Janeiro", "C) Brasília", "D) São Paulo"], "C) Brasília")
quiz.add_question("Which famous scientist developed the theory of relativity?", ["A) Isaac Newton", "B) Albert Einstein", "C) Stephen Hawking", "D) Nikola Tesla"], "B) Albert Einstein")
quiz.add_question("What is the chemical symbol for iron?", ["A) Ir", "B) Fe", "C) I", "D) In"], "B) Fe")
quiz.add_question("Who wrote 'To Kill a Mockingbird'?", ["A) Harper Lee", "B) F. Scott Fitzgerald", "C) Ernest Hemingway", "D) John Steinbeck"], "A) Harper Lee")
quiz.add_question("What is the largest ocean on Earth?", ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"], "D) Pacific Ocean")
quiz.add_question("What is the capital city of France?", ["A) Rome", "B) Madrid", "C) Berlin", "D) Paris"], "D) Paris")
quiz.add_question("Who composed 'Symphony No. 9', also known as the 'Choral Symphony'?", ["A) Ludwig van Beethoven", "B) Wolfgang Amadeus Mozart", "C) Johann Sebastian Bach", "D) Franz Schubert"], "A) Ludwig van Beethoven")
quiz.add_question("Which gas is most abundant in Earth's atmosphere?", ["A) Oxygen", "B) Nitrogen", "C) Carbon dioxide", "D) Helium"], "B) Nitrogen")
quiz.add_question("Who wrote 'The Great Gatsby'?", ["A) Ernest Hemingway", "B) F. Scott Fitzgerald", "C) John Steinbeck", "D) Harper Lee"], "B) F. Scott Fitzgerald")
quiz.add_question("What is the capital city of China?", ["A) Shanghai", "B) Beijing", "C) Hong Kong", "D) Taipei"], "B) Beijing")
quiz.add_question("Who is known as the 'Father of Geometry'?", ["A) Euclid", "B) Pythagoras", "C) Archimedes", "D) Aristotle"], "A) Euclid")
quiz.add_question("Which planet is known as the 'Red Planet'?", ["A) Mars", "B) Jupiter", "C) Saturn", "D) Venus"], "A) Mars")
quiz.add_question("Who wrote 'Pride and Prejudice'?", ["A) Charles Dickens", "B) Jane Austen", "C) Emily Brontë", "D) Virginia Woolf"], "B) Jane Austen")
quiz.add_question("What is the chemical formula for ammonia?", ["A) NH3", "B) N2", "C) H2O", "D) CO2"], "A) NH3")
quiz.add_question("Who painted the ceiling of the Sistine Chapel?", ["A) Michelangelo", "B) Leonardo da Vinci", "C) Raphael", "D) Donatello"], "A) Michelangelo")
quiz.add_question("What is the capital city of Russia?", ["A) Saint Petersburg", "B) Moscow", "C) Kiev", "D) Vladivostok"], "B) Moscow")
quiz.add_question("Which country is known as the 'Land of the Rising Sun'?", ["A) China", "B) Japan", "C) South Korea", "D) Thailand"], "B) Japan")
quiz.add_question("What is the chemical symbol for silver?", ["A) Si", "B) Ag", "C) S", "D) Au"], "B) Ag")
quiz.add_question("Who painted the 'Mona Lisa'?", ["A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Michelangelo"], "A) Leonardo da Vinci")
quiz.add_question("What is the capital city of India?", ["A) New Delhi", "B) Mumbai", "C) Kolkata", "D) Bangalore"], "A) New Delhi")
quiz.add_question("Which of the following is not a primary color of light?", ["A) Red", "B) Green", "C) Yellow", "D) Blue"], "C) Yellow")
quiz.add_question("What is the chemical formula for table salt?", ["A) NaCl", "B) H2O", "C) CO2", "D) NH3"], "A) NaCl")
quiz.add_question("Who is known as the 'Father of Medicine'?", ["A) Hippocrates", "B) Galen", "C) Aristotle", "D) Socrates"], "A) Hippocrates")
quiz.add_question("What is the largest mammal in the world?", ["A) African elephant", "B) Blue whale", "C) Giraffe", "D) Polar bear"], "B) Blue whale")
quiz.add_question("Who was the first woman to fly solo across the Atlantic Ocean?", ["A) Amelia Earhart", "B) Bessie Coleman", "C) Harriet Quimby", "D) Sally Ride"], "A) Amelia Earhart")
quiz.add_question("Which of the following is a type of rock?", ["A) Neutron", "B) Marble", "C) Electron", "D) Proton"], "B) Marble")
quiz.add_question("What is the chemical symbol for potassium?", ["A) P", "B) Po", "C) K", "D) Pt"], "C) K")
quiz.add_question("Who discovered the theory of evolution by natural selection?", ["A) Charles Darwin", "B) Gregor Mendel", "C) Alfred Russel Wallace", "D) Jean-Baptiste Lamarck"], "A) Charles Darwin")
quiz.add_question("What is the capital city of Canada?", ["A) Toronto", "B) Montreal", "C) Vancouver", "D) Ottawa"], "D) Ottawa")
quiz.add_question("Who wrote 'The Catcher in the Rye'?", ["A) J.D. Salinger", "B) F. Scott Fitzgerald", "C) Ernest Hemingway", "D) John Steinbeck"], "A) J.D. Salinger")
quiz.add_question("What is the chemical symbol for lead?", ["A) L", "B) Li", "C) Pb", "D) Pu"], "C) Pb")
quiz.add_question("Who was the first woman to win a Nobel Prize?", ["A) Marie Curie", "B) Mother Teresa", "C) Ada Lovelace", "D) Amelia Earhart"], "A) Marie Curie")
quiz.add_question("What is the hardest natural substance on Earth?", ["A) Diamond", "B) Graphite", "C) Quartz", "D) Topaz"], "A) Diamond")
quiz.add_question("Who wrote 'Hamlet'?", ["A) William Shakespeare", "B) Christopher Marlowe", "C) John Milton", "D) Geoffrey Chaucer"], "A) William Shakespeare")
quiz.add_question("What is the chemical symbol for oxygen?", ["A) O", "B) Ox", "C) Co", "D) Oz"], "A) O")
quiz.add_question("Who invented the telephone?", ["A) Alexander Graham Bell", "B) Thomas Edison", "C) Nikola Tesla", "D) Guglielmo Marconi"], "A) Alexander Graham Bell")
quiz.add_question("What is the chemical formula for carbon dioxide?", ["A) CO2", "B) CH4", "C) CO", "D) C6H12O6"], "A) CO2")
quiz.add_question("Who painted 'The Starry Night'?", ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Claude Monet", "D) Salvador Dalí"], "A) Vincent van Gogh")
quiz.add_question("What is the capital city of Spain?", ["A) Barcelona", "B) Madrid", "C) Valencia", "D) Seville"], "B) Madrid")
quiz.add_question("Which of the following is a primary color?", ["A) Purple", "B) Green", "C) Orange", "D) Blue"], "D) Blue")
quiz.add_question("What is the chemical symbol for hydrogen?", ["A) H", "B) He", "C) Ho", "D) Hu"], "A) H")
quiz.add_question("Who wrote '1984'?", ["A) George Orwell", "B) Aldous Huxley", "C) Ray Bradbury", "D) Franz Kafka"], "A) George Orwell")
quiz.add_question("What is the chemical formula for water?", ["A) H2O", "B) CO2", "C) H2O2", "D) CH4"], "A) H2O")
quiz.add_question("Who discovered penicillin?", ["A) Alexander Fleming", "B) Louis Pasteur", "C) Jonas Salk", "D) Marie Curie"], "A) Alexander Fleming")
quiz.add_question("What is the capital city of Italy?", ["A) Rome", "B) Milan", "C) Florence", "D) Venice"], "A) Rome")
quiz.add_question("Who composed 'Für Elise'?", ["A) Ludwig van Beethoven", "B) Wolfgang Amadeus Mozart", "C) Johann Sebastian Bach", "D) Franz Schubert"], "A) Ludwig van Beethoven")
quiz.add_question("What is the chemical symbol for silver?", ["A) Si", "B) Ag", "C) S", "D) Au"], "B) Ag")
quiz.add_question("Who wrote 'The Odyssey'?", ["A) Homer", "B) Virgil", "C) Sophocles", "D) Plato"], "A) Homer")
quiz.add_question("What is the chemical formula for ammonia?", ["A) NH3", "B) N2", "C) H2O", "D) CO2"], "A) NH3")
quiz.add_question("Who painted the ceiling of the Sistine Chapel?", ["A) Michelangelo", "B) Leonardo da Vinci", "C) Raphael", "D) Donatello"], "A) Michelangelo")




# question_number = random.randint(0,95)
# print(f"Question number: {question_number}")
# print("Question 1:", quiz.get_question(question_number))
# Accessing the options for the first question
# print("Options:", quiz.get_options(question_number))
# Accessing the correct answer for the first question
# print("Correct Answer:", quiz.get_correct_answer(question_number))
# print(f"There are {len(quiz1.questions)} questions available")
# print(f"There are also {len(quiz1.answers)} correct answers available")


# if "_name _" == "_main_":
#     quiz = QuizQuestions()