from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Arpit")
# root.wm_iconbitmap('')<-- icon path in string



width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f'{width}x{height}')
Button(text='close', command=root.destroy).pack()


root.mainloop()