from tkinter import *

def red():
    canvas1.create_oval(120,120,50,50,fill = 'red',outline = 'gray',width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)

def yellow():
    canvas1.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'yellow',outline = 'gray',width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)

def green():
    canvas1.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'white',outline = 'gray',width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'green',outline = 'gray',width = 4)



ps = Tk()
ps.geometry("600x600")
ps.title("traffic control")
ps.configure(bg = "black")

button1= Button(ps,text ='RED',bg = 'gray',font = ('arial',15),width = 12,height = 1,command =red).grid(row = 1,column  = 1)
canvas1= Canvas(ps,height = 130,bg = 'black').grid(row = 1,column = 2)

button2= Button(ps,text ='YELLOW',bg = 'gray',font = ('arial',15),width = 12,height = 1,command =yellow).grid(row = 2,column  = 1)
canvas2= Canvas(ps,height = 130,bg = 'black').grid(row = 2,column = 2)

button3= Button(ps,text ='GREEN',bg = 'gray',font = ('arial',15),width = 12,height = 1,command =green).grid(row = 3,column  = 1)
canvas3= Canvas(ps,height = 130,bg = 'black').grid(row = 3,column = 2)

ps.mainloop()






