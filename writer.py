from turtle import Turtle


class Writer(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False, text: str = "", position: tuple = (0, 0), align: str = "center", fontsize: int = 15, font: str = "Arial") -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.goto(position)

        self.text = text
        self.align = align
        self.font_size = fontsize
        self.font = font

        self.write(arg=self.text, align=self.align, font=(
            f"{self.font}", self.font_size, "normal"))

    def change_text(self, text: str):
        self.clear()
        self.text = text
        self.write(arg=self.text, align=self.align, font=(
            f"{self.font}", self.font_size, "normal"))
