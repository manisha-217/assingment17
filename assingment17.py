#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
root=Tk()
label=Label(root,text="hello world",width=30,font=120,bg='green',fg='black')
label.pack()
b=Button(root,text="exit",width=30,bg='blue',fg='red',command=exit)
b.pack()
root.mainloop()
#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
def display():
    label=Label(root1,text="hello world",width=30)
    label.pack()
root1=Tk()
label=Label(root1,text="hello world",width=30,font=120,bg='green',fg='black')
label.pack()
b=Button(root1,text="exit",width=30,bg='blue',fg='red',command=exit)
b.pack()
b2 = Button(root1,text="click!",command=display)
b2.pack()
root1.mainloop()
#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
import tkinter
from tkinter import *
def display():
    label.config(text="hello java")
main=Tk()
f1=Frame(main)
f1.pack()
label=Label(f1,text="hello india",width=20)
label.pack()

b1=Button(f1,text="exit",width=40,command=exit)
b1.pack()
b2=Button(f1,text="change",width=25,command=display)
b2.pack()
main.mainloop()
#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
import tkinter
from tkinter import *
def show():
    print(entry.get())
root=Tk()
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text='click',width=20,command=show)
b.pack()
