from turtle import *
import random as rand
import sys

def sp(dist):
    setup(1.0,.9,0,0)
    tracer(55)
    colormode(255)
    wheight = window_height()/2
    wwidth = window_width()/2
    bgcolor(0,0,0)
    t1 = Turtle()
    t2 = Turtle()
    t3 = Turtle()
    tlist = [t1, t2, t3]
    for t in tlist:
        t.color('grey')
        t.shape('turtle')
        t.width(2)
        t.penup()
        t.speed(10)
    tdraw(tlist, wwidth, wheight, dist)

def tdraw(tlist, wwidth, wheight, dist):
    colos = [i for i in range(256) if i == 0 or i % 5 == 0]
    print(colos)
    for t in tlist:
        t.pendown()
        t.seth(rand.randint(0,360))
    while True:
        for t in tlist:
            t.color(rand.choice(colos),rand.choice(colos),rand.choice(colos))
            t.fd(20)
            if t.xcor() >= wwidth - dist or t.xcor() <= (-1 * wwidth) + dist:
                t.right(rand.randint(135,225))
            if t.ycor() >= wheight - dist or t.ycor() <= (-1 * wheight) + dist:
                t.left(rand.randint(135,225))



sp(3)





