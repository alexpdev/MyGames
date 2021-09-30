from window import Window
from population import Population

def main():
    win = Window()
    turt = win.pen()
    win,turt,xlines = draw_x_lines(turt,win)
    win,turt,ylines = draw_y_lines(turt,win)
    win.screen.tracer(0)
    while True:
        pop = Population(xlines,ylines,win)
        pop.clear_grid()
        pop.fill_random()
        pop.play()
    win.screen.mainloop()

def draw_x_lines(turt,win):
    start,lines = turt.xcor(),[]
    while start < win.width:
        turt.goto(turt.xcor(),-win.height)
        lines.append(turt.xcor())
        turt.goto(turt.xcor()+12,turt.ycor())
        turt.goto(turt.xcor(),win.height)
        lines.append(turt.xcor())
        turt.goto(turt.xcor()+12,turt.ycor())
        start += 24
    turt.undo()
    return win,turt,lines

def draw_y_lines(turt,win):
    start,lines = turt.ycor(),[]
    while start > -win.height:
        turt.goto(-win.width,turt.ycor())
        lines.append(turt.ycor())
        turt.goto(turt.xcor(),turt.ycor()-12)
        turt.goto(win.width,turt.ycor())
        lines.append(turt.ycor())
        turt.goto(turt.xcor(),turt.ycor()-12)
        start -= 24
    turt.goto(-win.width,turt.ycor())
    lines.append(turt.ycor())
    return win,turt,lines

if __name__ == "__main__":
    main()
