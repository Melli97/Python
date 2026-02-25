from turtle import Turtle, Screen
import random
screen= Screen()
screen.colormode(255)  

timmy = Turtle()
timmy.shape("turtle")

def colore_casuale():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Spirograph
numero_cerchi = 36  # quanti cerchi compongono lo spirograph
angolo = 360 / numero_cerchi  # rotazione tra un cerchio e l'altro
raggio = 100

for _ in range(numero_cerchi):
    timmy.color(colore_casuale())   # colore casuale per ogni cerchio
    timmy.circle(raggio)             # disegna il cerchio
    timmy.right(angolo)              # ruota per il prossimo cerchio

screen.exitonclick()