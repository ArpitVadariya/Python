from tkinter import *

root = Tk()

# root.geometry("width x height")
root.geometry("600x300")

f1 = Frame(root, bg='red', borderwidth=6, relief='sunken')
f1.pack(side='left', fill='y')

f2 = Frame(root, bg='green', borderwidth=10, relief='sunken')
f2.pack(side='top', fill='x')


l1 = Label(f1, text='Tkinter', font='Helvetica 16 bold', fg='blue', pady=2)
l1.pack(pady=40)
l2 = Label(f1, text='Tkinter2')
l2.pack()



root.mainloop()