from tkinter import *

def print_hello():
    print('Hello')

def quit():
    sys.exit()

root = Tk()
fr = Frame(root)
Button(fr, text='Hello', command=print_hello).pack(side=LEFT, anchor=N)
Label(fr, text='Hello cantainer world!').pack()
Button(fr, text='Quit', command=quit).pack(side=RIGHT)
fr.pack(expand=YES, fill=BOTH)
root.mainloop()