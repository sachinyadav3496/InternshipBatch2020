import tkinter as tk 


root = tk.Tk()

label = tk.Label(root, text='!!Hello World!!')
label.config(fg='#eeeeee', bg='#333333', font=("Courier", 25, "bold"), height=5, width=20)

def enter(e):
    label.config(bg='#eeeeee', fg='#333333', font=("Times", 30), height=5, width=20)

def leave(e):
    label.config(fg='#eeeeee', bg='#333333', font=("Courier", 25, "bold"), height=5, width=20)

label.bind("<Enter>", enter)
label.bind("<Leave>", leave)


label.pack(fill=tk.BOTH, padx=50, pady=50)
root.minsize(400, 400)
root.mainloop()