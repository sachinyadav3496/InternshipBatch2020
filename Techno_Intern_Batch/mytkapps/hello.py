import tkinter as tk 
from random import choice
class MyApp:
    def __init__(self, master=None):
        self.count = 0
        self.master = master
        self.createwidgets(master)
        self.labels = []
        self.colors = [ 'red', 'green', 'yellow', 'gold', 'silver', 'magenta', 
                        'cyan', 'purple', 'blue', 'orange']
        self.master.minsize(400, 400)
        self.master.maxsize(800, 800)
    def createwidgets(self, master):
        self.create_frame(master)
        self.create_button(self.frame)
    def create_frame(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()
    def create_button(self, master):
        self.button = tk.Button(master, text="Say Hello!", relief=tk.GROOVE)
        self.button.config(font=("Courier", 25, 'bold'), height=2, width=30)
        self.button.config(command = lambda : self.create_label(self.frame))
        self.button.pack()
    def create_label(self, master):
        lb = tk.Label(master, text=f"Hello World! {self.count}")
        self.count += 1
        lb.config(font=("Courier", 20, 'bold'))
        fg = choice(self.colors)
        while True:
            bg = choice(self.colors)
            if fg != bg:
                break
        lb.config(fg=fg, bg=bg)
        lb.pack(fill=tk.X)
        self.labels.append(lb)

if __name__ == "__main__":

    app = MyApp(tk.Tk())
    app.master.mainloop()