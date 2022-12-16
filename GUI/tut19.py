from tkinter import *
from tkinter import messagebox


def itneaadami():
    print(f'sardar {myslider2.get()} aadami the')
    messagebox.showinfo('gabbar', 'Aur Tum Teen fir bhi vapas lot ke aaye')


root = Tk()
root.geometry('300x300')
root.title('slider')

# verticle slider
# myslider = Scale(root, from_=0, to=500, orient='vertical').pack()

Label(root, text='kitne aadmi the?').pack()
# horizontal slider
myslider2 = Scale(root, from_=0, to=5, orient='horizontal', tickinterval=2)
myslider2.set(1)
myslider2.pack()
Button(root, text='aatla', command=itneaadami).pack()




root.mainloop()