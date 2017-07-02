"""
从简单的tkinter GUI启动getfile脚本
"""

import sys, os
from tkinter import *
from tkinter.messagebox import showinfo

def onReturnKey():
    cmdline = ('python getfile.py -mode client -file %s -port %s -host %s' %
               (content['File'].get(),
                content['Port'].get(),
                content['Server'].get()))
    os.system(cmdline)
    showinfo('getfilegui_1', 'Download complele')

box = Tk()
labels = ['Server', 'Port', 'File']
content = {}
for label in labels:
    row = Frame(box)
    row.pack(fill=X)
    Label(row, text=label, width=6).pack(side=LEFT)
    entry = Entry(row)
    entry.pack(side=RIGHT, expand=YES, fill=X)
    content[label] = entry

box.title('getfilegui_1')
box.bind('<Return>', (lambda event: onReturnKey()))
mainloop()




























