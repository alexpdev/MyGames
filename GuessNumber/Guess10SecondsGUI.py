"""UTF_8 Encoding: Python 3.5 and PyQt5"""
"""written by asp 2018 May 13"""


from PyQt5 import QtWidgets
import random
from datetime import datetime, timedelta
import sys

# input()
# a = datetime.now()
# input()
# b = datetime.now()
# c = b - a
# print(c.seconds())

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._initui()

    def _initui(self):
        self.setGeometry(200,200,273,130)
        self.Btn = QtWidgets.QPushButton()
        self.ftime = QtWidgets.QLabel()
        self.ftime2 = QtWidgets.QLabel()
        self.Btn.setText("Start/Stop")
        self.label = QtWidgets.QLabel("Press the Button To Start Clock then Press again after you believe exactly 10 seconds have passed.")
        Box = QtWidgets.QGridLayout()
        self.label.setWordWrap(True)
        self.setLayout(Box)
        Box.addWidget(self.Btn,4,0)
        Box.addWidget(self.ftime,1,0)
        Box.addWidget(self.ftime2,3,0)
        Box.addWidget(self.label,0,0)
        self.count = 0
        self.first = datetime.now()
        self.stop = datetime.now()


        self.Btn.clicked.connect(self.BtnClick)
        self.show()


    def BtnClick(self):
        now = datetime.now()
        self.count += 1
        if self.count == 1:
            self.first = now
            self.ftime.setText(repr(datetime.now()))
        elif self.count == 2:
            self.stop = now
            finaltime = self.stop - self.first
            comp = ['hours', 'minutes', 'seconds']
            res = str(finaltime).split(':')
            if res[0] == '0' and res[1] == '00':
                final = comp[2] + ": " + res[2]
            else:
                final = ' '.join([comp[i] + ': ' + res[i] for i in range(len(res))])
            self.ftime.setText(str(self.stop) + '-' + str(self.first))
            self.ftime2.setText(final)
            self.count = 0







def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Window()
    sys.exit(app.exec_())

main()
