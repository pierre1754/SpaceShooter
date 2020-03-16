import vector
from tkinter import PhotoImage
from PIL import Image, ImageTk

def init(can, window):
    global background
    img = Image.open("background.png")
    img = img.resize((window.winfo_screenwidth(), window.winfo_screenheight()), resample = 0)
    background = ImageTk.PhotoImage(img)
    position = can.create_image(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2, image = background)
    
