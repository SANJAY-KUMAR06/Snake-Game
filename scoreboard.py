from turtle import Turtle

with open("data.txt") as file:
    _high_score = file.read()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(_high_score)
        self.color("White")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()  # hides the turtle arrow
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.score}, High Score:{self.high_score}", move=False, align="center",
                   font=("Arial", 23, "normal"))  # allows to write

    def reset(self):
        with open("data.txt", mode="w") as updateFile:
            updateFile.write(str(self.high_score))
        if self.score > self.high_score:  # this is when score of player is greater than previous high score
            self.high_score = self.score
        self.score = 0  # after game ends the score is set to 0 again
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()
