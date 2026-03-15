from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()  # Load high score from file
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        """Load the high score from file"""
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            # If file doesn't exist, create it with 0
            with open("highscore.txt", "w") as file:
                file.write("0")
            return 0
        except ValueError:
            # If file is corrupted, reset to 0
            return 0

    def save_high_score(self):
        """Save the high score to file"""
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        """Update the display with current score and high score"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                  align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the game and update high score if needed"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """Display game over message (alternative to reset)"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # Check if new high score was achieved
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        """Increase current score"""
        self.score += 1
        # Update high score if current score exceeds it
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()