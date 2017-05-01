"create two linked scales used to lauch dialog demos"

from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Scale demos').pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
              command=self.onMove,
              variable=self.var,
              from_=0, to=len(demos)-1).pack()
        Scale(self, label='Pick demo numbe',
              command=self.onMove,
              variable=self.var,
              from_=0, to=len(demos)-1,
              length=200, tickinterval=1,
              showvalue=YES, orient='horizontal').pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self,text="State", command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]
        print(demo())

    def report(self):
        print(self.var.get())
if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()

























