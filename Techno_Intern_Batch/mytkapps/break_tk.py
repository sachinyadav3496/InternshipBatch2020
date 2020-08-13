import tkinter as tk 
from random import choice
time = 900
lb_text = f"Time Left: {time}"
root = tk.Tk() 
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
text = tk.Label(root, text=lb_text)
text.config(font=("Times", 25, "bold"), width=30, fg='#eeeeee', bg='#123456',
height=5, )
text.pack(fill=tk.BOTH)

def update():
    global time, lb_text
    time -= 1
    lb_text = f"Time Left: {time}"
    text.config(text=lb_text, bg=make_color())
    if time == 0:
        top = tk.Toplevel(root)
        lb = tk.Label(top, text="Timeout", font=("Times", 30, 'bold'), fg='red')
        lb.pack()
        top.grab_set()
        time = 20
        top.configure(height=200, width=200)

    else:
        root.after(1000, update)


button = tk.Button(root, text='Exit', command=root.quit) #, bitmap='question')
button.config(font=("Times", 25, "bold"), height=3, width=30, bg='#eeeeee', fg='#123456', )
button.pack(fill=tk.BOTH)


root.minsize(400, 400)
root.after(1000, update)
# root.after(milisecond, func)
root.mainloop()