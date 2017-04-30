from tkinter import *

def quit():
    print('execute quit()')

Button(text='Hello Event World!', command=quit).pack(expand=YES)

mainloop()