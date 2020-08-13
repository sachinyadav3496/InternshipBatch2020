import tkinter as tk 
from random import choice 
current_color = None
choices = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def make_color():
    global current_color
    while True:
        color = "#"+"".join( [ choice(choices) for _ in range(6)] )
        if color != current_color:
            current_color = color
            break
    return color 
c = 0
def create_label():
    global c
    lb = tk.Label(frame)
    lb.config(text=f"Hello World Times: {c}", fg=make_color(), bg=make_color())
    lb.config(font=("Courier", 20, "bold"))
    c += 1
    lb.pack(fill=tk.X, pady=10, padx=20)
root = tk.Tk()
frame = tk.Canvas(root)
for var in range(5):
    create_label()
sc = tk.Scrollbar(frame, command=frame.yview, orient='vertical')
frame.config(yscrollcommand=sc.set)



button = tk.Button(frame, text="Say Hello!", fg='#eeeeee', bg='#333333', relief=tk.RAISED)
button.config(height=1, width=30, command=create_label, 
                font=("Courier", 20, "bold"), bd=2)
button.config(padx=20, pady=20)
button.pack(fill=tk.X)

sc.pack(side=tk.RIGHT, fill=tk.Y)

frame.pack()
root.minsize(400, 400)
root.maxsize(800, 800)
root.mainloop()