"""
similar, but show return values of dialo calls; the lambda saves data from
the local scope to be passed to the handler (button press handlers normally
get no arguments, and enclosin scope references don't work for loop variables)
and works just like a nested def statement: def func(key=key): self.printit(key)
"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Basic demos").pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns =>', demos[name]())

if __name__ == '__main__':
    Demo().mainloop()





















