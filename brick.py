#brick.py code for the Shrinking Building Game

class Brick:
    ####construktor
    def __init__(self, bg, width=14, height=14, colour="pink",
                  speed=6, x_start=0, y_start=0, show = 1):
        #the brick won't move on the x axis
        #we still need x_posn and y_posn to determine the brick location
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.colour = colour
        self.x_start = x_start
        self.y_start = y_start
        self.speed = speed
        self.bg = bg
        self.show = show
        self.rectangle = self.bg.draw_rectangle(self)

    #### methods
    ## startting position of the brick
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def start_brick(self, speed):
        self.speed = speed
        self.start_position()

    def move_brick(self):
        self.x_posn = self.x_posn + self.speed
        # if the ball hits the left wall:
        if(self.x_posn <= -self.width):
            self.x_posn = -self.width
            self.speed = -self.speed
        # if it hits right wall:
        if(self.x_posn >= (self.bg.width - 0)):
            self.x_posn = (self.bg.width - 0)
            self.speed = -self.speed
        # finally move the circle:
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.bg.move_item(self.rectangle, x1, y1, x2, y2)

    def stop_brick(self):
        self.speed = 0

    def erase_brick(self):
        self.bg.remove_item(self.rectangle)
