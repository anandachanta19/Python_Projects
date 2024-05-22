from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.pu()
        self.setpos(x=0, y=270)
        self.ht()
        self.color("white")
        self.write(arg=f"score: {self.score}", move=False, align="center", font=("Arial", 12, "bold"))

    def update_score(self):
        self.score += 1
        self.undo()
        self.write(arg=f"score: {self.score}", move=False, align="center", font=("Arial", 12, "bold"))
