from tkinter import *
from tkinter import messagebox

def javab():
    messagebox.showinfo('javab', f'o to te coffe {var.get()} mangavi')

root = Tk()
root.geometry('300x300')
root.title('radiobutton')

var = StringVar()
# by default selected 1 value
var.set('khalee')
Label(root, text='te coffe kem mangavi?', font='lucida 16 bold', justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text='bhave etle', padx=14, variable=var, value='bhave etle').pack(anchor='w')
radio = Radiobutton(root, text='cha garam noti etle', padx=14, variable=var, value='cha garam noti etle').pack(anchor='w')
radio = Radiobutton(root, text='kadak cha noti etle', padx=14, variable=var, value='kadak cha noti etle').pack(anchor='w')
radio = Radiobutton(root, text='maja aavi etle', padx=14, variable=var, value='maja aavi etle').pack(anchor='w')
radio = Radiobutton(root, text='aapel paiki ek pan nahi', padx=14, variable=var, value='aapel paiki ek pan nahi').pack(anchor='w')

Button(text='javab de', command=javab).pack()

root.mainloop()