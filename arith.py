from tkinter import *
def add():
    a = Text1.get()
    b = Text2.get()
    c = int(a)+int(b)
    Text3.set(c)
    return
def sub():
    a = Text1.get()
    b = Text2.get()
    c = int(a)-int(b)
    Text3.set(c)
    return
def mul():
    a = Text1.get()
    b = Text2.get()
    c = int(a)*int(b)
    Text3.set(c)
    return
def div():
    a = Text1.get()
    b = Text2.get()
    c = int(a)/int(b)
    Text3.set(c)
    return

root=Tk()
root.title("application")
root.geometry("1000x1000")

global Text1, Text2, Text3
Text1 = StringVar()
Text2 = StringVar()
Text3 = StringVar()

f1=Frame(root)
l1=Label (f1,text="ARITHMETIC OPERATER",bg="#0000d3",bd="22" ,width="1000",font=("bold",24),fg="#55ffcc")
l1.pack()
l2=Label (f1,text="Python Tkinter ***Desktop Application***",bg="#8080ff" ,width="1000",font=("bold",13),fg="black",bd="11")
l2.pack()
f1.pack()
f2=Frame(root)
l21=Label (f2,text="NUMBER A",bg="lightgreen")
l21.grid(row=0,column=0,padx="20",pady="20")
a1=Entry(f2,textvariable=Text1)
a1.grid(row=0,column=1,padx="20",pady="20")
l22=Label (f2,text="NUMBER B",bg="lightgreen")
l22.grid(row=1,column=0,padx="20",pady="20")
a2=Entry(f2,textvariable=Text2)
a2.grid(row=1,column=1,padx="20",pady="20")
l23=Label (f2,text="RESULT C",bg="lightyellow")
l23.grid(row=2,column=0,padx="20",pady="20")
a3=Entry(f2,textvariable=Text3)
a3.grid(row=2,column=1,padx="20",pady="20")
f2.pack(fill="both")
f2.config(bg="#ffcc33")
f3=Frame(root)
a31=Button(f3,text="ADD",command=add,bd="20",border="15",bg="#00ffcc")
a31.grid(row="0",column="1",padx="50",pady="50")
a32=Button(f3,text="SUB",command=sub,bd="20",border="15",bg="#00ffcc")
a32.grid(row="0",column="2",padx="50",pady="50")
a33=Button(f3,text="MUL",command=mul,bd="20",border="15",bg="#00ffcc")
a33.grid(row="0",column="3",padx="50",pady="50")
a34=Button(f3,text="DIV",command=div,bd="20",border="15",bg="#00ffcc")
a34.grid(row="0",column="4",padx="50",pady="50")
f3.config(bg="#ff8080")
f3.pack(fill="both")
root.mainloop()
