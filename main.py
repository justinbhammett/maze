from window import Window
from maze import *


def main():
    win = Window(800,800)
    l = Line(Point(400,400), Point(0,400))
    win.draw_line(l)
    win.wait_for_close()
    
main()