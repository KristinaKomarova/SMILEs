from tkinter import * 
a=""
b=""
c=""
d=""
e=""
f=""
g=""
def lisa_pea():
    global a
    if var_pea.get()=="pea":
        a=ca_.create_oval((50,50,350,350),outline="grey", fill="pink")
    else:
        ca_.delete(a)
def lisa_nina():
    global b
    if var_nina.get()=="nina":
        b=ca_.create_polygon([(200, 220), (250, 200), (350,100)],outline="grey",fill="pink")
    else:
        ca_.delete(b)
def lisa_suu():
     global c
     if var_suu.get()=="suu":
         c=ca_.create_line((200, 250, 90, 215),fill="red",width=2)
     else:
         ca_.delete(c)
def lisa_silm1():
    global d,e
    if var_silm1.get()=="silm1":
        d=ca_.create_oval((72,72,130,150))
        e=ca_.create_oval((82,82,117,120),fill="black")
    else:
        ca_.delete(d,e)
def lisa_silm2():
    global f,g
    if var_silm2.get()=="silm2":
        ca_.create_oval((165,72,221,130))
        ca_.create_oval((175,82,211,120),fill="black")
    else:
        ca_.delete(f,g)
aken = Tk() 
aken.title("okno")
aken.geometry("600x600")
f1=Frame(aken,width=200,height=200)
f1.pack(side=LEFT)
f2=Frame(aken,width=400,height=400)
f2.pack(side=LEFT)
pea=Canvas()
ca_= Canvas(f2, width=400, height=400, bg="violet")
ca_.pack()

var_pea=StringVar()
c_pea=Checkbutton(f1,text="pea",variable=var_pea,onvalue="pea",offvalue="tühi",font="Calibri 26",command=lisa_pea)
c_pea.deselect()
var_nina=StringVar()
c_nina=Checkbutton(f1,text="nina",variable=var_nina,onvalue="nina",offvalue="tühi",font="Calibri 26",command=lisa_nina)
c_nina.deselect()
var_suu=StringVar()
c_suu=Checkbutton(f1,text="suu",variable=var_suu,onvalue="suu",offvalue="tühi",font="Calibri 26",command=lisa_suu)
c_suu.deselect()
var_silm1=StringVar()
c_silm1=Checkbutton(f1,text="silm1",variable=var_silm1,onvalue="silm1",offvalue="tühi",font="Calibri 26",command=lisa_silm1)
c_silm1.deselect()
var_silm2=StringVar()
c_silm2=Checkbutton(f1,text="silm2",variable=var_silm2,onvalue="silm2",offvalue="tühi",font="Calibri 26",command=lisa_silm2)
c_silm2.deselect()
c_pea.pack()
c_nina.pack()
c_suu.pack()
c_silm1.pack()
c_silm2.pack()


aken.mainloop()