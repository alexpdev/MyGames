"""creates purple rain"""
"""requires python turtle module and tkinter"""


import random
from turtle import bgcolor,speed,seth,setup,color,penup,pendown,tracer,goto,shapesize,fd,ycor,clone,width,shape
import os
os.system("clear")
bgcolor("black")
speed(0)
tracer(300)
setup(.8,.6)
seth(270)
color("purple")
width(.06)
shape("square")
penup()
lst = []
for i in range(300):
    tr = clone()
    goto(random.randint(-800, 800),random.randint(500,800))
    lst.append(tr)


while True:
    for tr in lst:
        tr.shapesize(stretch_wid=0.04, stretch_len=1.6, outline=None)
        tr.speed(0)
        tr.fd(random.randint(70,100))
        if tr.ycor() < -300:
            tr.goto(random.randint(-800, 800), random.randint(200, 400))