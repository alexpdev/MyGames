import time
import random
from turtle import RawTurtle, _Screen as Screen

from connect4.board import Board
from connect4.player import Player, Ai

class Window(Screen):

    """Class to generate game window, tkcanvas subclass.
    """

    def __init__(self,color="#643",mode=1):

        """ Constructor for TK window.
            color {str} -- hex color string (default: {None})
        """

        super().__init__()
        self.player_mode = mode
        self.new_game(color)

    def new_game(self,color):

        """ Starts a New Game, Draws game board and creates Players.
            Args: color{str} - Hex-Color passed along from constructor.
        """

        self.setup(.8,.9,1000,0)
        self.width = (self.window_width()*.9)
        self.height = (self.window_height()*.9)
        self.x = self.width/2
        self.y = self.height/2
        # ^ dimensions of game board

        self.font = ('Arial',20,'bold'),"#f50"
        # ^ Game Status Messages written above Game Board

        self.winner = None
        # ^ slot is adjusted once a winner is established.

        self.bgcolor(color)
        self.start_message()
        self.delay(8)
        self.tracer(2)
        # functions for controlling animation speed

        self.game_board()
        self.create_players()
        self.player.turn()

    def start_message(self):

        """ Creates Pen for drawing game update messages above the board. """

        self.pen = RawTurtle(self)
        self.pen.ht()
        self.pen.up()
        self.pen.color(self.font[1])
        self.pen.goto(0,self.y)
        self.pen.write("New Game",align="center",font=self.font[0])
        return

    def create_players(self):

        """ Creates 2 player objects. Either AI controlled of User controlled
            Player_mode 1 = User vs User
            Player_mode 2 = User vs AI
            Player_mode 3 = AI vs AI
        """

        if self.player_mode in [1,2]:
            player_1 = Player(1,"#f00")
            if self.player_mode == 1: player_2 = Player(2,"#000")
            else: player_2 = Ai(2,"#000",self.board,self)
        else:
            player_1 = Ai(1,"#f00",self.board,self)
            player_2 = Ai(2,"#000",self.board,self)
        self.player = player_1
        self.players = (player_1,player_2)

    def activate_space(self,x,y):
        """
            Onclick callback: assigns the bottom most space to active player.
            Arguements: (x{int},y{int}) = window coordinates for click position.
        """

        space = self.board.find_space(x,y)
        #find the space associated with the position given by onclick method
        if space and not space.state:
            space = self.board.space_empty(space)
            self.board.animate_drop(space)
            """ if space is valid... check if it is the bottommost empty
                space in column or return the bottom space and render
                dropping animation
            """

            space.draw(color=self.player.color)
            space.state = self.player.name
            """ fill bottommost empty space with players color
                set space state to filled by active player """

            if self.board.check_winner(space):
                # check if game over
                self.draw_message(f"GAME OVER {self.player} WINS")
                return

            # switch active players
            self.player = self.players[0] if self.players[0] != self.player else self.players[1]
            self.draw_message(str(self.player) + " Turn")
            self.player.turn()

        else:
            # if click is not in valid empty space player turn continues
            self.draw_message("Try Again")
            self.player.turn()


    def draw_message(self,msg):
        """ Write game state update messages to top of the window """
        self.pen.clear()
        self.pen.write(msg,align="center",font=self.font[0])
        return

    def play(self):
        self.onclick(self.activate_space)

    def game_board(self):
        """ Calculates and generates the board object. """
        board_height = (self.height//42)*42
        board_width = (board_height*7)/6
        bx = board_width/2
        by = board_height/2
        board_corners = [(-bx,by),(-bx,-by),(bx,-by),(bx,by)]
        self.board = Board(self,board_corners,board_width,board_height,bx,by)
        return


mode = {
    1: "Player vs Player",
    2: "Player vs AI",
    3: "AI vs AI"
}



if __name__ == "__main__":
    window = Window("#643",3)
    window.play()
    window.mainloop()
