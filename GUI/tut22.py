from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Scrollbar')


scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

# scrollbar for listbox
# listbox = Listbox(root, yscrollcommand= scrollbar.set)
# for i in range(50):
#     listbox.insert(END, f'Item --> {i+1}')

# listbox.pack(fill=BOTH)
# scrollbar.config(command=listbox.yview)


# scrollbar for textbox
text = Text(root, yscrollcommand= scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
root.mainloop()