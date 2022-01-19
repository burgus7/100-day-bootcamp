import turtle as t
import time

FONT = ("Courier", 24, "normal")
SMALLER_FONT = ("Courier", 20, "normal")

class Scoreboard:
    def __init__(self):
        self.level = 1
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        t.penup()
        t.hideturtle()
        self.write_score()
        self.is_game_on = True
        self.start_counter = 3

    def countdown(self, screen):
        # TODO implement countdown so the cars start moving before the turtle can
        t.color("black")
        t.goto(0, 260)
        for i in range (3, 0, -1):
            time.sleep(1)
            t.write(f"Get Ready...", font=SMALLER_FONT, align="center")
            t.write(f"{i}", font=FONT, align="center")
            screen.update()
        t.write(f"Get Ready...", font=SMALLER_FONT, align="center")
        t.write(f"GO!", font=FONT, align="center")

    def write_score(self):
        t.color("black")
        t.goto(-290, 260)
        t.write(f"Level: {self.level}", font=FONT)

    def clear_text(self):
        t.color("lightblue")
        t.goto(-300, 300)
        t.begin_fill()
        t.goto(300, 300)
        t.goto(300, 250)
        t.goto(-300, 250)
        t.goto(-300, 300)
        t.end_fill()

    def level_up(self):
        self.clear_text()
        self.level += 1
        self.write_score()

    def game_over(self):
        t.color("lightblue")
        t.goto(-300, 300)
        t.begin_fill()
        t.goto(300, 300)
        t.goto(300, -300)
        t.goto(-300, -300)
        t.goto(-300, 300)
        t.end_fill()
        t.home()
        t.color("black")
        t.write("Game Over", font=FONT, align="center")
        t.goto(0, -30)
        t.write(f"You got to Level {self.level}", font=SMALLER_FONT, align="center")
        t.goto(0, -60)
        disp_text = f"High Score: {self.high_score}"
        if self.level > self.high_score:
            self.high_score = self.level
            with open("high_score.txt", mode="r") as data:
                data.write(f"{self.high_score}")
            disp_text = "New High Score!!"
        t.write(f"{disp_text}", font=SMALLER_FONT, align="center")
        t.done()
        # TODO add best score
        # t.goto(0, -60)
        # t.write(f"Best Score: {self.level}", font=SMALLER_FONT, align="center")
        # TODO add retry button


