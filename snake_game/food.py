from turtle import Turtle
import random

class Food(Turtle):
    """Classe che rappresenta il cibo del serpente."""

    def __init__(self):
        super().__init__()  # Inizializza la Turtle
        self.shape("circle")  # Forma del cibo: cerchio
        self.penup()  # Evita che la Turtle disegni linee
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Riduce le dimensioni del cerchio
        self.color("blue")  # Colore del cibo
        self.speed("fastest")  # Velocità massima dello spostamento (nessuna animazione lenta)
        self.refresh()  # Posiziona il cibo in una posizione casuale iniziale

    def refresh(self):
        """Sposta il cibo in una nuova posizione casuale sullo schermo."""
        random_x = random.randint(-280, 280)  # Coordinate x casuali (entro i bordi della finestra)
        random_y = random.randint(-280, 280)  # Coordinate y casuali
        self.goto(random_x, random_y)  # Sposta il cibo nella nuova posizione