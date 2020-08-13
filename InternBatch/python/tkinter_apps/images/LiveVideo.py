import tkinter as tk
import PIL
from PIL.ImageTk import PhotoImage
import cv2
# python -m pip install opencv-python
width, height = 800, 600
root = tk.Tk()
device = cv2.VideoCapture(1)
device.set(cv2.CAP_PROP_FRAME_WIDTH, width)
device.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
def click_image():    
    flag, image = device.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image = cv2.flip(image, 1)
    image = PIL.Image.fromarray(image)
    
    imgtk = PhotoImage(image=image)
    lb.imgtk = imgtk # local scope ?  delete after function call so 
    # we have to store our imgage inside label object
    # obj.attr = 'new value'
    lb.config(image=imgtk)
    lb.after(10, click_image)


lb = tk.Label(root, font=("Courier", 35, 'bold'))
lb.pack(fill=tk.BOTH, expand=tk.YES)
button = tk.Button(root, text="Exit", font=("Courier", 25, 'bold'),
height=2, width=30, command=root.quit)
button.pack(fill=tk.X)
lb.after(1, click_image)
root.mainloop()