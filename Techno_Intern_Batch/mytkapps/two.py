import tkinter as tk
root = tk.Tk()
main_frame = tk.Frame(root, relief=tk.RAISED)
text_label = tk.Label(main_frame, text="Hello World", relief=tk.RAISED)
text_label.config(bg='#dddddd', font=('Courier', 30, 'bold'))
main_frame.config(bg='blue', height=300, width=300)
root.config(bg='red')
text_label.pack(ipadx=20, ipady=20, padx=20, pady=20)
main_frame.pack(ipadx=20, ipady=20, padx=30, pady=30,  fill=tk.BOTH, expand=tk.YES)
root.wm_minsize(400, 400)
root.mainloop()

# red -> dd -> 0-f -> 16 -> 14 -> 14 / 16 * 100 -> 
# green -> dd color hex code 
# blue -> dd