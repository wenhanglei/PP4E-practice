"""
use Entry widgets directly
lay out by rows with fixed-width labels
"""

from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())

def makeform(root, fields):
    entries = []
    for field in fields:
         row = Frame(root)
         lab = Label(row, width=5, text=field)
         ent = Entry(row)
         row.pack(side=TOP, fill=X)
         lab.pack(side=LEFT)
         ent.pack(side=RIGHT, expand=YES, fill=X)
         entries.append(ent)
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', lambda event: fetch(ents))
    Button(root, text='Fetch',
           command=lambda: fetch(ents))
    Quitter(root).pack(side=RIGHT)
    root.mainloop()

















