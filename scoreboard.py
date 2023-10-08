from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("high_score.txt") as content:
            self.high_score = int(content.read())
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=260)
        self.write(arg=f"SCORE : {self.score} || High score : {self.high_score}", move=True, align="center", font=("Arial", 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as content:
                content.write(f'{self.high_score}')
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align="center", font=("Arial", 24 , "bold"))
