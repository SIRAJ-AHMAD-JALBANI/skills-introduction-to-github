from tkinter import *
# tkinter module has been imported successfully

window = Tk()
#instantiated
window.geometry("420x420")
window.title("Calculator")
window.config(background='blue')

icon = PhotoImage(file='logo3.png')
window.iconphoto(True,icon)
window.mainloop()
