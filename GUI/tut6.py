from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Arpit")

lbl_ttl = Label(text='''QWERTYUIOP
ASDFGHJKL
ZXCVBNM''', bg="red", fg="white", padx=123, pady=50, font=("comicsansms", 19, "bold"))

lbl_ttl.pack(anchor="sw", side="bottom", fill="x", padx="20", pady="20")

root.mainloop()