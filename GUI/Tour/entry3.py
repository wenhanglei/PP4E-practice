"""
using StringVar variable
"""

from tkinter import *
from quitter import Quitter
fields = 'name', 'job', 'pay'

def fetch(vars):
    for field, var in zip(fields, vars):
        print('%s => %s' % (field, var.get()))

def makeform(root, fields):
    vars = []
    fr = Frame(root)
    fr.pack(expand=YES, fill=BOTH)
    for filed in fields:
        row = Frame(fr)
        row.pack(expand=YES, fill=BOTH)
        Label(row, text=filed, width=5).pack(side=LEFT)
        ent = Entry(row)
        var = StringVar()
        ent.config(textvariable=var)
        ent.pack(side=RIGHT)
        var.set('enter here')
        vars.append(var)
    return vars

if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=lambda: fetch(vars)).pack()
    root.mainloop()












