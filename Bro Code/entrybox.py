from tkinter import *

# entry widget = textbox that accepts a single line of user input
def submit():
    username= entry.get()
    print("Hello ",username)
window = Tk()

entry = Entry(window,
              font=("Arial",50)
)
entry.pack(side=LEFT)

submit_button = Button(window, text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_= Button(window, text="submit",command=submit)
submit_button.pack(side=RIGHT)

submit_button = Button(window, text="submit",command=submit)
submit_button.pack(side=RIGHT)


window.mainloop()
