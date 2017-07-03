import getfile
from tkinter import *
from tkinter.messagebox import showinfo

def onSubmit():
    getfile.client(content['Server'].get(),
                   int(content['Port'].get()),
                   content['File'].get())
    showinfo('getfilegui_2', 'Download complete')

box = Tk()
labels = ['Server', 'Port', 'File']
rownum = 0
content = {}
for label in labels:
    Label(box, text=label).grid(column=0, row=rownum)
    entry = Entry(box)
    entry.grid(column=1, row=rownum, sticky=E+W)
    content[label] = entry
    rownum += 1

box.columnconfigure(0, weight=0)
box.columnconfigure(1, weight=1)
Button(text='Sumit', command=onSubmit).grid(row=rownum, column=0, columnspan=2)

box.title('getfilegui_2')
box.bind('<Return>', (lambda event: onSubmit()))
mainloop()



































