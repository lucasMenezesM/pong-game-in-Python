from turtle import Turtle
import random

UP_DIRECTIONS = []


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.shape("circle")
        self.penup()
        self.move_y = 10
        self.move_x = 10

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce(self, direction: str):
        if direction == "vertical":
            self.move_y *= -1
        elif direction == "horizontal":
            self.move_x *= -1

    # def reflect(self, direction: str):
    #     if direction == "up":
    #         if self.heading() > 90 and self.heading() < 270:
    #             self.setheading(random.randint(60, 120))
    #         else:
    #             self.setheading(random.randint(240, 300))
    #     elif direction == "down":
    #         if self.heading() > 90 and self.heading() < 270:
    #             self.setheading(random.randint(60, 120))
    #         else:
    #             self.setheading(random.randint(240, 300))
    #     elif direction == "left":
    #         self.setheading(random.randint(150, 210))
    #     else:
    #         self.setheading(random.randint(-30, 30))
