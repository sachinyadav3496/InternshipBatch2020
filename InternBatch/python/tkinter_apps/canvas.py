import tkinter as tk 

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)

canvas.create_line(0,0, 500, 500 ,fill='white', width=3)

canvas.create_line(0, 500, 500, 0, fill='white', width=3)

canvas.configure(bg="#333333")
canvas.pack(fill=tk.BOTH, expand=tk.YES,  padx=30, pady=30)

root.mainloop()