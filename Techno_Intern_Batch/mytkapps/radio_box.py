import tkinter as tk 

root = tk.Tk()

v = tk.StringVar()
v.set("India")

label = tk.Label(root, text="Which Country you belong ?")
label.config(font=("Courier", 20, 'bold'))
label.pack(padx=20, pady=20)

rd1 = tk.Radiobutton(root, text="India", value="India", variable=v,
font=("Courier", 20, 'bold'), indicatoron=0)
rd1.pack(anchor=tk.W,padx=20, pady=20)

rd2 = tk.Radiobutton(root, text="USA", value="USA", variable=v,
font=("Courier", 20, 'bold'), indicatoron=0)
rd2.pack(anchor=tk.W,padx=20, pady=20)

rd3 = tk.Radiobutton(root, text="UK", value="UK", variable=v,
font=("Courier", 20, 'bold'), indicatoron=0)
rd3.pack(anchor=tk.W,padx=20, pady=20)

rd4 = tk.Radiobutton(root, text="CHINA", value="CHINA", variable=v,
font=("Courier", 20, 'bold'), indicatoron=0)
rd4.pack(anchor=tk.W,padx=20, pady=20)

def show_value():
    print(v.get())

b = tk.Button(root, text="show value", command=show_value)
b.config(font=("Courier", 20, 'bold'))
b.pack(padx=20, pady=20)
root.mainloop()