import tkinter as tk

root = tk.Tk()

# rows = 4
# cols = 3
# entry, buttons 
e_var = tk.StringVar()
entry = tk.Entry(root, textvariable=e_var)
entry.config(
    font=("Courier", 30, 'bold'), bg='#123456', fg='white'
)

entry.grid(row=0, column=0, columnspan=3)
buttons = []
c = 1
for row in range(1, 4): # 1, 2, 3
    for col in range(3): # 0, 1, 2
        # row - 1, col - 0
        value = str(c)
        b = tk.Button(root, text= str(c),
        command=lambda value = value:e_var.set(e_var.get()+value) )
        b.config(bg='#eeeeee', fg='#123456', 
            font=("Times", 25, 'bold'), width=6 ,height=2,
            relief=tk.RAISED, bd=3)
        b.grid(row=row, column=col, padx=5, pady=5)
        c += 1
        buttons.append(b)
clr = tk.Button(root, text="CLR", bg='red', fg='white', font=20)
clr.grid(row=0, column=3)
clr.config(command=lambda :e_var.set(''), width=6, height=2,
relief=tk.RAISED, bd=3)
root.iconbitmap('images/main.ico')
root.title("Pre-Calculator")
root.minsize(400, 400)
root.mainloop()