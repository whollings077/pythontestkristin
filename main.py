from tkinter import *
import random
class MyWindow:
    def __init__(self, win):

        self.lbl1=Label(win, text='Answer')
        self.lbl2=Label(win, text='Correct/Incorrect')
        self.lbl3=Label(win, text='+')
        self.t1=Entry(state='readonly' , bd=3)
        self.t2=Entry(state='readonly', bd=3)
        self.t3=Entry( bd=3)
        self.t4=Entry(state='readonly', bd=3)
        self.t1.place(x=50, y=50)
        self.t2.place(x=250, y=50)
        self.b1=Button(win, text='submit answer', command=self.answer)
        self.b2=Button(win, text='generate numbers', command=self.generate)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl1.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.lbl2.place(x=100, y=250)
        self.t4.place(x=200, y=250)
        self.lbl3.place(x=210, y=50)
    def generate(self):
        self.t1.config(state='normal') #allow editing of the number boxes
        self.t2.config(state='normal')
        self.t4.config(state='normal')
        self.t1.delete(0, 'end') #clear the number boxes
        self.t2.delete(0, 'end')
        self.t4.delete(0, 'end')
        num1=random.randint(1, 10) #generate random numbers
        num2=random.randint(1, 10)
        self.t1.insert(END, str(num1)) #insert the numbers into the boxes
        self.t2.insert(END, str(num2))
        self.t1.config(state='readonly') #make the boxes read only again
        self.t2.config(state='readonly')
        self.t4.config(state='readonly')

    def answer(self):
        answer=int(self.t3.get())
        result=int(self.t1.get())+int(self.t2.get())
        if result==answer:
            self.t4.config(state='normal')
            self.t4.delete(0, 'end')
            self.t4.insert(END, 'Correct')
            self.t4.config(state='readonly')
            with open('logs.txt', 'a') as f:
                f.write("Correct " + str(answer) + "="+ str(result) + '\n')
        else:
            self.t4.config(state='normal')
            self.t4.delete(0, 'end')
            self.t4.insert(END, 'Incorrect')
            self.t4.config(state='readonly')
            with open('logs.txt', 'a') as f:
                f.write("Incorrect " + str(answer) + "="+ str(result) + '\n')

window=Tk()
mywin=MyWindow(window)
window.title('Williams Math Game')
window.geometry("500x300+10+10")
window.mainloop()