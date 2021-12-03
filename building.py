#building.py code for the Shrinking Building game


class Building:
    ####construktor
    def __init__ ( self, bg, width=15, height=100,
                    x_posn=50, y_posn=50, colour="black", i = 0):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn

        self.x_start = x_posn
        self.y_start = y_posn 
        self.bg = bg
        self.colour = colour
        self.rectangle = self.bg.draw_rectangle(self)
        
        
    def erase_building(self):
        self.bg.remove_item(self.rectangle)    

    ####methods
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def hide_building(self):
        self.bg.change_item_colour(self.rectangle, "#fcedf3")
        
    def show_building(self):
        self.bg.change_item_colour(self.rectangle, self.colour)
        

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def hide_building(self):
        self.bg.change_item_colour(self.rectangle, "#fcedf3")
        
    def show_building(self):
        self.bg.change_item_colour(self.rectangle, self.colour)
        