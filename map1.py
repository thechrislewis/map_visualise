import tkinter as tk
import json

# Load room data
with open("game_data.json") as f:
    data = json.load(f)

rooms = data["rooms"]

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Place rooms in a grid-like layout
x, y = 100, 100
for i, name in enumerate(rooms):
    canvas.create_rectangle(x, y, x+100, y+50, fill="lightblue")
    canvas.create_text(x+50, y+25, text=name)
    x += 150
    if x > 600:
        x = 100
        y += 100

root.mainloop()
