from tkinter import *
root=Tk()
root.geometry("1000x1000")
f1=Frame(root)
l1=Label (f1,text="SRM INFOTECH COMPUTER EDUCATION", bg="red", fg="yellow", bd="10", font=("bold",24))
l1.pack()
l2=Label (f1,text="ISO:9001-2015 CERTIFIED INSTITUTION", bg="red", fg="white", bd="10", font=("regular",15))
l2.pack()
f1.pack(fill="both")
f1.config(bg="grey")

f2=Frame(root)
l11=Label (f2,text="Register Number", bg="pink", fg="black", bd="10", font=("regular",12))
l11.pack()
a1=Entry()
a1.pack()
f2.pack(fill="both")
f2.config(bg="pink")


root.mainloop()