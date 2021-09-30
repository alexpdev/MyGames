import random
import time
from datetime import datetime
from itertools import product
from turtle import RawTurtle, Screen

class Window:
    def __init__(self,w=.9,h=.9,x=0,y=0):
        self.screen = Screen()
        self.screen.setup(w,h,x,y)
        self.screen.bgcolor("wheat")
        self.screen.colormode(255)
        self.screen_width = (((self.screen.window_width())*.98)//12)*12
        self.screen_height = (((self.screen.window_height())*.95)//12)*12
        self.width = self.screen_width/2
        self.height = self.screen_height/2

    def pen(self):
        turt = RawTurtle(self.screen)
        turt.ht()
        turt.speed(0)
        turt.up()
        turt.goto(-self.width,self.height)
        turt.down()
        return turt


