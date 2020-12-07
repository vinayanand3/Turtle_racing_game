from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Name your Bet ', prompt='which turtle will win the race\n "magenta", "purple", "blue", "green", "yellow", "orange", "red"? Enter color: ')
colors = ["magenta", "purple", "blue", "green", "yellow", "orange", "red"]
any_turtle = []
y_coord = -160
is_race_on = True
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_coord)
    new_turtle.color(colors[turtle_index])
    y_coord += 50
    any_turtle.append(new_turtle)

while is_race_on:
    for single_turtle in any_turtle:
        single_turtle.fd(random.randint(0, 10))
        if single_turtle.xcor() > 230:
            is_race_on = False
            winning_color = single_turtle.pencolor()
            if user_bet == winning_color:
                print(f"you won, the {winning_color} is the winner")
            else:
                print(f"You lost, {winning_color} is the winner")


screen.exitonclick()
