from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock Project")


def time():
    string = strftime(
        'Military Time - %H:%M:%S\nStandard Time - %I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 30),
              background="black", foreground="green")
label.pack(anchor="center")
time()
mainloop()
