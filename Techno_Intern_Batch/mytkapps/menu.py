import tkinter as tk

root = tk.Tk() 

menu = tk.Menubutton(root, text="Menu")
menu.pack(anchor=tk.NW, expand=tk.YES)

options = tk.Menu(menu, tearoff=True)

options.add_command(label="Hello", command=lambda: print("hello World"))
options.add_command(label="Exit", command=root.quit)

menu.config(menu=options)
root.config(menu=menu)

tk.Label(root, text="Ha ha ha", height=5, width=30).pack(fill=tk.BOTH, expand=tk.YES)
root.mainloop()

