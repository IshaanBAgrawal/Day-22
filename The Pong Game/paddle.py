from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.goto((x_cor, y_cor))

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)
