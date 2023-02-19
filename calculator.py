from tkinter import *

# root definition
root = Tk()
root.title("Calculator")
root.geometry("263x370")

# screen entry 
entry  = Entry(root,width=40,borderwidth=5,)
entry.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

# add button
def add_button():
    first_number = entry.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    entry.delete(0,END)
# sub button
def sub_button():
    first_number = entry.get()
    global f_num
    global math
    math = "sub"
    f_num = float(first_number)
    entry.delete(0,END)


#equal button
def equal():
    secon_num = float(entry.get())
    entry.delete(0,END)
    
    if math == "add":
        sum=f_num+secon_num
        entry.insert(0,sum)
    elif math == "sub":
        dif = f_num-secon_num
        entry.insert(0,dif)
    elif math == "div":
        quo = f_num/secon_num
        entry.insert(0,quo)
    elif math == "mul":
        pro = f_num*secon_num
        entry.insert(0,pro)

#clear button
def clear():
    entry.delete(0,END)
 
# button click
def buttonClick(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))
# delete function
def deleteButton():
    current = entry.get()
    newVal = current[0:len(current)-1]
    entry.delete(0,END)
    entry.insert(0,newVal)
# div function
def div_button():
    first_number = entry.get()
    global f_num
    global math
    math = "div"
    f_num = float(first_number)
    entry.delete(0,END)
# mul function 
def mul_button():
    first_number = entry.get()
    global f_num
    global math
    math = "mul"
    f_num = float(first_number)
    entry.delete(0,END)


# define button for numbers
button1=Button(root,text=1,padx=30,pady=15,command=lambda: buttonClick(1))
button2=Button(root,text=2,padx=30,pady=15,command=lambda: buttonClick(2)) 
button3=Button(root,text=3,padx=30,pady=15,command=lambda: buttonClick(3))
button4=Button(root,text=4,padx=30,pady=15,command=lambda: buttonClick(4))
button5=Button(root,text=5,padx=30,pady=15,command=lambda: buttonClick(5))
button6=Button(root,text=6,padx=30,pady=15,command=lambda: buttonClick(6))
button7=Button(root,text=7,padx=30,pady=15,command=lambda: buttonClick(7))
button8=Button(root,text=8,padx=30,pady=15,command=lambda: buttonClick(8))
button9=Button(root,text=9,padx=30,pady=15,command=lambda: buttonClick(9))
button0=Button(root,text=0,padx=30,pady=15,command=lambda: buttonClick(0))
# special signs
button_dot =Button(root,text=".", padx=30,pady=15, command=lambda  : buttonClick('.'))
button_c=Button(root,text="clear",padx=20,pady=15,command=clear)
button_equal=Button(root,text="=",padx=30,pady=15,command=equal)
button_del=Button(root,text="<--",padx=24,pady=15,command=deleteButton)
button_plus=Button(root,text="+",padx=30,pady=15,command=add_button)
button_sub=Button(root,text="-",padx=30,pady=15,command=sub_button)
button_div=Button(root,text="/",padx=30,pady=15,command=div_button)
button_mul=Button(root,text="x",padx=30,pady=15,command=mul_button)

# first row placement
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

# second row placement
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)

# third row placement
button1.grid(row=5,column=0)
button2.grid(row=5,column=1)
button3.grid(row=5,column=2)
# fourth row button
button0.grid(row=6,column=0)
button_dot.grid(row=6,column=1)
button_sub.grid(row=6,column=2)
# fifth row
button_plus.grid(row=7,column=0)
button_div.grid(row=7,column=1)
button_mul.grid(row=7,column=2)
# sixth row
button_del.grid(row=8,column=0)
button_c.grid(row=8,column=1)
button_equal.grid(row=8,column=2)
root.mainloop()