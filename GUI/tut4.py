from tkinter import *

root = Tk()

# root.geometry(widthxheight)
# root.geometry('100x100')

# root.minsize(width, height)
root.minsize(250, 250)
# root.maxsize(width, height)
root.maxsize(650, 650)

lbl_1 = Label(text='First LABEL')
lbl_1.pack()



root.mainloop()