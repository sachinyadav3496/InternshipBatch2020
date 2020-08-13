import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)

canvas.config(bg='#333333',)
canvas.pack(pady=30, padx=30)
s = 10
for var in range(20):
    x1,y1 = (20, s+30) # 20,20, 30, 20
    x2, y2 = (380, s+30)
    s = s + 30
    canvas.create_line(x1, y1, x2, y2, fill='white')
s = 10
for var in range(20):
    x1, y1  = (s+30, 20)
    x2, y2  = (s+30, 380)
    s += 30
    canvas.create_line(x1, y1, x2, y2, fill='#cccccc')

root.minsize(500, 500)
root.mainloop()