# snake game

import os
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# setup the screen
window = turtle.Screen()
window.title("PythonSnake")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # turns off animation on the screen

# Snake head
head = turtle.Turtle()
head.speed(0)  # animation speed
head.shape("square")
head.color("Red")
head.penup()
head.goto(0, 0)
head.direction = "right"

# Snake food 
food = turtle.Turtle()
food.speed(0)  # animation speed
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:  0 High Score:  0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

# Main game loop
while True:
    window.update()

    # Check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # Hide segments after death
        for segment in segments:
            segment.goto(1000,1000)
        # Clear segment list
        segments.clear()

        # Score
        score = 0
        pen.clear()
        pen.write("Score:  {} High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #check for collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot on the screen
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        #add segment to Snake
        new_segment =  turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        # Score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score:  {} High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)   

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Check for head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide segments after death
            for segment in segments:
                segment.goto(1000,1000)

            # Clear segment list
            segments.clear()

            # Score
            score = 0
            pen.clear()
            pen.write("Score:  {} High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

window.mainloop()
