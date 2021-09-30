import os,sys
from unittest import TestCase
from pathlib import Path
import turtle
sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
from connect4.board import Window

class WindowTest(TestCase):

    def test_window_with_args(self):
        color,mode = "#FFF",1
        win = Window(color=color,mode=mode)
        self.assertTrue(win)
        self.assertEqual(win.height/2,win.y)
        self.assertGreater(win.width,win.x)
        self.assertEqual(win.player_mode,mode)
        self.assertTrue(win.board)
        win.bye()
        del win

    def test_window_without_args(self):
        self.assertRaises(turtle.Terminator,Window)
        # win2 = Window()
        # self.assertTrue(win2)
        # self.assertEqual(win2.height/2,win2.y)
        # self.assertGreater(win2.width,win2.x)
        # self.assertTrue(win2.player_mode)
        # self.assertTrue(win2.board)
        # self.assertEqual(len(win2.players), 2)



