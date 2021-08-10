from turtle import Turtle


class WinnerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def r_win(self):
        self.goto(x=200, y=0)
        self.write("You Win.", align="center", font=("Courier", 40, "normal"))
        self.goto(x=-200, y=0)
        self.write("You Lose.", align="center", font=("Courier", 40, "normal"))

    def l_win(self):
        self.goto(x=200, y=0)
        self.write("You Lose.", align="center", font=("Courier", 40, "normal"))
        self.goto(x=-200, y=0)
        self.write("You Win.", align="center", font=("Courier", 40, "normal"))


class ExitGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def exit(self):
        self.goto(x=0, y=-280)
        self.write(arg="Click anywhere on the screen to exit.", align="center", font=("Courier", 10, "normal"))
