from turtle import *
import random
import sys

setup(.9,.9,0,0)
tracer(1000)
bgcolor("black")
wh = window_height()/2
ww = window_width()/2
lst = [False]*40
lst2 = []
c = 2
for i in range(40):
    lst[i] = Turtle()
for t in lst:
    t.shape("turtle")
    t.color("white")
    t.penup()
    t.speed(0)
    t.goto(random.randint(-ww,ww),random.randint(-wh,wh))
    t.seth(random.randint(0,360))
    lst2.append([t.xcor(), t.ycor()])


while True:
    for i,t in enumerate(lst):
        if t.ycor() <= -wh or t.ycor() >= wh:
            t.left(random.randint(135,225))
        if t.xcor() <= -ww or t.xcor() >= ww:
            t.right(random.randint(135,225))
        t.fd(1)
        lst2[i] = [t.xcor(),t.ycor()]
        a,b = lst2[i][0], lst2[i][1]
        for idx,cor in enumerate(lst2):
            x,y = cor[0],cor[1]
            if idx != i:
                if x >= a - 6 and x <= a + 6:
                    if y >= b - 6 and y <= b + 6:
                        lst[idx].color("red")
                        lst[idx].circle(12)
                        del lst2[idx]
                        del lst[idx]






mainloop()
