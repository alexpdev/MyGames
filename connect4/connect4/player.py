import random
import time

class Player:
    """ User Player Class controlled by end user """
    def __init__(self,number,color):
        self.number = number
        self.color = color
        self.name = "P" + str(self.number)

    def __str__(self):
        return "Player " + str(self.number)

    def turn(self):
        pass


class Ai(Player):
    def __init__(self,number,color,board,window):
        super().__init__(number,color)
        self.board = board
        self.window = window
        self.name = "Ai" + str(self.number)

    def turn1(self):
        lst = list(range(6))
        random.shuffle(lst)
        time.sleep(2.2)
        col = random.choice(lst)
        pos = self.board.spaces[0][col].center
        self.window.activate_space(*pos)

    def turn(self):
        spaces = self.board.spaces
        for x,space in enumerate(self.board.spaces[0]):
            btm = self.board.space_empty(space)
            neighbors = btm.neighbor()
        s = self.weigh_options(lo,hi,lpos,hpos)
        self.window.activate_space(*s)

    def weigh_options(self,lo,hi,lpos,hpos):
        if hi == 3 or abs(lo) < hi: x,y  =  hpos
        else: x,y = lpos
        self.window.activate_space(*self.board.spaces[x][y].center)












