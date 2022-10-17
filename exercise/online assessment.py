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
    Button(admin_frame, text='login',
           command=adminlogin, font=('Arial', 13)).pack()


def adminlogin():
    username = admin_username.get()
    password = admin_password.get()
    if username == '1' and password == '1':
        tkinter.messagebox.showinfo('Authenticate', 'Welcome Admin')
        adminhome()
    else:
        tkinter.messagebox.showinfo('Authenticate', 'invalid')


def adminhome():
    global adminpage
    adminpage = Toplevel(homepage)
    adminpage.geometry("1300x500")
    adminpage.title("ADMIN HOME")
    adminpage.configure(bg="aqua")
    pending = Button(adminpage, text="pending List", command=pendinglist, font=(
        'aria', 15), bg='gray', fg='white', width='10', height='1')
    pending.grid(row=1, column=1)
    approved = Button(adminpage, text="approved List", command=approvedlist, font=(
        "Arial,15"), bg='gray', fg='white', width='10', height='1')
    approved.grid(row=1, column=2)


def pendinglist():
    global pendingframe
    pendingframe = Frame(adminpage)
    pendingframe.grid()
    cursor.execute('select * from access')
    a = cursor.fetchall()
    Label(pendingframe, text='ID', font=('Arial', 13)).grid(row=4, column=0)
    Label(pendingframe, text='Name', font=('Arial', 13)).grid(row=4, column=1)
    Label(pendingframe, text='Mail', font=('Arial', 13)).grid(row=4, column=2)
    Label(pendingframe, text='gender', font=(
        'Arial', 13)).grid(row=4, column=3)
    Label(pendingframe, text='Address', font=(
        'Arial', 13)).grid(row=4, column=4)
    Label(pendingframe, text='username', font=(
        'Arial', 13)).grid(row=4, column=5)
    Label(pendingframe, text='password', font=(
        'Arial', 13)).grid(row=4, column=6)
    Label(pendingframe, text='status', font=(
        'Arial', 13)).grid(row=4, column=7)

    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(cols):
            s = Entry(pendingframe, font=('Arial', 11))
            s.grid(row=i+5, column=j)
            s.insert(END, a[i][j])
        but1 = Button(pendingframe, text='Approve',
                      command=lambda: approve(a[i][0]))
        but1.grid(row=i+5, column=cols+1)
        but1 = Button(pendingframe, text='Delete',
                      command=lambda: delete(a[i][0]))
        but1.grid(row=i+5, column=cols+2)


def approvedlist():
    global approveframe
    approveframe = Frame(adminpage)
    approveframe.grid()
    cursor.execute('select * from access where')
    a = cursor.fetchall()
    Label(approveframe, text='ID', font=('Arial', 13)).grid(row=4, column=0)
    Label(approveframe, text='Name', font=('Arial', 13)).grid(row=4, column=1)
    Label(approveframe, text='Mail', font=('Arial', 13)).grid(row=4, column=2)
    Label(approveframe, text='gender', font=(
        'Arial', 13)).grid(row=4, column=3)
    Label(approveframe, text='Address', font=(
        'Arial', 13)).grid(row=4, column=4)
    Label(approveframe, text='username', font=(
        'Arial', 13)).grid(row=4, column=5)
    Label(approveframe, text='password', font=(
        'Arial', 13)).grid(row=4, column=6)
    Label(approveframe, text='status', font=(
        'Arial', 13)).grid(row=4, column=7)
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(cols):
            s = Entry(approveframe, font=('calibri', 11))
            s.grid(row=i+5, column=j)
            s.insert(END, a[i][j])


def approve(id):
    cursor.execute('update access set verify = True where id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate', 'Approved')


def delete(id):
    cursor.execute('delete from access where id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate', 'Deleted')


def userlogin():
    username = user_username.get()
    password = user_password.get()
    cursor.execute(
        'SELECT * FROM access where username=%s and password=%s', [username, password])
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
    cursor.execute('insert into access(name,mail,gender,address,username,password) values(%s,%s,%s,%s,%s,%s)', [
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
