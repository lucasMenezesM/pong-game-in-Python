from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, position: str = "right") -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(350, 0) if position == "right" else self.goto(-350, 0)

    def move_up(self):
        # self.setheading(90)
        self.goto(self.xcor(), self.ycor()+30)

    def move_down(self):
        # self.setheading(270)
        self.goto(self.xcor(), self.ycor()-30)
