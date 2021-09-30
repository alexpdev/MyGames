import os,sys
from pathlib import Path
sys.path.append(os.path.dirname(Path(__file__).resolve()))
from connect4.window import Window





if __name__ == "__main__":
    window = Window("#643",3)
    window.play()
    window.mainloop()

