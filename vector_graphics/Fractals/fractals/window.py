import random
from turtle import Screen, RawTurtle


def gen_screen(width,height,color=None):
    screen = Screen()
    if not color:
        screen.screensize(width,height)
    else:
        screen.screensize(width,height,color)
    return screen

class Turt(RawTurtle):
    def __init__(self,screen):
        super().__init__(screen)
        self.screen = screen

    @property
    def x(self):
        return self.xcor()

    @property
    def y(self):
        return self.ycor()

    @property
    def position(self):
        return self.pos()

    @property
    def win_width(self):
        return self.screen.window_width()

    @property
    def win_height(self):
        return self.screen.window_height()

def draw_tree(turtle,distance,angle):
    if distance >= 10:
        print(distance)
        turtle.forward(distance)
        turtle.right(angle)
        draw_tree(turtle,distance*.8,angle*1.2)
        turtle.left(angle*2)
        draw_tree(turtle,distance*.65,angle*.9)
        turtle.right(angle)
        turtle.backward(distance)




def draw_fractals(turtle):
    turtle.up()
    turtle.goto(0,-150)
    turtle.down()
    turtle.setheading(90)
    turtle.speed(10)
    turtle.screen.tracer(3)
    angle = 40
    distance = 100
    draw_tree(turtle,distance,angle)
    turtle.hideturtle()
    turtle.screen.mainloop()




if __name__ == "__main__":
    screen = gen_screen(800,600,"#efe")
    turtle = Turt(screen)
    draw_fractals(turtle)
