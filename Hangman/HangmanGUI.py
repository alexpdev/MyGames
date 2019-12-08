# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:46:11 2018
@author: ASP
This is a very simple Hangman game with QtGUI
python 3.7 and PyQt5
"""

from PyQt5 import QtWidgets
import sys

#main window
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    #Main Window Build
    def __init_ui(self):
        self.glabel = QtWidgets.QLabel("Letters Guessed Already")
        self.clabel = QtWidgets.QLabel("Current Status")
        self.label = QtWidgets.QLabel("Type Next Guess Here, Single Letter Only")
        self.btn3 = QtWidgets.QPushButton("Guess")
        self.btn3.setMaximumWidth(100)
        self.btn1 = QtWidgets.QPushButton("New Game")
        self.btn1.setMaximumWidth(100)
        self.txtman = QtWidgets.QTextBrowser()
        self.txtman.setFontPointSize(10.0)
        self.txtman.setMinimumWidth(300)
        self.txtg = QtWidgets.QTextBrowser()
        self.txtc = QtWidgets.QTextBrowser()
        self.nextguess = QtWidgets.QLineEdit()
        self.setGeometry(60,60,580,480)

        # Set main window Layout
        vert = QtWidgets.QGridLayout()
        self.setLayout(vert)
        vert.addWidget(self.glabel, 0, 0)
        vert.addWidget(self.txtg, 1, 0)
        vert.addWidget(self.clabel, 2, 0)
        vert.addWidget(self.txtc, 3, 0)
        vert.addWidget(self.label, 4, 0)
        vert.addWidget(self.nextguess, 5, 0)
        vert.addWidget(self.btn3, 6, 0)
        vert.addWidget(self.btn1, 6, 1)
        vert.addWidget(self.txtman, 0, 1, 6, 1)
        vert.setRowStretch(3, 1)
        vert.setRowStretch(4,2)
        vert.setRowStretch(2,2)
        vert.setRowStretch(0,2)
        vert.setRowStretch(1,1)
        vert.setRowStretch(5,1)
        vert.setRowStretch(6,1)

        # User triggered events
        self.btn1.clicked.connect(self.btn1_click)
        self.btn3.clicked.connect(self.btn3_click)
        self.show()

        # Class Instance Variables
        self.count = 0
        self.wrongcount = 0
        self.array = []
        self.answer = ''
        self.wronglst = []

    #Instance Action Driven Functions
    # Press the "guess" button ...
    # Must be 1 single alpha character in the line edit box above otherwise error
    def btn3_click(self):
        self.count += 1
        self.nextguess.selectAll()
        guess = self.nextguess.selectedText()
        if len(guess) > 1:
            self.txtman.setText("Too many letters try again")
        elif guess.isalpha() == False:
            self.txtman.setText("Must be a single letter")

        # If the input meets requirements....
        else:
            if guess.lower() in self.answer.lower():  # if input is in the init string
                guesscount = self.answer.count(guess.lower())
                idx = self.answer.index(guess.lower())
                self.array[idx] = guess   # Add Character to string of correct guesses at the correct index

                # checks if character count is more than 1 and makes adjustments if necessary
                if guesscount > 1:
                    while guesscount > 1:
                        guesscount -= 1
                        idx2 = self.answer.index(guess.lower(), idx+1)
                        self.array[idx2] = guess
                        idx = idx2
                self.txtc.setText(''.join(self.array))

           # if the input does not appear anywhere within the answer string...
            else:
                self.wronglst.append(guess)   # add char to wrongguess list for output to screen
                self.txtg.setText(' '.join(self.wronglst))
                self.wrongcount += 1
                self.txtman.setText(plist[self.wrongcount])
        if ''.join(self.array).lower() == self.answer:
            self.txtman.setText("you win")
            # output text string representation of a hangman with a new part added for bad each guess

    # New Game Button... Grabs the input string and stores it as Answer then displays the start game text and waits for Guess button
    def btn1_click(self):
        self.txtman.setText(p1)
        self.nextguess.selectAll()
        answer = self.nextguess.selectedText()
        self.nextguess.clear()
        print(answer)
        blanks = [" __ " for i in answer]
        self.array = blanks
        blanks2 = ''.join(blanks)
        self.answer = answer.lower()
        self.txtc.setText(blanks2)

# Init Window Script
def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Window()
    sys.exit(app.exec_())



p1 = """                                              \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""

p2 = """                                              \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p3 = """                                              \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
             |                         |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p4 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
           --|                         |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p5 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
           --|--                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""


p6 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""

p7 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""

p8 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
             |                         |              \n
                                       |              \n
                                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p9 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
             |                         |              \n
            /                          |              \n
           /                           |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""

p10 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
             |                         |              \n
            /\                         |              \n
           /  \                        |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p11 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
             |                         |              \n
            /\                         |              \n
          _/  \                        |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
p12 = """                                               \n
             |-------------------------|              \n
             |                         |              \n
             |                         |              \n
             |                         |              \n
            )@(                        |              \n
          o--|--o                      |              \n
             |                         |              \n
            /\                         |              \n
          _/  \_                       |              \n
                                       |              \n
                                       |              \n
------------------------------------------------------"""
plist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
main()