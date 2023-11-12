from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/marwakhan/Desktop/my_file.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.score = self.high_score
            with open("/Users/marwakhan/Desktop/my_file.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    def Score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score  # Update the high score
            with open("/Users/marwakhan/Desktop/my_file.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.clear()
        self.score_update()


