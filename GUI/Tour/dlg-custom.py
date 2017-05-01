from tkinter import *

makemodal = len(sys.argv)>1             #如果从控制台输入参数则设置为锁定对话框


def dialog():
    win = Toplevel()
    Label(win, text='I am a popup dialog.').pack()
    Button(win, text='Ok', command=win.destroy).pack()
    if makemodal:
        win.focus_set()                  #锁定对话框
        win.grab_set()                   #阻止其他窗口的响应
        win.wait_window()                #等待该对话框退出
    print('dialog exited.')

win = Tk()                               #创建主窗口
Label(win, text='popup new dialog').pack()
Button(win, text='create', command=dialog).pack()
win.mainloop()