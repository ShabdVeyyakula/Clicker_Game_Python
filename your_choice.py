# a121_catch_a_turtle.py
#-----import statements-----
import turtle

import random as rand

#-----game configuration----
filclr = "red"
size = 2
shape = "triangle"
score = 0
font_setup = ("Arial", 20, "normal")

#-----countdown variables-----
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter = turtle.Turtle()

counter.penup()
counter.hideturtle()
counter.goto(-150,125)

#-----initialize turtle-----
triangle = turtle.Turtle()
triangle.shape(shape)
triangle.fillcolor(filclr)

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(150, 125)
score_writer.hideturtle()

#-----game functions--------
def tri_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        counter.hideturtle()
        triangle.hideturtle()
        score_writer.hideturtle()


def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    global size
    size = rand.randint(1,3)
    triangle.shapesize(size)
    triangle.penup()
    triangle.hideturtle()
    triangle.goto(new_xpos,new_ypos)
    triangle.showturtle()


def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
triangle.onclick(tri_clicked)
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("orange")
wn.mainloop()