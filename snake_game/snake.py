from turtle import Turtle, Screen
import time

# Costanti iniziali
STARTING_POSITION = [(0,0), (-20,0),(-40,0)]  # Posizioni iniziali dei segmenti
MOVE_DISTANCE = 20  # Distanza percorsa dalla testa ad ogni passo
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # Lista dei segmenti del serpente
        self.create_snake()  # Crea il serpente iniziale
        self.head = self.segments[0]  # Salva il riferimento alla testa

    def create_snake(self):
        # Crea i segmenti iniziali del serpente e li posiziona
        for position in STARTING_POSITION:
            self.add_segment(position)
            new_segment = Turtle("square")  # Segmento a forma di quadrato
            new_segment.color("white")  # Colore del segmento
            new_segment.penup()  # Non disegna linee quando si sposta
            new_segment.goto(position)  # Posiziona il segmento
            self.segments.append(new_segment)  # Aggiunge il segmento alla lista
    
    def move(self):
        # Muove il serpente: ogni segmento segue quello davanti
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Dal ultimo al secondo
            new_x = self.segments[seg_num - 1].xcor()  # Posizione x del segmento davanti
            new_y = self.segments[seg_num - 1].ycor()  # Posizione y del segmento davanti
            self.segments[seg_num].goto(new_x, new_y)  # Sposta il segmento corrente

        self.head.forward(MOVE_DISTANCE)  # Muove la testa in avanti


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Funzioni per cambiare direzione
    def up(self):
        if self.head.heading() != DOWN:  # Evita inversione a 180°
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)