class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.currency = 0
        self.badges = []

    def update_score(self, points):
        self.score += points

    def update_currency(self, amount):
        self.currency += amount

    def earn_badge(self, badge):
        self.badges.append(badge)

# Initialize player
player = Player("Player 1")