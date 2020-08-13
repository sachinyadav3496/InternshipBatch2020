import tkinter as tk 


root = tk.Tk()

label = tk.Label(root, text="Hello World")

label.pack()

def change():
    label.config(text="Ohh I am Changed")
label.after(5000, change)

root.mainloop()