#bg.py code for the Shrinking Building Game

from tkinter import *

class Bg:
    #### constructor
    def __init__(self, window, width=200, height=600, colour = "light green"):

        self.width = width
        self.height = height
        self.colour = colour
        
        
        # order a canvas to draw on from the tkinter factory:
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()
        self.font = ("Arial", 25)
        self.double_font = ("italic large Palatino", 20)
        self.scoreboard = self.canvas.create_text(200, 50, font=self.font, fill="darkgreen",justify='center')
        self.endgame = self.canvas.create_text(200, 150, font=self.font, fill="darkgreen",justify='center')
        self.restart = self.canvas.create_text(200, 300, font=self.font, fill="darkgreen",justify='center')
        self.double = self.canvas.create_text(350, 120, font=self.font, fill="red")
        
    ## extra tool for adding a rectangle to the canvas
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.colour
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c, outline="")

    # extra tools for manipulating items on the canvas:
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
            
    def remove_item(self, item):
        self.canvas.delete(item)
    
    def change_item_colour(self, item, c):
        self.canvas.itemconfigure(item, fill=c)

    def draw_score(self, scr):
        scores = "Building Height:\n" + str(scr) + "m"
        self.canvas.itemconfigure(self.scoreboard, text=scores)
        self.canvas.update

    def draw_endgame(self,scr):
        endgame = "YOU LOST!\n\nYour Building Height:\n" + str(scr) + "m"
        self.canvas.itemconfigure(self.endgame, text=endgame)
        restart = "Press the R Button\nto Restart!"
        self.canvas.itemconfigure(self.restart, text=restart)
        self.canvas.update
        
    def draw_double_score(self):
        self.canvas.itemconfigure(self.double, text=f"double!!")
                
    def erase_double_score(self):
        self.canvas.itemconfigure(self.double, text="")
        
        
    def erase_endgame(self):
        self.canvas.itemconfigure(self.endgame, text="")
        self.canvas.itemconfigure(self.restart, text="")

    def erase_score(self):
        self.canvas.itemconfigure(self.scoreboard, text="")