# a121_catch_a_turtle.py
#-----import statements-----
import turtle as triangle
import random as rand

#-----game configuration----
filclr = "red"
size = 3
shape = "triangle"
score = 0

#-----initialize turtle-----
triangle.shape(shape)
triangle.shapesize(size)
triangle.fillcolor(filclr)

#-----game functions--------
def tri_clicked(x,y):
    change_position()

def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    triangle.penup()
    triangle.hideturtle()
    triangle.goto(new_xpos,new_ypos)
    triangle.showturtle()



#-----events----------------
triangle.onclick(tri_clicked)

wn = triangle.Screen()
wn.mainloop()