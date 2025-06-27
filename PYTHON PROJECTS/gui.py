from tkinter import *

# windows = serves as a container to hold or contain the widgets
# widgets = GUI elements: buttons, textboxes, labels, images

window = Tk() 
# instantiate an instance of a window

window.geometry("420x420")
window.title("Bro code first GUI program")

icon = PhotoImage(file='logo3.png')
window.iconphoto(True,icon)

window.config(background="green")

window.mainloop()
# place window on computer screen, listen for events
