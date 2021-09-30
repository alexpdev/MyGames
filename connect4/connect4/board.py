from turtle import RawTurtle

class Board:
    """ Area of the screen dedicated to the connect 4 game board.
    """
    def __init__(self,screen,corners,width,height,x,y):
        self.corners = corners
        self.screen = screen
        self.pen = RawTurtle(screen)
        self.pen.speed(8)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.spaces = []
        self.draw()
        self.draw_spaces()

    def draw(self):
        self.pen.up()
        self.pen.goto(self.corners[-1])
        self.pen.color("#ddd")
        self.pen.down()
        self.pen.begin_fill()
        for i in self.corners:
            self.pen.goto(i)
        self.pen.ht()
        self.pen.end_fill()
        return

    def check_winner(self,space):
        r, c = space.idx
        if  self.check_row(space,r,c) or \
            self.check_column(space,r,c) or \
            self.check_direction(space,r,c):
            return True
        return False

    def check_row(self,space,r,c):
        if space.state*4 in "".join([str(i.state) for i in self.spaces[r]]):
            return True

    def check_column(self,space,r,c):
        if space.state*4 in "".join([str(i[c].state) for i in self.spaces]):
            return True

    def check_direction(self,space,r,c):
        direct,score = [(-1,-1),(-1,1),(1,1),(1,-1)],[0,0]
        for i,(x,y) in enumerate(direct):
            idx = 0 if i % 2 == 0 else 1
            score[idx] += self.check_angle(space,r,c,x,y,(x,y))
            if max(score) >= 3: return True
        return False

    def check_angle(self,space,r,c,x,y,i):
        if r+x >= 0 and r+x < 6 and c+y >= 0 and c+y < 7:
            if self.spaces[r+x][c+y].state == space.state:
                return 1 + self.check_diag(space,r,c,x+i[0],y+i[1],i)
            return 0
        return 0

    def animate_drop(self,space):
        r,c = space.idx
        for i in range(r):
            self.spaces[i][c].draw()
            self.spaces[i][c].remove()
        return

    def space_empty(self,space):
        r,c = space.idx
        if r == len(self.spaces)-1 or self.spaces[r+1][c].state:
            return space
        for row in range(r+1,len(self.spaces)):
            if self.spaces[row][c].state:
                return self.spaces[row-1][c]
        return self.spaces[len(self.spaces)-1][c]


    def find_space(self,x,y):
        for row in self.spaces:
            cent,rad = row[0].center, row[0].radius
            if y > cent[1] - rad and y < cent[1] + rad:
                return self.search_column(row,x)
        return False

    def search_column(self,row,x):
        for space in row:
            x2 = space.center[0]
            if x > x2-space.radius and x < x2 + space.radius:
                return space
        return False

    def draw_spaces(self):
        row,size = [],self.width/7
        radius = (size*.9)/2
        x,y = self.corners[0]
        for j in range(6):
            for i in range(7):
                space_x = x + (size*i)
                space_y = y - (size*j)
                center = space_x+(size/2),space_y-(size/2)
                color = "#643"
                idx = (j,i)
                space = Space(self,center,radius,color,idx)
                row.append(space)
            self.spaces.append(row)
            row = []
        return

class Space(RawTurtle):
    """ circles drawn on the window for players to assign their color """
    def __init__(self,board,center,radius,color,idx):
        RawTurtle.__init__(self,board.screen)
        self.board = board
        self.center = center
        self.radius = radius
        self.state = None
        self.idx = idx
        self._bgcolor = color
        self.color(color)
        self.up()
        self.speed(5)
        self.goto(self.center[0],self.center[1]-self.radius)
        self.ht()
        self.down()
        self.draw()

    def neighbor_left(self):
        r,c = self.idx
        if c == 0: return None
        return self.board.spaces[r][c-1]

    def neighbor_right(self):
        r,c = self.idx
        if c == 6: return None
        return self.board.spaces[r][c+1]

    def neighbor_below(self):
        r,c = self.idx
        if r == 5: return None
        return self.board.spaces[r+1][c]

    def neighbor_bl(self):
        r,c = self.idx
        if r == 5 or c == 0: return None
        return self.board.spaces[r+1][c-1]

    def neighbor_br(self):
        r,c = self.idx
        if r == 5 or c == 6: return None
        return self.board.spaces[r+1][c+1]

    def neighbors(self):
        lst = [self.neighbor_left(),self.neighbor_right(),
               self.neighbor_bl(),self.neighbor_below(),
               self.neighbor_br()]
        return lst


    def draw(self,color=None):
        if color:
            self.fillcolor(color)
        else:
            self.fillcolor(self._bgcolor)
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()
        return


    def remove(self):
        self.clear()
        self.draw()
        return
