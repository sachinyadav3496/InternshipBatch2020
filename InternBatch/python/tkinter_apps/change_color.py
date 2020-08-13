import tkinter as tk
from random import choice
colors = [ 'red', 'green', 'purple', 'cyan', 'magenta', 'blue', 'orange', 'gold', 'gray', 'black']
i = 0
choices = [ hex(var)[2:] for var in range(16)]
root = tk.Tk() 
# creating a root window
label = tk.Label(root, text="Press Enter to Start")
label.config(font=("Times", 25, 'bold'), height=3, width=10)
label.pack(padx=20, pady=20, fill=tk.BOTH, expand=tk.YES)

def start(event):
    color = "#"+ "".join(choice(choices) for _ in range(6))
    text = f"I am Color: {color}"
    label.config(fg='#eeeeee', bg=color, text=text)

"""def start(event):
    global i
    if i < len(colors):
        color = colors[i]
        i += 1
        text = f"I am Color: {color}"
        label.config(fg='#eeeeee', bg=color, text=text)
    else:
        i = 0
"""
root.bind("<Return>", start)
# Button-1 means left click
# on press enter do this task called start
root.title("Change Color App")
root.iconbitmap("images/main.ico")
root.minsize(400, 400)
root.mainloop()