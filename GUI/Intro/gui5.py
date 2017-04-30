from tkinter import *

class MyButton(Button):
    def __init__(self, text):
        Button.__init__(self)
        self.config(text=text, command=self.quit)

    def quit(self):
        sys.exit()

if __name__ == '__main__':
    MyButton('Hello Class World!').pack()
    mainloop()