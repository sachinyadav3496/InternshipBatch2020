import tkinter as tk
from PIL.ImageTk import PhotoImage
import PIL
import cv2 

height, width = 600, 800
device = cv2.VideoCapture(0)
device.set(cv2.CAP_PROP_FRAME_WIDTH,width)
device.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

root = tk.Tk()
photo_Frame = tk.Label(root,)
photo_Frame.pack(fill=tk.BOTH, expand=tk.YES)

def capture():
    _, photo = device.read() # click
    im = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(im)
    image = PhotoImage(image=image)
    photo_Frame.config(image=image)
    photo_Frame.image = image # to store a local variable in photo_frame
button = tk.Button(root, text="CLICK", command=capture)
button.config(height=2, bg='black', fg='white')
button.pack(fill=tk.X)

root.mainloop()