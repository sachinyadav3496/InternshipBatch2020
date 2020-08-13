import tkinter as tk 


root = tk.Tk()
canvas = tk.Canvas(root, bg='#333333', height=500, width=500)

canvas.pack(padx=30, pady=30)
flag = False 

def draw():
    global flag
    if flag:
        canvas.create_rectangle(50, 50, 250, 250, fill='#cccccc', width=3)
    else:
        canvas.create_oval(300, 50, 450, 250, fill='red', width=3)
        flag = True 
        canvas.after(3000, draw)
canvas.after(3000, draw)
root.mainloop()