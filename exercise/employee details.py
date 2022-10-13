from sqlite3 import Cursor
import tkinter.messagebox
from tkinter import *
from turtle import update
import MySQLdb

from playstation.models import prem


db = MySQLdb.connect(host = 'localhost', password= 'Root@1234',user='root',db='prem')
Cursor=db.cursor()

pk = Tk()
pk.geometry("600x600")
pk.title("access control matrix")
pk.configure(bg='lightblue')

def add():
    first1= first.get()
    last2 = last.get()
    member = prem(firstname=first, lastname=last)
    member.save()

firstname_label = Label(pk,text = 'first name',bg="blue",fg =  "white",font = "bold")
firstname_label.place(x=100,y=100)
first = StringVar()
firstname_entry = Entry(pk,textvariable ='first',bg='red',fg = "white",font = "bold").place(x=200,y=100)
lastname_label = Label(pk,text = 'last name',bg="blue",fg="white",font = "bold")
lastname_label.place(x = 100,y=200)
last = StringVar()
lastname_entry = Entry(pk,textvariable ='first',bg='red',fg = "white",font = "bold").place(x=200,y=200)
update_but = Button(pk,text ='add',bg='black',fg='white',font = "arial",command="add").place(x = 350,y=250)

pk.mainloop()