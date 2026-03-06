from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # inizializza la Turtle
        self.score = 0  # variabile che salva il punteggio
        self.color("white")  # colore del testo
        self.penup()  # evita di disegnare linee
        self.goto(0, 270)  # posizione dello score in alto
        self.hideturtle()  # nasconde la freccia della turtle
        self.update_score()  # scrive lo score iniziale

    def update_score(self):
        self.clear()  # cancella il testo precedente
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        # scrive il punteggio aggiornato sullo schermo

    def increase_score(self):
        self.score += 1  # aumenta il punteggio
        self.update_score()  # aggiorna il testo sullo schermo

    def game_over(self):
        self.goto(0,0)  # va al centro dello schermo
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
        # scrive GAME OVER quando il gioco finisce