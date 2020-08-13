
import tkinter as tk

root = tk.Tk() 
#Tk() -> creates a root window for you


main_frame = tk.Frame(root, height=350, width=350, bg='red')

main_frame.pack()
root.title("MyApp")
root.iconbitmap('images/main.ico')
root.configure(bg='blue')
root.wm_minsize(400, 400)
#root.wm_minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.resizable(0, 0)
#root.wm_maxsize(800, 800)
root.mainloop()
#mainloop() runs your root window untill you close your application
