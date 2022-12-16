from tkinter import *

root = Tk()

canvas_width = 600
canvas_height = 400

root.geometry(f'{canvas_width}x{canvas_height}')
# root.geometry('900x900')

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 200, 600, 200, fill='red')
can_widget.create_line(300, 0, 300, 400, fill='blue')

can_widget.create_rectangle(10, 10, 50, 70, fill='yellow')
can_widget.create_rectangle(50, 10, 70, 70, fill='green')



root.mainloop()