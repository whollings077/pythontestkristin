from tkinter import *
class MyWindow:
    def __init__(self, win):

        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.lbl4=Label(win, text='Answer')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b1.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=int(self.t4.get())
        if num1+num2==result:
            self.t3.insert(END, 'Correct')
            with open('logs.txt', 'a') as f:
                f.write("Correct " + str(num1) + '+' + str(num2) + '=' + str(num1+num2) + '\n' )
        else:
            self.t3.insert(END, 'Incorrect')
            with open('logs.txt', 'a') as f:
                f.write("Incorrect " + str(num1) + '+' + str(num2) + '=' + str(num1+num2) + '\n')

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()