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
    print("Spot was clicked!")


#-----events----------------
triangle.onclick(tri_clicked)

wn = triangle.Screen()
wn.mainloop()