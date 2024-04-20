from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from writer import Writer
from score_board import ScoreBoard
from game import Game
import pygame

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
pygame.init()
pygame.mixer.music.load("music.mp3")

paddle1 = Paddle(position="left")
paddle2 = Paddle()
ball = Ball()

second_player = True if screen.numinput(
    title="Second Player", prompt="How many players will play?", maxval=2, minval=1) == 2 else False

winner_condition = int(screen.textinput(
    title="Winner Condition", prompt="Type the maximum score to win the game. Or type 0 if you don't want a maximum score."))

score = ScoreBoard()

game = Game(ball=ball, score=score, paddle1=paddle1,
            paddle2=paddle2, screen=screen, second_player=second_player, winner_condition=winner_condition)

if second_player != None and winner_condition != None:
    pygame.mixer.music.play()
    game.start_game()

screen.exitonclick()
