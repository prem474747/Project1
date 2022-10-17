from tkinter import *

homepage = Tk()
homepage.title('Home')
homepage = Canvas(homepage,width=450,height=450)
homepage.pack()
image = PhotoImage(
    file='/home/vignesh/Downloads/PNG_transparency_demonstration_1.png')
homepage.create_image(0, 0, anchor=NW, image=image)
# Button(homepage,text='django',background='gray',fg='white').grid()
homepage.mainloop()