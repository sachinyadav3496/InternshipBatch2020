import tkinter as tk 


root = tk.Tk()
canvas = tk.Canvas(root, bg='#333333', height=500, width=500)

canvas.pack(padx=30, pady=30)

for x in range(50, 500, 50):
    canvas.create_line(x, 0, x, 500, fill='white', width=3)

for y in range(50, 500, 50):
    canvas.create_line(0, y, 500, y, fill='white', width=3)
root.mainloop()