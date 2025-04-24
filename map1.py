# a simple program to draw a grid of rooms without connections
# the title of the window is the number of rooms

import tkinter as tk
import json

# Load room data uncomment as required
#datafile = "star_wars.json"
#datafile = "game_data.json"
#datafile = "game_data.json3"


with open(datafile) as f:
    data = json.load(f)

rooms = data["rooms"]

root = tk.Tk()
root.title(str(len(rooms)) + " Rooms")

# width and height of window
w = 1200
h = 800

canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()

#draw the room - a blue box
# the colour default is lightblue
def draw_room( name, x, y, colour="lightblue"):
    canvas.create_rectangle(x, y, x+stepx, y+stepy, fill=colour)
    canvas.create_text(x+50, y+25, text=name, font=("Arial", 8), justify="center")   


# Place rooms in a grid-like layout
startx = 50
starty = 50

x, y = startx, starty
stepx = 100
stepy = 50

for i, name in enumerate(rooms):
    draw_room(name, x,y,colour="lightblue")
    x += (stepx * 1.1)
    if x >= w - 100:
        x = startx
        y += stepy * 2

root.mainloop()
