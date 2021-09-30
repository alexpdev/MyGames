from turtle import Screen, RawTurtle

def draw_line(t):
    t.setx(-100)
    c1 = t.position()
    t.setx(100)
    c2 = t.position()
    t.left(180)
    t.right(60)
    move_to_xpt(t,0)
    t.right(180)
    t.right(60)
    move_to_xpt(t,-100)

def move_to_xpt(t,pt):
    pos = t.xcor()
    while t.xcor() > pt + 1 or t.xcor() < pt -1:
        print(t.pos())
        t.fd(1)
    return

def leftDragon(t,sz,level):
    if level == 0:
        t.left(90)
        t.fd(sz)
    else:
        leftDragon(t, sz*.8, level-1)
        t.left(90)
        rightDragon(t, sz*8, level-1)

def rightDragon(t,sz,level):
    if level == 0:
        t.fd(sz)
        t.right(90)
    else:
        leftDragon(t, sz*.8, level-1)
        t.right(90)
        rightDragon(t, sz*.8, level-1)


window = Screen()
window.setup(1400,800,50,50)
t = RawTurtle(window)
t.up()
t.home()
print(t.pen())
t.down()
draw_line(t)
window.mainloop()
