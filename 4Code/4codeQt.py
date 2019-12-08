# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:46:11 2018
@author: ASP
This is a very simple Hangman game with QtGUI
python 3.7 and PyQt5
"""

from PyQt5 import QtWidgets
import random
import sys


# main
class FourCode(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self._initGUI()
    # Main Window Structure with PyQt5
    def _initGUI(self):
        self.setGeometry(516,257,60,60)
        self.btn1 = QtWidgets.QPushButton("Guess")
        self.btn2 = QtWidgets.QPushButton("New Game")
        self.lbl5 = QtWidgets.QLabel("")
        self.lbl6 = QtWidgets.QLabel("")
        self.lbl1 = QtWidgets.QLabel("4-digit Pin")
        self.lbl2 = QtWidgets.QLabel("Your guess goes here.")
        self.lbl3 = QtWidgets.QLabel("Right Number, Wrong Spot.")
        self.lbl4 = QtWidgets.QLabel("Right Number, Right Spot.")
        self.edit = QtWidgets.QLineEdit()


        g = QtWidgets.QGridLayout()
        self.setLayout(g)
        g.addWidget(self.edit,4,1)
        g.addWidget(self.btn1,5,1)
        g.addWidget(self.btn2,5,0)
        g.addWidget(self.lbl1,0,0,1,1)
        g.addWidget(self.lbl2,4,0)
        g.addWidget(self.lbl3,2,0)
        g.addWidget(self.lbl4,3,0)
        g.addWidget(self.lbl5,2,1)
        g.addWidget(self.lbl6,3,1)
        g.setRowStretch(0,0)
        g.setRowStretch(1,0)
        g.setRowStretch(2,0)
        g.setRowStretch(3,0)
        g.setRowStretch(4,0)
        g.setRowStretch(5,0)



        self.count = 0
        self.guess = 0
        self.code = []
        self.corlocal = []
        self.incorlocal = []

        self.btn2.clicked.connect(self.ngBtn)
        self.btn1.clicked.connect(self.guesBtn)
        self.show()

    #function for New Game Button click event
    def ngBtn(self):
        self.code = [random.randint(0,9) for i in range(4)] #create random code
        self.corlocal = ["_" for i in range(4)]
        self.lbl6.setText(repr(self.corlocal))
        self.incorlocal = []    #set labels to echo new game
        self.lbl5.setText(repr(self.incorlocal))

    #function for guess button click event
    def guesBtn(self):
        self.count += 1 #counter for # of tries (todo)
        self.edit.selectAll()
        guess = self.edit.selectedText()
        lst = [int(i) for i in str(guess)]  #select input text and format
        for i, x in enumerate(lst):
            if x in self.code:
                if self.code[i] == x:       #iterate through guess for correct nums
                    self.corlocal[i] = x
                    self.lbl6.setText(str(self.corlocal))
                else:
                    if x not in self.incorlocal:
                        self.incorlocal.append(x)   #notify user if nums in wrong index
                        self.lbl5.setText(str(self.incorlocal))

        # Congratulations to winner
        if self.corlocal == self.code and len(self.code) == 4:
            self.lbl1.setText("Well good golly gosh god darn you won!")
            self.lbl3.setText("Winner!")
            self.lbl5.setText("Winner!")
            self.lbl4.setText("Chicken")
            self.lbl6.setText("Dinner")
            self.lbl2.setText("HOLY CRAP YOU'RE GOOD")






def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = FourCode()
    sys.exit(app.exec_())

main()
