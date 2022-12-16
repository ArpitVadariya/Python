from tkinter import *

def myfun(text):
    print(f'{text}')
    pass

root = Tk()
root.geometry('500x500')



# my_menu = Menu(root)
# my_menu.add_command(label='File', command=mufun)
# my_menu.add_command(label='Exit', command=quit)
# root.config(menu=my_menu)


main_menu = Menu(root)
m1 = Menu(main_menu, tearoff=0)
m1.add_command(label='New', command=myfun('New'))
m1.add_command(label='Save', command=myfun('Save'))
m1.add_separator()
m1.add_command(label='Save as', command=myfun('Save as'))
m1.add_command(label='Cancel', command=myfun('Cancel'))
root.config(menu=main_menu)
main_menu.add_cascade(label='File', menu=m1)

m2 = Menu(main_menu, tearoff=0)
m2.add_command(label='cut', command=myfun('cut'))
m2.add_command(label='copy', command=myfun('copy'))
m2.add_separator()
m2.add_command(label='paste', command=myfun('paste'))
m2.add_command(label='print', command=myfun('print'))
root.config(menu=main_menu)
main_menu.add_cascade(label='Edit', menu=m2)

main_menu.add_cascade(label='Exit', command=quit)



root.mainloop()