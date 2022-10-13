from tkinter import *
from tkinter import ttk

def func(selected):
    dropmenu2.set_menu(*option2.get(selected))

def func1(selected):
    dropmenu3.set_menu(*option3.get(selected))

play = Tk()
play.geometry('600x600')
play.configure(bg='lightgray')
play.title('dd list')

label1 =Label(play,text = 'select the BIKE',font = ('arial',13,'bold'))
label1.place(x = 50, y = 100)
option1 =['KTM','BAJAJ','TVS','YAMAHA']
dropvar1 = StringVar()
dropmenu1 =ttk.OptionMenu(play,dropvar1,'----select-----',*option1,command = func)
dropmenu1.place(x = 300, y = 100)
label2 = Label(play,text='select the MODEL',font=('arial',13,'bold'))
label2.place(x = 50, y = 250)
option2 = {
    'KTM': ['----select----','DUKE 200','DUKE 250','DUKE 390'],
    'BAJAJ':['----select----','NS 200','DOMINAR 250','N250'],
    'TVS':['----select----','APACHE 160','RTR 200','APACHE 310R'],
    'YAMAHA':['----select----','R15','MT15','FZ']
}
dropvar2 =StringVar()
dropmenu2 =ttk.OptionMenu(play,dropvar2,'----select-----',*option2,command = func1)
dropmenu2.place(x = 300, y = 250)

label3= Label(play,text='select the COLOR',font=('arial',13,'bold'))
label3.place(x = 50, y = 400)
option3= {
    'DUKE 200':['----select----','WHITE','ORANGE'],
    'DUKE 250':['----select----','GREY','GALVANO'],
    'DUKE 390':['----select----','BLACK','SILVER'],
    'N250':['----select----','BLACK','SILVER'],
    'R15':['----select----','CYAN','BLUE'],
    'MT15':['----select----','GREY','YELLOW'],
    'FZ':['----select----','BLACK','MILITARY SHADE'],
    'NS200':['----select----','YELLOW','BLUE'],
    'DOMINAR 250':['----select----','BLACK','GREEN'],
    'APACHE 160':['----select----','RED','GREEN'],
    'RTR 200':['----select----','BROWN','YELLOW'],
    'APACHE 310R':['----select----','RED','GRAY'],
}
dropvar3 =StringVar()
dropmenu3 =ttk.OptionMenu(play,dropvar3,'----select-----')
dropmenu3.place(x = 300, y = 400)

play.mainloop()