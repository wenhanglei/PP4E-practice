from tkinter import *
from tkinter.colorchooser import askcolor

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack(expand=YES, fill=BOTH)
        self.btn = Button(self,
                          text='Set Background Color',
                          command=self.change_color)
        self.btn.pack(expand=YES, fill=BOTH)
    def change_color(self):
        color = askcolor()
        self.btn.config(bg=color[1])
Demo().mainloop()



