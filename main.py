import turtle
from turtle import Turtle, Screen
import random
import time

all_turtle = []
colors = ['red', 'blue', 'white',
          'pink', 'green', 'yellow', 'black']
y_positions = [-260, -170, -85, 0, 85, 170, 260]
screen = Screen()
screen.title('TURTLE RACING GAME 2022')
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

for index in range(7):
    new_tur = Turtle(shape='turtle')
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()
    new_tur.goto(x=-355, y=y_positions[index])
    new_tur.color(colors[index])
    all_turtle.append(new_tur)

user_choice = turtle.textinput('WELCOME TO THE GAME', 'Which Turtle Is Winning?')
start = time.time()

play = True
while play:
    for turtle_obj in all_turtle:
        if turtle_obj.xcor() > 332:
            play = False
            end = time.time()
            winner = turtle_obj.pencolor()
            if winner == user_choice:
                turtle_obj.write(
                    f'Hey Congratulations!! You won! {winner} turtle won the race in {end - start:.2f} seconds',
                    font=('Tacoma', 14, 'bold'), align='right')
            else:
                turtle_obj.write(
                    f'Damn! You lose! {winner} turtle won the race in {end - start:.2f} seconds',
                    font=('Tacoma', 14, 'bold'), align='right')
        pace = random.randint(0, 7)
        turtle_obj.forward(pace)

screen.exitonclick()
