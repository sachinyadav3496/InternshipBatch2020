import tkinter as tk 

root = tk.Tk()

cn = tk.Canvas(root, height=400, width=400)

cn.create_rectangle(100, 100, 300, 300, fill='red')
v = [ 200, 100, 200, 300]
h = [ 100, 200, 300, 200]
cn.create_line(*v, fill='white', width=5)
cn.create_line(*h, fill='white', width=5)
cn.create_oval(50, 50, 100, 100, fill='blue')
cn.create_line(50,50, 100, 100, width=3, fill='white')
cn.create_line(50,75,100, 75,  width=3, fill='white')
cn.pack()
root.mainloop()

cn.create_oval()


