from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
# timmy.color("orange")

color = ["red","orange","black","yellow","brown","pink","blue"]

for lati in range(3 , 11): # da 3 a 10 lati
    timmy.color(random.choice(color))
    angolo = 360/lati       # calcolo dell'angolo interno

    for _ in range(lati):
        timmy.forward(100)
        timmy.left(angolo)


screen= Screen()

screen.exitonclick()