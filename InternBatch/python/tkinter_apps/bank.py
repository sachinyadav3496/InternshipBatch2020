import tkinter as tk 

### https://github.com/sachinyadav3496/Bank_Application
root = tk.Tk()

sex = tk.StringVar()
sex.set('Male')

country = tk.StringVar()
country.set('India')

name = tk.StringVar()
font = ("Courier", 20, 'bold')

l = tk.Label(root, text="Name: ", font=font)
l.grid(row=0, column=0, columnspan=2)

e = tk.Entry(root, textvariable=name, font=font)
e.grid(row=0, column=2, columnspan=2)
lb = tk.Label(root, text="Gender ?", font=font)
lb.grid(row=1, column=0, columnspan=4)

b1 = tk.Radiobutton(root, value="Male", variable=sex, text="Male", font=font)
b1.grid(row=2, column=0, columnspan=2)
b2 = tk.Radiobutton(root, value="Female", variable=sex, text="Female", font=font )
b2.grid(row=2, column=2, columnspan=2)

lb2 = tk.Label(root, text="Country ?", font=font)
lb2.grid(row=4, column=0, columnspan=4)

b3 = tk.Radiobutton(root, value="India", variable=country, text="India", font=font)
b3.grid(row=5, column=0, columnspan=2)
b4 = tk.Radiobutton(root, value="Other", variable=country, text="Other", font=font )
b4.grid(row=5, column=2, columnspan=2)

def submit():
    top = tk.Toplevel(root, height=400, width=400)
    top.grab_set()
    message = f"""
    Name   = {name.get()}
    Gender = {sex.get()}
    Country = {country.get()}
    """
    m = tk.Message(top, text=message, font=font)
    m.pack()


button = tk.Button(text='Submit', font=font, command=submit)
button.grid(row=6, columnspan=4)

root.mainloop()

# check box, canvas 
# saturday, sunday -> scrollbar--> doubts