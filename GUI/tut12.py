from tkinter import *

root = Tk()
root.geometry('500x500')

def getval():
    print('hailu hailu hailu')
    # print the name from checkbox
    print(namevalue.get())

# heading
Label(root, text='Jay Shree Krishna', font='comicsansms 16 bold', pady=5, fg='red').grid(row=0, column=3)


name = Label(root, text='name')
phone = Label(root, text='phone')
gender = Label(root, text='gender')
email = Label(root, text='email')
paisa = Label(root, text='paisa')


name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
paisa.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emailvalue = StringVar()
paisavalue = StringVar()
foodservicevalue = IntVar()


nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emailentry = Entry(root, textvariable=emailvalue)
paisaentry = Entry(root, textvariable=paisavalue)




nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paisaentry.grid(row=5, column=3)


foodservice = Checkbutton(text='khava nu joye chhe k bhegu layavya?', variable=foodservicevalue)
foodservice.grid(row=6, column=3)

Button(text='alyo', command=getval).grid(row=7, column=3)


root.mainloop()