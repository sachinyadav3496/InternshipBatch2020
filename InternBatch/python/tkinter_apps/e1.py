import tkinter as tk
import random
colors = [ 'red', 'green', 'yellow', 'blue', 'purple', 'magenta', 'cyan', 'orange']
def ent_enter(e):
    ent_var.set('')
    ent_box.config(bg='white', fg='gray')

def ent_leave(e):
    ent_box.config(bg='gray', fg='white')
    ent_var.set('write something')

def ent_process_data(e=None):
    print(e)
    text = ent_var.get()
    lb = tk.Label(root, text=text, fg=random.choice(colors), font=20)
    ent_var.set('')
    lb.pack()

root = tk.Tk()
ent_var =  tk.StringVar()
ent_var.set('write something')
ent_box = tk.Entry(root, font=('Times', 34, 'italic'),
                  bg='gray', fg='white', textvariable=ent_var)

ent_box.pack(fill='x')
ent_box.focus()

ent_box.bind('<Enter>', ent_enter)
ent_box.bind('<Leave>', ent_leave)
ent_box.bind('<Return>', ent_process_data)

ent_button = tk.Button(root, text='Click Me', font=('Times', 24, 'bold'), command=ent_process_data)
ent_button.pack()

root.wm_minsize(400, 400)
root.mainloop()
