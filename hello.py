from tkinter import *
window = Tk()
window.config(bg="green")
window.title("My program")

# lables
label1 = Label(window,  text="Hello world")
label2 = Label(window,  text="Hello world in long sentence")

label1.grid(row=0, column=0, rowspan=3,columnspan=3)
label2.grid(row=6, column=0, rowspan=3,columnspan=3)

window.mainloop()