"""creates purple rain"""


import random
from turtle import bgcolor,speed,seth,setup,color,penup,pendown,tracer,goto,shapesize,fd,ycor,clone,width,shape
import os
os.system("clear")
bgcolor("black")
speed(0)
tracer(300)
setup(.9,.9,1950,0)
seth(270)
color("purple")
width(.06)
shape("square")
penup()
lst = []
for i in range(300):
    tr = clone()
    goto(random.randint(-800, 800),random.randint(600,900))
    lst.append(tr)


while True:
    for tr in lst:
        tr.shapesize(stretch_wid=0.04, stretch_len=1.6, outline=None)
        tr.speed(0)
        tr.fd(random.randint(70,100))
        if tr.ycor() < -600:
            tr.goto(random.randint(-800, 800), random.randint(200, 400))