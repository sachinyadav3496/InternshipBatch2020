from tkinter import * 

root = Tk()

var1 = IntVar()
var2 = IntVar()
chk1 = Checkbutton(root, text="Male", variable=var1)
chk1.pack()

chk2 = Checkbutton(root, text="Female", variable=var2)
chk2.pack()

b= Button(root, text='result', font=20, command=lambda: print(var1.get(), var2.get()))
b.pack()

root.mainloop()