import tkinter as tk 
from PIL.ImageTk import PhotoImage

root = tk.Tk()

def enlarge(event):
    lb.config(height=tkimg.height()+10, width=tkimg.width()+10)
def normal(event):
    lb.config(height=tkimg.height(), width=tkimg.width())
#tkimg = tk.PhotoImage(file="images/one.gif")
tkimg = PhotoImage(file="images/corona.jpg")


lb = tk.Label(root,  text="Python is Awesome!", image=tkimg, justify=tk.LEFT,
compound=tk.CENTER, font=("Courier", 25, "bold"), fg='white')

lb.config(height=tkimg.height(), width=tkimg.width())
lb.pack()

lb.bind("<Enter>", enlarge)
lb.bind("<Leave>", normal)

msg = """Coronavirus live updates: India reports 8,171 new Covid cases
 and 204 deaths in last 24 hours
The death toll due to Covid-19 rose to 
5,598 and the number of cases has climbed to
 198,706 in the country. While the recovery 
 rate in India is progressively increasing and 
 has reached 48.19% amongst coronavirus patients, 
 the health ministry said. Stay here for all live 
 updates"""

mblock = tk.Message(root, text=msg)
mblock.config(font=('Times', 20, 'bold'))
mblock.pack()
root.mainloop()
# gif, png, .... jpeg