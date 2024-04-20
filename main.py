from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from writer import Writer
from score_board import ScoreBoard
from game import Game
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle1 = Paddle(position="left")
paddle2 = Paddle()
ball = Ball()


second_player = True if screen.numinput(
    title="Second Player", prompt="How many players will play?", maxval=2, minval=1) == 2 else False

score = ScoreBoard()

game = Game(ball=ball, score=score, paddle1=paddle1,
            paddle2=paddle2, screen=screen, second_player=second_player)

if second_player != None:
    game.start_game()


screen.exitonclick()
