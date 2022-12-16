from tkinter import *

def getval():
    print(username.get())
    print(password.get())

root = Tk()
root.geometry('600x600')

unm = Label(root, text='username')
pwd = Label(root, text='password')

unm.grid()
pwd.grid()

username = StringVar()
password = StringVar()

userentry = Entry(root, textvariable=username)
passwordentry = Entry(root, textvariable=password)

userentry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

Button(text='Submit', command=getval).grid()


root.mainloop()