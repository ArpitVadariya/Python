from tkinter import *
from PIL import ImageTk, Image


def every_100(text):
    final_text = ''
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100 == 0 and i!=0:
            final_text += '\n'
    return final_text

root = Tk()
root.geometry('1000x1000')
root.title('Toofan Express')

texts = []
photos = []
for i in range(0, 3):
    with open(f'{i+1}.txt') as f:
        text = f.read()
        texts.append(every_100(text))
        # print('HA')
    
    image = Image.open('Realme.png')
    # image.resize(25, 25)
    image = image.resize((100, 100), Image.Resampling.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))


f0 = Frame(root, width=800, height=70, pady=10)
Label(f0, text='Toofan Express', font='lucida 60 bold', fg='red', bg='yellow', padx=600, pady=30).pack()
Label(f0, text='February 29, 2000', font='lucida 10 italic', pady=10).pack()
f0.pack()

f1 = Frame(root, width=900, height=200)
# Label(f1, text=texts[0]).pack(side='left')
Label(f1, text=texts[0], padx=22, pady=22).pack(side='left')
Label(f1, image=photos[0], anchor='e').pack()
f1.pack(anchor='w')

f2 = Frame(root, width=900, height=200)
# Label(f1, text=texts[0]).pack(side='left')
Label(f2, text=texts[1], padx=22, pady=22).pack(side='right', anchor='e')
Label(f2, image=photos[0], anchor='e').pack()
f2.pack(anchor='e')



f3 = Frame(root, width=900, height=200)
# Label(f1, text=texts[0]).pack(side='left')
Label(f3, text=texts[2], padx=22, pady=22).pack(side='left')
Label(f3, image=photos[0], anchor='e').pack()
f3.pack(anchor='w')


root.mainloop()