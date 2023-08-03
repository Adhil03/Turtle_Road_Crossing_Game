from turtle import Turtle,Screen

FONT = ("Courier", 19, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 268)
        self.write(f"Level :{self.level} ", font=FONT)

    def inc_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level :{self.level} ", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def quit(self):
        self.goto(0, 0)
        self.write("click screen to EXIT GAME", align="center", font=FONT)
        screen = Screen()
        screen.exitonclick()
