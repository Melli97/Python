from turtle import Turtle, Screen
from snake import Snake  # Importa la classe Snake dal file snake.py
from food import Food
from scoreboard import Scoreboard
import time

# Imposta la finestra di gioco
screen = Screen()
screen.setup(width=600, height=600)  # Dimensione finestra
screen.bgcolor("black")  # Sfondo nero
screen.title("Snake Game")  # Titolo finestra
screen.tracer(0)  # Disattiva l'aggiornamento automatico della finestra (più veloce)

# Crea il serpente
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Riconosce i comandi della tastiera
screen.listen()  # Attiva l'ascolto dei tasti
screen.onkey(snake.up, "Up")  # Freccia su
screen.onkey(snake.down, "Down")  # Freccia giù
screen.onkey(snake.left, "Left")  # Freccia sinistra
screen.onkey(snake.right, "Right")  # Freccia destra

game_is_on = True

# Ciclo principale del gioco
while game_is_on:
    screen.update()  # Aggiorna la finestra (necessario perché tracer=0)
    time.sleep(0.1)  # Pausa tra un movimento e l'altro (controlla la velocità)
    
    snake.move()  # Muove il serpente

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
   # controlla se la testa esce dai bordi dello schermo
    if (
        snake.head.xcor() > 280 or   # supera il bordo destro
        snake.head.xcor() < -280 or  # supera il bordo sinistro
        snake.head.ycor() > 280 or   # supera il bordo superiore
        snake.head.ycor() < -280     # supera il bordo inferiore
    ):
        game_is_on = False           # ferma il ciclo del gioco
        scoreboard.game_over()       # mostra la scritta GAME OVER
    
    #collisione con il corpo serpente
    for segment in snake.segments[1:]:  #slicing IMPORTANTE
        if snake.head.distance(segment) < 10 :
            game_is_on = False           # ferma il ciclo del gioco
            scoreboard.game_over()       # mostra la scritta GAME OVER

screen.exitonclick()