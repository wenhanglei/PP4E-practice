from tkinter import *
from entry2 import makeform, fetch, fields

def show(entries, popup):
    fetch(entries)
    popup.destroy()

def ask():
    popup = Toplevel()
    entries = makeform(popup, fields)
    Button(popup, text='Ok', command=lambda: show(entries, popup)).pack()
    popup.focus_set()
    popup.grab_set()
    popup.wait_window()

root = Tk()
Button(root, text='popup', command=ask).pack()
root.mainloop()