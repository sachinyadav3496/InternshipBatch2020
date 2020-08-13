import tkinter as tk

root = tk.Tk()

def print_hello(name):
    print("hello world", name, flush=True)

b = tk.Button(root, text="Click Me", command=lambda name='Sachin yadav': print_hello(name))
#                                            None                                     
b.pack() 
    

root.mainloop()
