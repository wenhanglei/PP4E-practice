from tkinter import *

message = Message(text='Hello World! I am a message, you can see me')
message.config(bg='yellow', font=('times', 20, 'italic'))
message.pack(expand=YES, fill=BOTH)
message.mainloop()
