from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("Image Viewer")

imagenumber = 0

image1 = ImageTk.PhotoImage(Image.open("./images/1.png"))
image2=ImageTk.PhotoImage(Image.open("./images/2.png"))
image3 = ImageTk.PhotoImage(Image.open("./images/3.jpg"))
image4=ImageTk.PhotoImage(Image.open("./images/4.jpg"))
image5 = ImageTk.PhotoImage(Image.open("./images/5.jpg"))
image6=ImageTk.PhotoImage(Image.open("./images/6.jpg"))
image7 =ImageTk.PhotoImage(Image.open("./images/7.jpg"))
image8=ImageTk.PhotoImage(Image.open("./images/8.jpg"))
image9 = ImageTk.PhotoImage(Image.open("./images/9.jpg"))
image10=ImageTk.PhotoImage(Image.open("./images/10.jpg"))
image11 = ImageTk.PhotoImage(Image.open("./images/11.jpg"))
imag12=ImageTk.PhotoImage(Image.open("./images/12.png"))
image13 = ImageTk.PhotoImage(Image.open("./images/13.png"))
image14=ImageTk.PhotoImage(Image.open("./images/14.jpg"))
image15 = ImageTk.PhotoImage(Image.open("./images/15.jpg"))
image16=ImageTk.PhotoImage(Image.open("./images/16.jpg"))
image17 = ImageTk.PhotoImage(Image.open("./images/17.jpg"))
image18=ImageTk.PhotoImage(Image.open("./images/18.jpg"))
image19 = ImageTk.PhotoImage(Image.open("./images/19.jpg"))
image20=ImageTk.PhotoImage(Image.open("./images/20.jpg"))



# functions
def programClose():
    root.destroy()

def nextImage(image_number):
    global imageLable
    global forWards
    global backWards
    global images
   
    imageLable.grid_forget()
    imageLable = Label(image=images[image_number],width=500,height=500)
    forWards = Button(root,text=">>",command=lambda : nextImage(image_number+1))
    backWards = Button(root,text="<<",command=lambda  : prevImage(image_number-1))
    if image_number == 19:
        forWards = Button(root,text=">>",state=DISABLED)
    imageLable.grid(row=0,column=0,columnspan=3)
    backWards.grid(row=1,column=0)
    forWards.grid(row=1,column=2)

    status = Label(root, text="Image "+str(image_number)+" of "+str(len(images) ),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E,pady=6)
def prevImage(image_number):

    global imageLable
    global forWards
    global backWards
    global images
   
    imageLable.grid_forget()
    imageLable = Label(image=images[image_number],width=500,height=500)
    backWards = Button(root,text="<<",command=lambda  : prevImage(image_number-1))
    forWards = Button(root,text=">>",command=lambda : nextImage(image_number+1))
    if image_number == 0:
        backWards = Button(root,text="<<",state=DISABLED)
    imageLable.grid(row=0,column=0,columnspan=3)
    backWards.grid(row=1,column=0)
    forWards.grid(row=1,column=2)
    status = Label(root, text="Image "+str(image_number)+" of "+str(len(images) ),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E,pady=6)

images=[
    image1,image2,image3,image4,image5,
    image6,image7,image8,image9,image10,
    image11,imag12,image14,image13,image15,
    image16,image17,image18,image19,image20
]
status = Label(root, text="Image 1 of "+str(len(images) ),bd=1,relief=SUNKEN, anchor=E)
imageLable = Label(root,image=images[imagenumber], width=500,height=500)
imageLable.grid(row=0,column=0,columnspan=3)


exitbutt = Button(root,text="Exit Program",command=programClose)
forWards = Button(root,text=">>",command=lambda : nextImage(2))
backWards = Button(root,text="<<",command=lambda  : prevImage(2))

backWards.grid(row=1,column=0,padx=2,pady=2)
exitbutt.grid(row=1,column=1,padx=2,pady=2)
forWards.grid(row=1,column=2,padx=2,pady=2)
status.grid(row=2,column=0,columnspan=3, sticky=W+E,pady=6)
root.mainloop()
