from tkinter import *
from quitter import Quitter

def fetch():
    print('message you typed is: ' + ent.get())

root = Tk()

ent = Entry(root)
ent.bind('<Return>', lambda event: fetch())
ent.insert(0, 'please type some words')
ent.pack(fill=X)

ent.focus()

Button(root, text='Fetch', command=fetch).pack(side=LEFT)
Quitter(root).pack(side=RIGHT)

root.mainloop()
