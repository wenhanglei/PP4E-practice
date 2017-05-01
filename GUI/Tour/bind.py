from tkinter import *

def show_pos_event(event):
    print('widget:%s x:%s y:%s' % (event.widget, event.x, event.y))

def get_attr_in_event(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith("__"):
            print(attr, ' => ', getattr(event, attr))

def on_key_press(event):
    print('Got key press: ' + event.char)

def on_arrow_key(event):
    print('Got arrow key pressed')

def on_return_key(event):
    print('Got return key pressed')

def on_left_click(event):
    print('Got left mouse click: ', end=' ')
    show_pos_event(event)

def on_right_click(event):
    print('Got right mouse click: ', end=' ')
    show_pos_event(event)

def on_middle_click(event):
    print('Got middle mouse click: ', end=' ')
    show_pos_event(event)

def on_left_drag(event):
    print('Got left mouse drag: ', end=' ')
    show_pos_event(event)

def on_double_left_click(event):
    print('Got double left click: ', end=' ')
    show_pos_event(event)
    root.quit()

root = Tk()

label_font = ('courier', 20, 'bold')
widget = Label(root, text='hello event world!')
widget.config(bg='pink',font=label_font)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', on_left_click)
widget.bind('<Button-3>', on_right_click)
widget.bind('<Button-2>', on_middle_click)
widget.bind('<B1-Motion>', on_left_drag)
widget.bind('<Double-1>', on_double_left_click)

widget.bind('<KeyPress>', on_key_press)
widget.bind('<Down>', on_arrow_key)
widget.bind('<Return>', on_return_key)

widget.focus()
root.mainloop()




















