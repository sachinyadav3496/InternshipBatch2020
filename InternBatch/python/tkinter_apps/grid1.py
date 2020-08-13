import tkinter as tk
from random import choice

root = tk.Tk()

def change():    
    color = "#" + "".join( [choice([hex(var)[2:] for var in range(16)]) for _ in range(6)])
    root.config(bg=color)
change_color = tk.Button(root, text='change_color', height=3, font=20, width=20)
change_color.config(command=change)

exit_button = tk.Button(root, text='exit', height=3, font=15, width=25,
command=root.quit)

change_color.grid(row=0, column=0, columnspan=2)
exit_button.grid(row=0, column=2, columnspan=3 )

root.minsize(400, 400)
root.mainloop()