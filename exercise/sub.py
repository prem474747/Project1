from tkinter import *
def sub():
    number_1 = number1.get()
    number_2 = number2.get()
    result = int(number_1) - int(number_2)
    label3.configure(text = "result : %d"%result)

pr = Tk()
pr.geometry("600x600")
pr.title("game")
pr.configure(bg="green")
label1 = Label(pr,text = "number 1 : ",bg = "red",fg = "white",font = "bold").grid(row = 1, column = 1)
number1 = StringVar()
entry1 = Entry(pr,textvariable = number1,bg = "blue",fg = "white",font = "bold").grid(row = 1, column = 2)
label2 = Label(pr,text = "number 2 : ",bg = "red",fg = "white",font = "bold").grid(row = 2, column = 1)
number2 = StringVar()
entry2 = Entry(pr,textvariable = number2,bg = "blue",fg =  "white",font = "bold").grid(row = 2, column = 2)
Button = Button(pr,text = "SUB",command = sub,bg = "green",fg = "white",font = "italic").grid(row = 4, column = 2)
label3 = Label(pr,bg = "green",fg = "white",font = ("calibri",15))
label3.grid(row = 5, column = 4)
pr.mainloop()