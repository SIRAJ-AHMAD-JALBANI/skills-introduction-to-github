from tkinter import *

window = Tk()

photo = PhotoImage(file='image.png') 

label = Label(window,
              text="bro do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top'
              )
#label.place(x=100,y=100)

label.pack()

window.mainloop()