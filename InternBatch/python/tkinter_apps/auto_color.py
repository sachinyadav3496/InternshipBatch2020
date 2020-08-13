import tkinter as tk
from random import choice
colors = [ 'red', 'green', 'purple', 'cyan', 'magenta', 'blue', 'orange', 'gold', 'gray', 'black']
i = 0
choices = [ hex(var)[2:] for var in range(16)]
root = tk.Tk() 
# creating a root window
label = tk.Message(root, text="Wait for 5 seconds .... ")
label.config(font=("Times", 25, 'bold'), )#height=3, width=10)
label.pack(padx=20, pady=20, fill=tk.BOTH, expand=tk.YES)

with open("auto_color.py") as fp:
    text = fp.read()
def start():
    color = "#"+ "".join(choice(choices) for _ in range(6))
    fg = color[0]+color[:0:-1]
    label.config(fg=fg, bg=color, text=text)
    root.after(2000, start)

root.title("Change Color App")
root.iconbitmap("images/main.ico")
root.minsize(400, 400)

root.after(5000, start)
# run start function after x miliseconds
root.mainloop()