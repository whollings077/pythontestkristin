from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300+10+10")
root.config(bg="#3655ff")
frame = Frame(root)
frame.pack()

operators = ["+", "-", "*", "/"]
operatorselect = ttk.Combobox(frame, values=operators)
operatorselect.set("Pick an Option")
operatorselect.place(x=210, y=50)


root.mainloop()