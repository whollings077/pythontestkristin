from tkinter import *
from tkinter import ttk
import random
import operator
import csv
class MyWindow:
    def __init__(self, win):

        self.lbl1=Label(win, text='Your Answer:') #where the answer is put by the user
        self.lbl2=Label(win, text='Result:') #where the program tells the user if they are correct or not
        self.lbl5=Label(win, text='Your Name:') #where the user puts their name
        self.t1=Entry(state='readonly' , bd=3) #the first number
        self.t2=Entry(state='readonly', bd=3) #the second number
        self.t3=Entry( bd=3) #where the user puts their answer
        self.t4=Entry(state='readonly', bd=3) #where the program tells the user if they are correct or not
        self.t5=Entry(state='readonly', bd=3) #where the user enters their name
        self.t1.place(x=50, y=50)
        self.t2.place(x=250, y=50)
        self.b1=Button(win, text='Submit', command=self.answer)
        self.b2=Button(win, text='New Question', command=self.generate)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl1.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.lbl2.place(x=100, y=250)
        self.t4.place(x=200, y=250)
        self.lbl5.place(x=100, y=300)
        self.t5.place(x=200, y=300)
        operators = ["+", "-", "*",] #the operators that can be used
        self.combobox = ttk.Combobox(win, values=operators, width=1)
        self.combobox.set(operators[0])
        self.combobox.place(x=200, y=50)
        self.t5.config(state='normal')
    def generate(self):
        self.t1.config(state='normal') #allow editing of the number boxes
        self.t2.config(state='normal')
        self.t4.config(state='normal')
        self.t1.delete(0, 'end') #clear the number boxes
        self.t2.delete(0, 'end')
        self.t4.delete(0, 'end')
        num1=random.randint(1, 10) #generate random numbers
        num2=random.randint(1, 10)
        if num1 < num2: #make sure the first number is bigger than the second
            num1 = num1 + num2
        self.t1.insert(END, str(num1)) #insert the numbers into the boxes
        self.t2.insert(END, str(num2))
        self.t1.config(state='readonly') #make the boxes read only again
        self.t2.config(state='readonly')
        self.t4.config(state='readonly')
        self.t5.config(state='normal')

    def answer(self): #check the answer
        testanswer = self.t3.get() #get the answer from the user
        try:
           int(testanswer) == testanswer #check if the answer is a number
        except ValueError:
            self.t4.config(state='normal')
            self.t4.delete(0, 'end')
            self.t4.insert(END, 'Please enter a number')
            self.t4.config(state='readonly')
            return
        answer=int(self.t3.get()) #get the answer from the user
        testval1 = int(self.t1.get()) #these are the numbers that the user is being tested on
        testval2 = int(self.t2.get()) #these are the numbers that the user is being tested on
        operator = self.combobox.get() #get the operator
        name = self.t5.get() #get the name
        expression = str(testval1) + str(operator) + str(testval2) #create the equation based on user input
        result= eval(expression) #evaluate the equation
        if result==answer: #if the answer is correct
            self.t4.config(state='normal') #make the result box editable
            self.t4.delete(0, 'end') #clear the result box
            self.t4.insert(END, 'Correct') #insert the result
            self.t4.config(state='readonly') #make the result box read only again
            with open('logs.csv', 'a', newline='') as csvfile: #writes the name and the correct answer to a csv file
                writer = csv.writer(csvfile)
                writer.writerow([name, expression, answer, 'Correct'])
        else: #if the answer is incorrect
            self.t4.config(state='normal') #make the result box editable
            self.t4.delete(0, 'end') #clear the result box
            self.t4.insert(END, 'Incorrect') #insert the result
            self.t4.config(state='readonly') #make the result box read only again
            with open('logs.csv', 'a', newline='') as csvfile: #writes the name and the incorrect answer to a csv file
                writer = csv.writer(csvfile)
                writer.writerow([name, expression, answer, 'Incorrect'])


window=Tk()
mywin=MyWindow(window)
window.config(bg="#3655ff")
window.title('Williams Math Game')
window.geometry("420x480+100+100") #the sizeing of the window
window.mainloop()