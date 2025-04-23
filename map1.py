import tkinter as tk
import json

# Load room data
with open("game_data.json3") as f:
    data = json.load(f)

rooms = data["rooms"]

root = tk.Tk()
canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.pack()

# Place rooms in a grid-like layout
startx = 50
starty = 50

x, y = startx, starty
stepx = 100
stepy = 50
for i, name in enumerate(rooms):
    canvas.create_rectangle(x, y, x+stepx, y+stepy, fill="lightblue")
    canvas.create_text(x+50, y+25, text=name)
    x += 150
    if x > 800:
        x = startx
        y += 100

root.mainloop()
