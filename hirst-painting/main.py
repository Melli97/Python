import random
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
timmy.goto(-250, -200)   # sposta 250 pixel a sinistra

color_list=[(245, 243, 239), (247, 242, 244), (204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123),
             (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), 
             (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), 
             (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90),
               (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90),
                 (13, 71, 68), (213, 178, 183), (179, 191, 207)]

def painting():
# PRIMA RIGA
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)     
        timmy.forward(50)

    # Torna all'inizio
    timmy.backward(500)

    # Sali sopra
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)

for _ in range(10):
    painting()


screen.exitonclick()
