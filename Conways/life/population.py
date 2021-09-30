import time
import random
from datetime import datetime
from turtle import RawTurtle
from colors import gen_color


class Population:
    def __init__(self,xlines,ylines,window):
        self.screen = window.screen
        self.state = []
        self.final = False
        self.draw_world(xlines,ylines)

    def draw_world(self,xlines,ylines):
        self.grid = []
        for yi,y in enumerate(ylines[:-1]):
            row = []
            for xi,x in enumerate(xlines[1:]):
                cor,index = (x,y),(yi,xi)
                citizen = Citizen(self.screen,cor,index,self)
                self.position_citizen(citizen,cor)
                row.append(citizen)
            self.grid.append(row)
        self.screen.update()
        return

    def position_citizen(self,citizen,cor):
        citizen.up()
        citizen.goto(cor)
        citizen.down()
        return

    def dt(self):
        iso = datetime.isoformat(datetime.now())
        stamp = datetime.timestamp(datetime.now())
        seed = iso + str(stamp)
        return seed

    def fill_random(self):
        for i in range(len(self.grid)):
            row = self.grid[i]
            k = random.randrange(len(row))
            random.seed(a=self.dt())
            for i in random.sample(row,k):
                i.fill()
            self.screen.update()

    def clear_grid(self):
        for row in self.grid:
            for item in row:
                item.clear()
            self.screen.update()

    def play(self):
        while True:
            self.generation()
            if self.final:
                return

    def generation(self):
        flip = []
        for row in self.grid:
            for citizen in row:
                if self.outcome(citizen):
                    flip.append(citizen)
        self.check_state(flip)
        self.toggle_citizen_state(flip)

    def check_state(self,flip,temp_=[]):
        self.state.append(flip)
        if len(self.state) <= 20: return
        del self.state[0]
        for state in self.state:
            if state not in temp_:
                temp_.append(state)
        if len(temp_) <= 3:
            self.final = True
        return

    def outcome(self,citizen):
        ct = citizen.neighbors_state()
        if citizen.filled:
            if ct < 2 or ct > 3:
                return True
        elif ct == 3:
            return True
        return False

    def toggle_citizen_state(self,flip):
        for citizen in flip:
            citizen.flip()
        self.screen.update()
        time.sleep(1.4)
        return

class Citizen(RawTurtle):
    def __init__(self,screen,cor,idx,population):
        RawTurtle.__init__(self,screen)
        x,y = cor
        self.filled = False
        self.color(gen_color())
        self.idx = idx
        self.pop = population
        nw = (x-12,y)
        ne = (x,y)
        sw = (x-12,y-12)
        se = (x,y-12)
        self.corners = (nw,sw,se,ne)
        self.speed(0)
        self.ht()

    def fill(self):
        self.down()
        self.begin_fill()
        for i in self.corners:
            self.goto(i)
        self.end_fill()
        self.filled = True
        return

    def flip(self):
        if self.filled:
            self.clear()
        else:
            self.color(gen_color())
            self.fill()

    def clear(self):
        self.filled = False
        return super().clear()

    def get_neighbors(self):
        r, c = self.idx[0], self.idx[1]
        self.neighbors = {
            "nw" : ((r-1, c-1), None),
            "w" : ((r, c-1), None),
            "sw" : ((r+1, c-1), (0, c-1)),
            "n" : ((r-1, c), None),
            "s" : ((r+1, c), (0, c)),
            "ne" : ((r-1, c+1), (r-1, 0)),
            "e" : ((r, c+1), (r, 0)),
            "se" : ((r+1, c+1), [(0, c+1), (r+1, 0), (0, 0)]),
        }
        return self.neighbors

    def neighbors_state(self):
        grid,ct = self.pop.grid, 0
        for k,v in self.get_neighbors().items():
            if k == "se":
                if self.check_se(k,v,grid):
                    ct += 1; continue
                else:
                    continue
            idx,alt = v
            try:
                if grid[idx[0]][idx[1]].filled:
                    ct += 1
            except:
                if grid[alt[0]][alt[1]].filled:
                    ct += 1
        return ct

    def check_se(self,k,v,grid):
        idx,lst = v
        try:
            return grid[idx[0]][idx[1]].filled
        except:
            item = None
            if idx[0] >= len(grid) and idx[1] >= len(grid[0]):
                item = lst[2]
            elif idx[0] >= len(grid):
                item = lst[0]
            else:
                item = lst[1]
            return grid[item[0]][item[1]].filled