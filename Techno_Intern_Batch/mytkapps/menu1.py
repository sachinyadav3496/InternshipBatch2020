from tkinter import * 

root = Tk()

menu = Menu(root)

fmenu = Menu(menu)

fmenu.add_command(label="...Open...", command=lambda : print("...Open..."))
fmenu.add_command(label="...New...", command=lambda : print("...New..."))
fmenu.add_command(label="...Folder...", command=lambda : print("...Folder..."))
fmenu.add_command(label="...Exit...", command=lambda : root.quit())

other = Menu(menu)

sb_menu = Menu(other)

sb_menu.add_command(label="info", command=lambda: print("information about company"))
sb_menu.add_command(label='hello', command=lambda: print("hello world"))

other.add_cascade(label='Other', menu=sb_menu)

menu.add_cascade(label="File", menu=fmenu)

menu.add_separator()

menu.add_cascade(label='other', menu=other)

root.config(menu=menu)

root.mainloop()




