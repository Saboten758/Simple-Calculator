from tkinter import*
root=Tk()

'''
Defining Functions...
'''

def clear():
    result.delete(0,END)
def add():
    clear()
    op1=float(first_val.get())
    op2=float(second_val.get())
    res=op1+op2
    result.insert(2,res)
def sub():
    clear()
    op1=float(first_val.get())
    op2=float(second_val.get())
    res=op1-op2
    result.insert(2,res)
def mult():
    clear()
    op1=float(first_val.get())
    op2=float(second_val.get())
    res=op1*op2
    result.insert(2,res)
def div():
    clear()
    op1=float(first_val.get())
    op2=float(second_val.get())
    res=op1/op2
    result.insert(2,res)
def clear2():
    result.delete(0,END)
    first_val.delete(0,END)
    second_val.delete(0,END)
    
'''
Creating buttons and input boxes...
'''

spacer=Label(root,text=" ")
spacer2=Label(root,text=" ")
spacer3=Label(root,text=" ")
spacer4=Label(root,text=" ")
first_val=Entry(root,width=30,borderwidth=2,bg="white",fg="black")
second_val=Entry(root,width=30,borderwidth=2,bg="white",fg="black")
add_but=Button(root,text="+",padx=40,command=add,fg="red")
sub_but=Button(root,text="-",padx=40,command=sub,fg="red")
mult_but=Button(root,text="x",padx=40,command=mult,fg="red")
div_but=Button(root,text="/",padx=40,command=div,fg="red")
clear2_but=Button(root,text="Clear",padx=40,command=clear2,fg="green")
l1=Label(root,text="First Num:")
l2=Label(root,text="Second Num:")
l3=Label(root,text="Result:")
result=Entry(root,width=40,borderwidth=2,bg="white",fg="black")
l4=Label(root,text="Calculator!")

'''
packing them to root window...
'''

l1.grid(row=0,column=0)
l2.grid(row=2,column=0)
first_val.grid(row=0,column=1)
spacer.grid(row=1,column=0)
second_val.grid(row=2,column=1)
spacer2.grid(row=3,column=0)
add_but.grid(row=4,column=0)
sub_but.grid(row=4,column=2)
l4.grid(row=4,column=1)
clear2_but.grid(row=5,column=1)
mult_but.grid(row=5,column=0)
div_but.grid(row=5,column=2)
spacer4.grid(row=6,column=0)
l3.grid(row=7,column=0)
result.grid(row=7,column=1)

root.mainloop()
