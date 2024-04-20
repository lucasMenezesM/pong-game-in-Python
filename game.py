from score_board import ScoreBoard
from ball import Ball
from paddle import Paddle
from turtle import Screen
import time


class Game:
    def __init__(self, ball: Ball, score: ScoreBoard, paddle1: Paddle, paddle2, screen: Screen = None, second_player: bool = True) -> None:
        self.second_player = second_player
        self.ball = ball
        self.score = score
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.screen = screen
        self.set_controls()

    def set_controls(self):
        print(f"Second player? {self.second_player}")
        self.screen.listen()
        if self.second_player:
            self.screen.onkey(self.paddle2.move_up, "Up")
            self.screen.onkey(self.paddle2.move_down, "Down")

            self.screen.onkey(self.paddle1.move_up, "w")
            self.screen.onkey(self.paddle1.move_down, "s")
        else:
            self.screen.onkey(self.paddle1.move_up, "Up")
            self.screen.onkey(self.paddle1.move_down, "Down")

    def start_game(self):
        while True:
            time.sleep(0.01)
            self.ball.move()

            if not self.second_player:
                move_y = 20
                print(self.paddle2.pos())
                if self.paddle2.ycor()+50 > 260:
                    move_y *= -1
                elif self.paddle2.ycor() == -260:
                    move_y *= -1
                ycor = self.paddle2.ycor() + move_y
                # elif ycor == -280:
                #     move_y
                self.paddle2.goto((self.paddle2.xcor(), ycor))
                # if self.paddle2.ycor() != 280 and self.paddle2.ycor() > 0:
                #     self.paddle2.move_up()
                # elif self.paddle2.ycor() != -280 and self.paddle2.ycor() < 0:
                #     self.paddle2.move_down()
                # else:
                #     self.paddle2.move_up()

            if self.ball.distance(self.paddle1.xcor(), self.paddle1.ycor() + 40) < 25 or self.ball.distance(self.paddle1.xcor(), self.paddle1.ycor() + -40) < 25 or self.ball.distance(self.paddle1) < 25:

                self.ball.bounce(direction="horizontal")

            if self.ball.distance(self.paddle2.xcor(), self.paddle2.ycor() + 40) < 25 or self.ball.distance(self.paddle2.xcor(), self.paddle2.ycor() + -40) < 25 or self.ball.distance(self.paddle2) < 25:

                self.ball.bounce(direction="horizontal")

            if self.ball.ycor() > 280 or self.ball.ycor() < -280:

                self.ball.bounce(direction="vertical")

            if self.ball.xcor() > 400:
                self.score.increase_left_score()
                self.ball.home()

            if self.ball.xcor() < -400:
                self.score.increase_right_score()
                self.ball.home()
