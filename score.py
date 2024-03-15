from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.u_scoreboard()
        self.hideturtle()

    def u_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 10
        self.clear()
        self.u_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over ", align="center", font=("Arial", 24, "normal"))
