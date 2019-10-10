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

#-----initialize turtle-----
triangle = turtle.Turtle()
triangle.shape(shape)
triangle.shapesize(size)
triangle.fillcolor(filclr)

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(150, 125)
score_writer.hideturtle()

#-----game functions--------
def tri_clicked(x,y):
    update_score()
    change_position()

def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    triangle.penup()
    triangle.hideturtle()
    triangle.goto(new_xpos,new_ypos)
    triangle.showturtle()


def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)


#-----events----------------
triangle.onclick(tri_clicked)

wn = turtle.Screen()
wn.mainloop()