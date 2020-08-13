from tkinter import * 
from tkinter.messagebox import showinfo, showwarning, askyesnocancel

root = Tk() 

lb = Label(root, text="Hello World", font=50)
lb.pack(fill=BOTH, expand=YES)

def some_ask():
    ans = askyesnocancel(title="Continue", message="do you want to close it  ? ")
    if ans:
        root.quit()
def some_func():
    showinfo(title="Information", message="See I am Giving you Some Instructions")

def some_error():
    showwarning(title="Error", message="You have done this wrong")

b = Button(root, text="INFO", command = some_func, font=("Courier", 20, 'bold'), bg='#333333',
fg='#eeeeee')
b.pack(side=BOTTOM, fill=X, expand=YES)

b1 = Button(root, text="Error", command = some_error, font=("Courier", 20, 'bold'), bg='#333333',
fg='#eeeeee')
b1.pack(side=BOTTOM, fill=X, expand=YES)

b2 = Button(root, text="ASKYESNO", command = some_ask, font=("Courier", 20, 'bold'), bg='#333333',
fg='#eeeeee')
b2.pack(side=BOTTOM, fill=X, expand=YES)

root.mainloop()