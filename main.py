from tkinter import * #import tkinter
from tkinter import ttk #import ttk
import random #import random
import operator #import operator for eval
import csv #import csv for writing to csv file
import time #import time for time stamp
class MyWindow:  #create class
    def __init__(self, win): #create the window
        self.lbl1=Label(win, text='Your Answer:') #where the answer is put by the user
        self.lbl2=Label(win, text='Result:') #where the program tells the user if they are correct or not
        self.lbl5=Label(win, text='Your Name:') #where the user puts their name
        self.t1=Entry(state='readonly' , bd=3) #the first number
        self.t2=Entry(state='readonly', bd=3) #the second number
        self.t3=Entry( bd=3) #where the user puts their answer
        self.t4=Entry(state='readonly', bd=3) #where the program tells the user if they are correct or not
        self.t5=Entry(state='readonly', bd=3) #where the user enters their name
        self.t1.place(x=50, y=50) #place the first number
        self.t2.place(x=250, y=50) #place the second number
        self.b1=Button(win, text='Submit', command=self.answer) #submit button
        self.b2=Button(win, text='New Question', command=self.generate) #new question button
        self.b1.place(x=280, y=150) #submit button
        self.b2.place(x=100, y=150) #new question button
        self.lbl1.place(x=100, y=200) #label for the answer box
        self.t3.place(x=200, y=200) #answer box
        self.lbl2.place(x=100, y=250) #label for the result box
        self.t4.place(x=200, y=250) #result box
        self.lbl5.place(x=100, y=300) #label for the name box
        self.t5.place(x=200, y=300) #name box
        operators = ["+", "-", "*",] #the operators that can be used
        self.combobox = ttk.Combobox(win, values=operators, width=1) #create the combobox
        self.combobox.set(operators[0]) #set the default operator
        self.combobox.place(x=200, y=50) #place the combobox
        self.t5.config(state='normal') #make the name box editable
    def generate(self): #generate the numbers
        self.t1.config(state='normal') #allow editing of the number boxes
        self.t2.config(state='normal') #allow editing of the number boxes
        self.t4.config(state='normal') #allow editing of the result box
        self.t1.delete(0, 'end') #clear the number boxes
        self.t2.delete(0, 'end') #clear the number boxes
        self.t4.delete(0, 'end')  #clear the result box
        num1=random.randint(1, 10) #generate random numbers
        num2=random.randint(1, 10) #generate random numbers
        if num1 < num2: #make sure the first number is bigger than the second
            num1 = num1 + num2
        self.t1.insert(END, str(num1)) #insert the numbers into the boxes
        self.t2.insert(END, str(num2)) #insert the numbers into the boxes
        self.t1.config(state='readonly') #make the boxes read only again
        self.t2.config(state='readonly') #make the boxes read only again
        self.t4.config(state='readonly') #make the boxes read only again
        self.t5.config(state='normal') #make the name box editable

    def answer(self): #check the answer and tell the user if they are correct or not
        testanswer = self.t3.get() #get the answer from the user and store it in a variable
        try: #try to do the following
           int(testanswer) == testanswer #check if the answer is a number or not
        except ValueError: #if the answer is not a number
            self.t4.config(state='normal') #make the result box editable
            self.t4.delete(0, 'end') #clear the result box
            self.t4.insert(END, 'Please enter a number')  #tell the user to enter a number
            self.t4.config(state='readonly') #make the result box read only again
            return #stop the function
        answer=int(self.t3.get()) #get the answer from the user and store it in a variable
        testval1 = int(self.t1.get()) #these are the numbers that the user is being tested on
        testval2 = int(self.t2.get()) #these are the numbers that the user is being tested on
        operator = self.combobox.get() #get the operator from the combobox
        name = self.t5.get() #get the name from the name box
        timenow = time.strftime("%D:%H:%M:%S") #get the time and date
        expression = str(testval1) + str(operator) + str(testval2) #create the equation based on user input and the numbers
        result= eval(expression) #evaluate the equation and store the result in a variable
        if result==answer: #if the answer is correct
            self.t4.config(state='normal') #make the result box editable
            self.t4.delete(0, 'end') #clear the result box
            self.t4.insert(END, 'Correct') #insert the result
            self.t4.config(state='readonly') #make the result box read only again
            with open('logs.csv', 'a', newline='') as csvfile: #writes the name and the correct answer to a csv file
                writer = csv.writer(csvfile) #create the writer
                writer.writerow([timenow, name, expression, answer, 'Correct']) #write the data to the csv file
        else: #if the answer is incorrect
            self.t4.config(state='normal') #make the result box editable
            self.t4.delete(0, 'end') #clear the result box
            self.t4.insert(END, 'Incorrect') #insert the result
            self.t4.config(state='readonly') #make the result box read only again
            with open('logs.csv', 'a', newline='') as csvfile: #writes the name and the incorrect answer to a csv file
                writer = csv.writer(csvfile) #create the writer
                writer.writerow([timenow, name, expression, answer, 'Incorrect']) #write the data to the csv file


window=Tk() #create the window
mywin=MyWindow(window) #create the window
window.config(bg="#3655ff") #set the background colour
window.title('Williams Math Game') #set the title of the window
window.geometry("420x480+100+100") #the sizeing of the window and the inital position on the screen
window.mainloop() #run the window