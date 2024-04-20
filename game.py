from score_board import ScoreBoard
from ball import Ball
from paddle import Paddle
from writer import Writer
from turtle import Screen
import time


class Game:
    def __init__(self, ball: Ball, score: ScoreBoard, paddle1: Paddle, paddle2, screen: Screen = None, second_player: bool = True, winner_condition: int = 0) -> None:
        self.second_player = second_player
        self.ball = ball
        self.score = score
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.screen = screen
        self.maximum_score = winner_condition
        self.winner_condition = self.set_winner_condition()
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

    def set_winner_condition(self):
        if self.maximum_score != 0:
            return int(self.score.left_score.text) < self.maximum_score and int(self.score.right_score.text) < self.maximum_score
        else:
            return True

    def start_game(self):
        while self.set_winner_condition():
            self.screen.update()
            time.sleep(0.04)
            self.ball.move()

            if not self.second_player:
                move_y = 20
                print(self.paddle2.pos())
                if self.paddle2.ycor()+50 > 260:
                    move_y *= -1
                elif self.paddle2.ycor() == -260:
                    move_y *= -1
                ycor = self.paddle2.ycor() + move_y

                self.paddle2.goto((self.paddle2.xcor(), ycor))

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

            if not self.set_winner_condition():
                winner = ""
                if int(self.score.left_score.text) == self.maximum_score:
                    winner = "Left Side"
                else:
                    winner = "Right Side"
                end_game_message = Writer(
                    text=f"{winner} won the Game!", position=(0, 0), fontsize=35)
