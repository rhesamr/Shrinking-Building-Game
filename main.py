# main.py code for the Shrinking Building Game
from tkinter import *
import bg,brick,building,random
import time

# initialise global variables
bg_width = 400 #the background size width
bg_height = 600 #the background size height

#skyblue, green, red
colour_index = ["#243436", "#2b3f41", "#33494c", "#3a5457", "#415e62", "#49696d", "#507378",
                "#577e83", "#5e888e", "#669399", "#6d9da4", "#74a8af", "#7cb2ba", "#83bdc5", 
                "#8ac7d0", "#97d4dc", "#9cd6de", "#a2d8e0", "#a7dbe2", "#addde4", "#b2dfe5",
                "#b8e1e7", "#bde4e9", "#c3e6eb", "#c8e8ed", "#cdeaee", "#d3edf0", "#d8eff2", 
                "#def1f4", "#e3f3f6"], ["#082208", "#0a290a", "#0b300b", "#0d370d", "#0f3e0f", "#114511", "#124c12",
                 "#145314", "#165a16", "#176117", "#196819", "#1b6f1b", "#1c761c", "#1e7d1e",
                 "#208420", "#2d902d", "#389638", "#439c43", "#4ea24e", "#59a859", "#64ad64",
                 "#6fb36f", "#7ab97a", "#85bf85", "#90c590", "#9bca9b", "#a6d0a6", "#b1d6b1",
                 "#bcdcbc", "#c7e2c7"], ["#3f0000", "#4c0000", "#590000", "#660000", "#720000", "#7f0000", "#8c0000",
                  "#990000", "#a50000", "#b20000", "#bf0000", "#cc0000", "#d80000", "#e50000",
                  "#f20000", "#ff0c0c", "#ff1919", "#ff2626", "#ff3333", "#ff3f3f", "#ff4c4c",
                  "#ff5959", "#ff6666", "#ff7272", "#ff7f7f", "#ff8c8c", "#ff9999", "#ffa5a5",
                  "#ffb2b2", "#ffbfbf"]
                 

velocity = 10 #the brick speed
score = 10 #initial score (building height)
universalwidth = 170 #the initial width for the 
entry_pos = -universalwidth #entry_pos means initial pixel for the brick to come. 0= from left, 600=from right
move_pos = True #move_pos=True for brick coming from left, else right
stack_count = 0 #stack counter for velocity
i = random.randint(0,2) #color chooser
j = 0


# order a window from the tkinter factory
window = Tk()
window.title("Shrinking Building v1.5")

# order a bg from the bg factory
my_bg = bg.Bg(window, width=bg_width, height=bg_height, colour = "#fcedf3")

# order a brick from the brick factory
my_brick = brick.Brick(bg= my_bg, speed=velocity, width=universalwidth, height=15, colour=colour_index[i][j], x_start=entry_pos, y_start=188)

# order a building from the building factory
my_building = building.Building (bg= my_bg, width=universalwidth, height=400, x_posn=((bg_width/2)-(universalwidth/2)), y_posn=203, colour=colour_index[i][j])



#### functions:                        
# basic game flow
def game_flow():
    global universalwidth
    global score

    if (universalwidth == 0):
        my_bg.erase_score()
        my_bg.draw_endgame(score)
        my_brick.erase_brick()
        my_building.erase_building()
        window.after(50, game_flow)
        window.bind("r", restart_game)
    else:
        my_brick.move_brick()
        my_bg.draw_score(score)
        window.after(50, game_flow)
    
    
# restart_game function
def restart_game(master):
    global universalwidth
    global score
    global move_pos
    global velocity
    global stack_count
    global my_brick
    global my_building
    global i, j

    my_bg.erase_endgame()
    my_brick.erase_brick()
    my_building.erase_building()

    #initial values as defined in the initial global variables
    velocity = 10
    i = random.randint(0,2)
    j = 0
    stack_count = 0
    universalwidth = 170
    entry_pos = -universalwidth
    move_pos = True
    score = 10

    # reorder a brick from the brick factory
    my_brick = brick.Brick(bg=my_bg, speed=velocity, width=universalwidth, height=15, colour=colour_index[i][j], x_start=entry_pos, y_start=188)

    # reorder a building from the building factory
    my_building = building.Building(bg=my_bg, width=universalwidth, height=400, x_posn=((bg_width/2)-(universalwidth/2)), y_posn=203, colour=colour_index[i][j])

    
# stacking bricks
def put_brick(master):
    global universalwidth
    global score
    global move_pos
    global velocity
    global stack_count
    global my_brick
    global my_building
    global i, j
   

    #colour change
    if j == 29:
        j = 0
    else:
        j = j + 1
    
        
    # building zones
    left = my_building.x_posn
    right = my_building.x_posn + my_building.width
    h_centre = left + (my_building.width/2)

    # brick zones
    left_b = my_brick.x_posn
    right_b = my_brick.x_posn + my_brick.width
    r = (right_b - left_b)/2

    # brick stacking logic / score
    if (left_b<left and right_b<left):
        universalwidth = 0
        my_bg.erase_double_score()
    elif (left_b>left-3 and left_b<left+3):
        universalwidth = universalwidth
        score = score + 2
        my_bg.draw_double_score()
        stack_count = stack_count + 2
    elif (left_b<left and right_b>left and right_b<right):
        universalwidth = right_b-left
        score = score + 1
        stack_count = stack_count + 1
        my_bg.erase_double_score()

        
    elif (left_b>left and left_b<right and right_b>right):
        universalwidth = right-left_b
        score = score + 1
        stack_count = stack_count + 1
        my_bg.erase_double_score()
        
    elif (left_b>right and right_b>right):
        universalwidth = 0
        my_bg.erase_double_score()

    # deleting the last brick and building
    my_brick.erase_brick()
    my_building.erase_building()

    # speedup the brick speed every 5 stacked bricks
    if (stack_count==5):
        velocity += 1
        stack_count = 0 

    # deciding where to start
    if (move_pos==True):
        entry_pos = universalwidth+bg_width
        move_pos = False
    else:
        entry_pos = -universalwidth
        move_pos = True
    
    # reorder a brick from the brick factory
    my_brick = brick.Brick(bg=my_bg, speed=velocity, width=universalwidth, height=15, colour=colour_index[i][j], x_start=entry_pos, y_start=188)

    # order a building from the building factory
    my_building = building.Building(bg=my_bg, width=universalwidth, height=400, x_posn=((bg_width/2)-(universalwidth/2)), y_posn=203, colour=colour_index[i][j])

# call the game_flow loop
game_flow()

# control binding

window.bind("<space>", put_brick)
 
# start the animation loop
window.mainloop()

#HWAPPY