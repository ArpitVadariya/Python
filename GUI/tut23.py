# solution of excercise 2
from tkinter import *
from turtle import *

def update():
    print('update')
    update_width = width.get()
    update_height = height.get()
    # if update_width == '':
    #     update_width = root.winfo_screenwidth()
    # if update_height == '':
    #     update_width = root.winfo_screenheight()
    # print(update_width)
    # print(update_height)
    # print(f'update-->{update_width}<--')
    root.geometry(f'{update_width}x{update_height}')




root = Tk()
root.geometry('300x200')
width = StringVar()
height = StringVar()


Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()
Button(root, text='Apply', command=update).pack()



root.mainloop()