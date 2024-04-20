from writer import Writer
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.left_score = Writer(fontsize=35, text=0, position=(-50, 230))
        self.right_score = Writer(fontsize=35, text=0, position=(50, 230))

        # self.write(arg=self.left_score, position=(50, 230))
        # self.write(arg=self.right_score, position=(-50, 230))

    def increase_left_score(self):
        # self.left_score += 1
        # self.clear()
        # self.update_score()
        self.left_score.change_text(text=int(self.left_score.text) + 1)

    def increase_right_score(self):
        # self.right_score += 1
        # self.clear()
        # self.update_score()
        self.right_score.change_text(text=int(self.right_score.text) + 1)

    def clear_scores(self):
        self.clear()

    def update_score(self):
        self.write(arg=self.left_score, position=(50, 230))
        self.write(arg=self.right_score, position=(-50, 230))
