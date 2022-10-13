from tkinter import *
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(
    host='localhost', password='Root@1234', user='root', db='prem')
cursor = db.cursor()


def admin():
    global admin_frame
    global admin_username
    global admin_password
    admin_frame = Frame(homepage)
    admin_frame.pack()
    admin_username = StringVar()
    admin_password = StringVar()
    Label(admin_frame, text='username', font=('Arial', 13)).pack()
    Entry(admin_frame, textvariable=admin_username, font=('Arial', 13)).pack()
    Label(admin_frame, text='password', font=('Arial', 13)).pack()
    Entry(admin_frame, textvariable=admin_password, font=('Arial', 13)).pack()
    Button(admin_frame, text='login', font=('Arial', 13)).pack()


def userlogin():
    username = user_username.get()
    password = user_password.get()
    cursor.execute(
        'SELECT * FROM details where username=%s and password=%s', [username, password])
    a = cursor.fetchone()
    if a != None:
        tkinter.messagebox.showinfo('Authenticate', 'Welcome to user')
    else:
        tkinter.messagebox.showinfo('Authenticate', 'invalid user')


def user():
    global user_frame
    global user_username
    global user_password
    user_frame = Frame(homepage)
    user_frame.pack()
    user_username = StringVar()
    user_password = StringVar()
    Label(user_frame, text='username', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=user_username, font=('Arial',)).pack()
    Label(user_frame, text='password', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=user_password, font=('Arial', 13)).pack()
    Button(user_frame, text='login', command=userlogin, font=(
        'Arial,13'), bg='gray', fg='white', width='10', height='1').pack()
    Button(user_frame, text='signup', command=register, font=(
        'Arial', 13), bg='gray', fg='white', width='10', height='1').pack()


def register():
    global register_frame
    global register_name
    global register_mail
    global register_address
    global register_gender
    global register_username
    global register_password
    register_frame = Frame(homepage)
    register_frame.pack()
    register_name = StringVar()
    register_mail = StringVar()
    register_address = StringVar()
    register_gender = StringVar()
    register_username = StringVar()
    register_password = StringVar()
    Label(user_frame, text='NAME', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=register_name, font=('Arial',)).pack()
    Label(user_frame, text='MAIL', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=register_mail, font=('Arial', 13)).pack()
    Label(user_frame, text='ADDRESS', font=('Arial,13')).pack()
    Entry(user_frame, textvariable=register_address, font=('Arial',)).pack()
    Label(user_frame, text='gender', font=('Arial', 13)).pack()
    Radiobutton(user_frame, text='MALE', variable=register_gender,
                value='MALE', font=('Arial', 13)).pack()
    Radiobutton(user_frame, text='FEMALE', variable=register_gender,
                value='FEMALE', font=('Arial', 13)).pack()
    Label(user_frame, text='USERNAME', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=register_username, font=('Arial',)).pack()
    Label(user_frame, text='PASSWORD', font=('Arial', 13)).pack()
    Entry(user_frame, textvariable=register_password, font=('Arial', 13)).pack()
    Button(user_frame, text='submit', command=storedata, font=(
        'Arial', 13), bg='gray', fg='white', width='10', height='1').pack()


def storedata():
    name = register_name.get()
    mail = register_mail.get()
    address = register_address.get()
    gender = register_gender.get()
    username = register_username.get()
    password = register_password.get()
    cursor.execute('insert into details(name,mail,gender,address,username,password) values(%s,%s,%s,%s,%s,%s)', [
                   name, mail, gender, address, username, password])
    db.commit()
    notify.config(text='Registered Successfully')


def mainpage():
    global homepage
    global notify
    homepage = Tk()
    homepage.geometry('1200x700')
    homepage.title('Authenticate')
    homepage.configure(bg='lightblue')
    button1 = Button(homepage, text='Admin', command=admin, font=(
        'Arial', 15, 'bold'), bg='gray', fg='white', width='13', height='1').pack()
    button2 = Button(homepage, text='User', command=user, font=(
        'Arial', 15, 'bold'), bg='gray', fg='white', width='13', height='1').pack()
    notify = Label(homepage, font=('Arial', 15, 'bold'), fg='red')
    notify.place(x=100, y=400)
    homepage.mainloop()


mainpage()
