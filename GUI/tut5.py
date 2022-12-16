from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.geometry('500x500')
# photo = PhotoImage(file="Realme.png")
# for jpg images

image = Image.open("Arpit Bitmoji.jpeg")
photo = ImageTk.PhotoImage(image)
lbl_photo = Label(image=photo)
lbl_photo.pack()


root.mainloop()