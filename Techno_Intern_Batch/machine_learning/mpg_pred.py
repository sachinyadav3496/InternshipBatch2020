import tkinter as tk
import pickle

with open('mpg_model.pkl', 'rb') as fp:
    model = pickle.load(fp) 


root = tk.Tk()

frame1 = tk.Frame(root)
label1 = tk.Label(frame1, text="Displacement".center(30)+" : ",
        width=20
        )
label1.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
label1.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT)
dis = tk.DoubleVar()
dis.set('')
entry1 = tk.Entry(frame1, textvariable=dis,
        width=20
        )
entry1.focus()
entry1.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
entry1.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT)
frame1.pack(expand=tk.YES,padx=15, pady=15,)

frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="Horse Power".center(30)+" : ", width=20)
label2.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
label2.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT,fill=tk.X)
horse = tk.DoubleVar()
horse.set('')
entry2 = tk.Entry(frame2, textvariable=horse, width=20)
entry2.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
entry2.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT)
frame2.pack(expand=tk.YES,padx=15, pady=15,)

frame3 = tk.Frame(root)
label3 = tk.Label(frame3, text="Weight".center(30)+"      : ", width=20)
label3.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
label3.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT)
weight = tk.DoubleVar()
weight.set('')
entry3 = tk.Entry(frame3, textvariable=weight, width=20)
entry3.config(font=('monospace', 30, 'bold'), fg='#333333', bg='#eeeeee')
entry3.pack(expand=tk.YES,padx=15, pady=15,side=tk.LEFT, fill=tk.X)
frame3.pack(expand=tk.YES,padx=15, pady=15,)
def predict():
    d = dis.get()
    h = horse.get()
    w =weight.get()
    pred = round(model.predict([[d, h,w]])[0])
    dis.set('')
    horse.set('')
    weight.set('')
    win = tk.Toplevel(root)
    win.grab_set()
    ans = f"""
    ___________________
    HorsePower    = {h:.2f}
    Weight        = {w:.2f}
    Displacement  = {d:.2f}
    ___________________
    Milege        = {pred:.2f}
    """
    lb = tk.Message(win, text=ans)
    lb.config(font=("monospace", 20, 'bold'),
            fg='#eeeeee',
            bg='#A6AAFF',
            )
    lb.pack(expand=tk.YES,padx=15, pady=15,fill=tk.BOTH)
    b = tk.Button(win, text='EXIT', command=lambda :(win.destroy(), entry1.focus()))
    b.config(font=("monospace", 20, 'bold'),
            fg='red',
            bg='#eeeeee',
    )
    b.pack(expand=tk.YES,padx=15, pady=15,fill=tk.X)

button = tk.Button(root, text='Predict', command=lambda : predict())
button.config(font=('Times', 30, 'bold'), fg='red', bg='white')
button.pack(expand=tk.YES,padx=15, pady=15, fill=tk.X)

button1 = tk.Button(root, text='EXIT', command=lambda : root.quit())
button1.config(font=('Times', 30, 'bold'), bg='red', fg='white')
button1.pack(expand=tk.YES,padx=15, pady=15,side=tk.BOTTOM, fill=tk.X)
root.title('Milege Prediction')
root.mainloop()
