from tkinter import * 
root = Tk() 

lst = Listbox(root)
lst.config(font=("Courier", 20, 'bold'), fg="#eeeeee", bg='#222222')

sc = Scrollbar(lst)

for i in range(50):
    print(f"adding {i}th element")
    lst.insert(i, f"Hello World Times {i}")


sc.config(command=lst.yview)
lst.config(yscrollcommand=sc.set)


sc.pack(side=RIGHT, fill=Y)
lst.pack(side=LEFT, fill=BOTH, expand=YES)
def print_item(event):
    i = lst.curselection()
    print("You have selected item ", lst.get(i))
lst.bind("<Button-1>", print_item)
root.minsize(400, 400)
root.mainloop()