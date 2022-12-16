from tkinter import *
from tkinter import messagebox

def myfun():
    print('button dabavyu tame')

def help():
    print('hu madad karis')
    messagebox.showinfo('HA', 'jankari ahee dekhase')

def rateus():
    print('rate us')
    javab = messagebox.askquestion('Anubhav', 'maja aavi ke nai?')
    print(javab)
    if javab == 'yes':
        msg = 'aabhar tamaro'
    else:
        msg = 'to thatu hoy e kari le ja'
    messagebox.showinfo('feedback', msg)


root = Tk()
root.geometry('500x500')



# my_menu = Menu(root)
# my_menu.add_command(label='File', command=mufun)
# my_menu.add_command(label='Exit', command=quit)
# root.config(menu=my_menu)


main_menu = Menu(root)
m1 = Menu(main_menu, tearoff=0)
m1.add_command(label='New', command=myfun)
m1.add_command(label='Save', command=myfun)
m1.add_separator()
m1.add_command(label='Save as', command=myfun)
m1.add_command(label='Cancel', command=myfun)
root.config(menu=main_menu)
main_menu.add_cascade(label='File', menu=m1)

m2 = Menu(main_menu, tearoff=0)
m2.add_command(label='cut', command=myfun)
m2.add_command(label='copy', command=myfun)
m2.add_separator()
m2.add_command(label='paste', command=myfun)
m2.add_command(label='print', command=myfun)
root.config(menu=main_menu)
main_menu.add_cascade(label='Edit', menu=m2)

m3 = Menu(main_menu, tearoff=0)
m3.add_command(label='Help', command=help)
root.config(menu=main_menu)
main_menu.add_cascade(label='Help', menu=m3)

m4 = Menu(main_menu, tearoff=0)
m4.add_command(label='Rate us', command=rateus)
root.config(menu=main_menu)
main_menu.add_cascade(label='Rate', menu=m4)

main_menu.add_cascade(label='Exit', command=quit)

root.mainloop()