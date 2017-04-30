from tkinter import *

class HelloClass:
    def __init__(self):
        self.btn = Button(text='press me', command=self.method)
        self.btn.pack(expand=YES)

    def method(self):
        print('Hello Class World!')
        sys.exit()

HelloClass()
mainloop()
