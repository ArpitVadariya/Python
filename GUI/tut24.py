from tkinter import *

def upload():
    statusvar.set('Ubharyo Ubharyo Ubharyo')
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set('Halo Have')



root = Tk()
root.geometry('400x400')
root.title('Statusbar')


statusvar = StringVar()

statusvar.set('Ready')

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)
Button(root, text='upload', command=upload).pack()
root.mainloop()