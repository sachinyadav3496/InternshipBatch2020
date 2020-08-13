import tkinter as tk
from random import choice
root = tk.Tk()
time = 900
choices = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
def make_color():
    return "#"+ "".join( [ choice(choices) for var in range(6) ] )
label = tk.Label(root, text="Time Left : 900")
label.config(fg='#eeeeee', bg='#123456', height=5, width=20, font=("Courier", 30, 'bold'))
label.pack(side=tk.TOP, fill=tk.BOTH)

button = tk.Button(root, text='Exit', command=root.quit, font=30 )
button.pack(fill=tk.X, side=tk.BOTTOM)
button.config(bg='#eeeeee', fg='#123456')


button.bind("<Enter>", lambda e: button.config(fg="#123456", bg='#eeeeee'))
button.bind("<Leave>", lambda e: button.config(bg="#123456", fg='#eeeeee'))
label.bind("<Enter>", lambda e: label.config(fg="#123456", bg='#eeeeee'))
label.bind("<Leave>", lambda e: label.config(bg="#123456", fg='#eeeeee'))
root.title("Break")
def update_time():
    global time
    if time != 0:
        time -= 1
        label.config(text=f"Time Left: {time}", bg=make_color())
        root.after(1000, update_time)
    else:
        top = tk.Toplevel(root)
        lb = tk.Message(top, text="Time Out", font=30, fg='white', bg='#123456')
        lb.pack(fill=tk.BOTH)
        ebutton = tk.Button(top, text="Exit", font=30, fg="#123456", bg="white", command=top.quit)
        ebutton.pack()
        top.minsize(200, 200)
        top.grab_set()
root.after(1000, update_time)
root.minsize(200, 200)
root.mainloop()