from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
screen= Screen()


def avanti():
    timmy.forward(10)

def dietro():
    timmy.backward(10)

def sinistra():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def destra():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(avanti,"w")
screen.onkey(dietro,"s")
screen.onkey(sinistra,"a")
screen.onkey(destra,"d")
screen.onkey(clear,"c")

screen.exitonclick() 