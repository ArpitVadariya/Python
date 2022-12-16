from tkinter import *

root = Tk()
root.geometry('500x500')


def JSK():
    print("JAs Shree Krishna")
def JSR():
    print("HellJay Shree Ram")
def HHM():
    print("Har Har Mahadev")

frame1 = Frame(root, borderwidth=10, bg='red', relief='sunken')
frame1.pack(side='left', anchor='nw')
# here pax will add padding inside the button in the text
# button1 = Button(frame1, bg='yellow' , fg='blue', text='Jay Shree Krishna', padx='123', command=JSK)
# here pax will add padding outside the button inside the frame 
# button1.pack(side='left', padx='123')
button1 = Button(frame1, bg='yellow' , fg='blue', text='Jay Shree Krishna', command=JSK)
button1.pack(side='left')
button2 = Button(frame1, bg='yellow' , fg='blue', text='Jay Shree Ram', command=JSR)
button2.pack(side='left')
button3 = Button(frame1, bg='yellow' , fg='blue', text='Har Har Mahadev', command=HHM)
button3.pack(side='left')




root.mainloop()