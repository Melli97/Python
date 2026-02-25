from turtle import Turtle, Screen
import random
screen= Screen()
screen.colormode(255)  # <- importantissimo per RGB

timmy = Turtle()
timmy.shape("turtle")
color = ["red","orange","black","yellow","brown","pink","blue"]
timmy.pensize(15)
timmy.speed("fastest")

distanza = [0,90,180,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(50):
    timmy.color(random_color())
      
    timmy.forward(30)
    timmy.setheading(random.choice(distanza))  





screen.exitonclick()