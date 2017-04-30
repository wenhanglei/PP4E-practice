from tkinter import *
from gui5 import MyButton

class HelloButton(MyButton):
    def quit(self):
        print('bye bye Hello world!')
        sys.exit()

if __name__ == '__main__':
    HelloButton('hello').pack()
    mainloop()



