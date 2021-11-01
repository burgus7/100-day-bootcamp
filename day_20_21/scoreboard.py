from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)


    def game_over(self, msg):
        self.home()
        self.write("GAME OVER!", move=False, align="center", font=("Courier", 24, "normal"))
        self.goto(0, -30)
        self.write(msg.title(), move=False, align="center", font=FONT)