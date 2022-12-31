from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, sp_x, sp_y):
        new_x = self.xcor() + sp_x
        new_y = self.ycor() + sp_y
        self.goto(new_x, new_y)

    def refresh(self):
        self.goto(0, 0)
