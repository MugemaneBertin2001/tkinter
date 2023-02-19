from tkinter import *
window = Tk()
window.config(bg="green")
window.title("My program")

def myclick():
    e=Entry(window,width=50)
    e.pack()

# lables
Button1 = Button(window,  text="Hello world", command=myclick)
Button2 = Button(window,  text="Hello world in long sentence")

Button1.pack()
Button2.pack()

window.mainloop()