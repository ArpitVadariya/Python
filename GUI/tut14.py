from tkinter import *

def leftclick(event):
    print('<Button-1> --> left click')

def rightclick(event):
    print('<Button-3> --> right click')

def doubleclick(event):
    print('<Double-1> --> double click')

root = Tk()
root.geometry('300x300')
root.title('events')

widget = Button(root, text='mane dabavo')
widget.pack()


widget.bind('<Button-1>', leftclick)
widget.bind('<Button-3>', rightclick)
widget.bind('<Double-1>', doubleclick)


root.mainloop()