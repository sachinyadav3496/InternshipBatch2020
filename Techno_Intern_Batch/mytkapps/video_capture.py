import tkinter as tk
import PIL
from PIL import ImageTk
import cv2 

height, width = 600, 800
cam_device = cv2.VideoCapture(0)
cam_device.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam_device.set(cv2.CAP_PROP_FRAME_WIDTH, width)

codec = cv2.VideoWriter_fourcc(*'XVID') #.mp4, .avi, .dvi.  
output = cv2.VideoWriter('output.avi', codec, 24.0, (height, width))

root = tk.Tk() 
video = tk.Label(root)
video.pack(fill=tk.BOTH, expand=tk.YES)

def destroy():
    cam_device.release()
    output.release()
    root.quit()
button = tk.Button(root, text='Exit', command = destroy)
button.config(bg='black', fg='white', font=("courier", 20, 'bold'), height=2)
button.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.YES)
def capture():
    _, im = cam_device.read()
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    output.write(im)
    im = cv2.flip(im, 1)
    im = PIL.Image.fromarray(im)
    tk_image = ImageTk.PhotoImage(image=im) 
    # we are converting an image into tkinter suitable format
    video.config(image=tk_image)
    video.tk_image = tk_image
    # we are saving image with label so that it should not be deleted after function call
    # tk_image is local variable so it will delete to prevent this we are storing it into label widget
    video.after(10, capture)

video.after(1, capture)
# 1 -> millisecond
root.mainloop()