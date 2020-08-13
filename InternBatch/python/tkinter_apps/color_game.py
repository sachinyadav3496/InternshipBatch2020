import tkinter as tk
from random import shuffle
colors = [ 'red', 'green', 'yellow', 'purple', 'gray', 'magenta', 'cyan', 'blue',
         'orange', 'black']
last_color = None
score = 0
timeout = 30
start = False

root = tk.Tk()

frame = tk.Frame(root, bg='#333333')

ct = list(map(str.upper, colors))
clb = tk.Label(root, text=", ".join(ct), bg='#333333', fg='#eeeeee', font=("Times", 15, 'bold'))
clb.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)


t = tk.Label(root, text=f"Time Left: {timeout}", font=("Courier", 15, 'bold'))
t.config(width=25, bg='#333333', fg='#eeeeee')
t.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)

l1 = tk.Label(root, text="", fg='red', font=("courier", 50, 'bold'))
l1.config(width=10, bg='#c0c0c0', relief=tk.RAISED, borderwidth=5)
l1.pack(side=tk.TOP, expand=tk.YES)

s = tk.Label(root, text=f"Your Score: {score}", font=("Courier", 20, "bold"), 
            height=3, width=25, bg="#333333", fg="#eeeeee")

s.pack(side=tk.TOP, expand=tk.YES)


quit = tk.Button(root, text="Exit", command=root.quit,
                width=10, bg="#dddddd", relief=tk.RAISED, fg="#333333",
                font=("Times", 15, 'italic'))

quit.pack(side=tk.BOTTOM, expand=tk.YES)

e = tk.Entry(root, font=("Courier", 25, "bold"), bg="#333333", fg="#eeeeee")
e.pack(side=tk.BOTTOM, expand=tk.YES)


frame.pack(fill=tk.BOTH, expand=tk.YES)


def choose_color():
    global last_color
    shuffle(colors)
    if last_color == colors[0]:
        choose_color()
    else:
        last_color = colors[0]
        

def change_color(event):
    global score, start
    start = True
    if e.get().lower().strip() == colors[0]:
        score += 1
        s.config(text=f"Your Score: {score}")
    e.focus_set()
    e.delete(0, tk.END)
    choose_color()
    l1.config(text=colors[1].upper(), fg=colors[0])
    
def start_timer():
    global timeout, start, score
    if start:
        if timeout:
            timeout -= 1
            t.config(text=f"Time Left: {timeout}")
            t.update()
            t.after(1000, start_timer)
        else:
            l1.config(text="")
            win = tk.Toplevel(root)
            # pop up window
            win.focus()
            win.grab_set()
            lab = tk.Label(win, text=f"Your Final Score is: {score}",
                          fg='#dddddd', bg='#333333')
            
            lab.config(font=("courier", 25, "bold"), height=5, width=25)
            lab.pack(fill=tk.BOTH, expand=tk.YES)
            b = tk.Button(win, text="Exit", command=win.destroy, font=("times", 15))
            b.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.YES)
            b.config(fg="#333333", bg="#dddddd")
            
            timeout = 30
            start = False
            score = 0
            start_timer()
    else:
        t.after(1000, start_timer)
    

e.focus()


prompt = tk.Label(root, text="Type in Your Guess Color Here", bg="#333333", 
              fg="#eeeeee", font=("Times", 15, "bold"))
prompt.pack(side=tk.BOTTOM, expand=tk.YES)

start_timer()

root.bind("<Return>", change_color)

root.config(bg="#333333")
root.wm_minsize(600, 400)

root.title("Color Game")

root.iconbitmap('images/main.ico')

root.mainloop()
