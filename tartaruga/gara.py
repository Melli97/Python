from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

userbet = screen.textinput(
    title="Fai la tua scelta",
    prompt="Quale tartaruga vince la gara? Scrivi un colore:"
)

colors = ["red", "orange", "purple", "yellow", "blue", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []  # LISTA PER SALVARE LE TARTARUGHE

for turtle_position in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_position])
    timmy.goto(x=-230, y=y_positions[turtle_position])
    
    all_turtles.append(timmy)  # SALVIAMO LA TARTARUGA
    
if userbet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == userbet:
                print("Hai vinto!")
            else:
                print(f"Hai perso! Ha vinto {winning_color}")

screen.exitonclick()