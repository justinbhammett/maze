from tkinter import Tk, BOTH, Canvas
from maze import *

class Window:
        def __init__(self, width, height):
                self.width = width
                self.height = height
                self.__root = Tk()
                self.__root.geometry(str(width)+"x"+str(height))
                self.__root.title("Maze Solver")
                self.__canvas = Canvas(self.__root, bg="black", height=self.height, width=self.width)
                self.__canvas.pack(fill=BOTH, expand=1)
                self.__running = False
                self.__root.protocol("WM_DELETE_WINDOW", self.close)


        def redraw(self):
                self.__root.update_idletasks()
                self.__root.update()
        
        def draw_line(self, line, fill_color="white"):
                line.draw(self.__canvas, fill_color)
        
        def wait_for_close(self):
                self.__running = True
                while self.__running:
                        self.redraw()
                print("Window closed.")



        def close(self):
                self.__running = False

