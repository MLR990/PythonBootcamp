from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
start_positions = [-70, -40, -10, 20, 50, 80]

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet!", prompt="Pick your turtle! Enter a color: ")

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.fillcolor(colors[turtle_index])
    new_turtle.goto(x=-230, y=start_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.fillcolor()
            if user_bet == winning_color:
                print(f"You won! The correctly picked the {winning_color} turtle to win!")
            else:
                print(f"You lost! You picked {user_bet} but the {winning_color} turtle won!")

            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()

