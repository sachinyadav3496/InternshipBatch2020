import tkinter as tk
from PIL.ImageTk import PhotoImage
import PIL
import cv2 

im = cv2.imread('images/sachin.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
im = cv2.resize(im, (600, 400))
im = PIL.Image.fromarray(im)

# open powershell window with root privileges (run as adminstrator)
# python -m pip install opencv-python
root = tk.Tk()
im = PhotoImage(image=im)

lb = tk.Label(root,  text="Sachin Yadav\nGrras Solutions Pvt. Ltd,\nJaipur",image=im, font=("Courier", 35, 'bold'),
fg='white', compound=tk.LEFT, justify=tk.LEFT, bg='#333333')

lb.pack()
root.mainloop()