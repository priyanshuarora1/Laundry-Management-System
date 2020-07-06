from tkinter import*
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox
import backend
from datetime import date
from datetime import timedelta
import smtplib, ssl

s=Tk()
s.title("LAUNDRY MANAGEMENT SYSTEM")
s.geometry('1350x1890+0+0')
s.configure(background='pink')


building=StringVar()
ref=StringVar()
socks=StringVar()
display=StringVar()
hanky=StringVar()
ug=StringVar()
pant=StringVar()
shirt=StringVar()
expdate=StringVar()
other=StringVar()
blanket=StringVar()
shorts=StringVar()
bs=StringVar()
pc=StringVar()
shirt=StringVar()
patientnhsno=StringVar()
name=StringVar()
dates=StringVar()
dates.set(date.today())
delivery=StringVar()
delivery.set(date.today()+timedelta(days=3))
room=StringVar()
total=StringVar()
email=StringVar()
mainframe=Frame(s)
mainframe.grid()
#--------------------------------------functions--------------------------

def add():
    a=int(socks.get())+int(hanky.get())+int(ug.get())+int(pant.get())+int(other.get())+int(blanket.get())+int(shorts.get())+int(bs.get())+int(pc.get())+int(shirt.get())
    total.set(a)
    
    
def iexit():
    iexit=tkinter.messagebox.askyesno("Laundry Management System","Confirm if you want to exit")
    if iexit>0:
        s.destroy()
        return
        
def idelete():
    building.set("")
    ref.set("")
    socks.set("")
    display.set("")
    hanky.set("")
    ug.set("")
    pant.set("")
    shirt.set("")
    expdate.set("")
    other.set("")
    blanket.set("")
    shorts.set("")
    total.set("")
    bs.set("")
    pc.set("")
    shirt.set("")
    patientnhsno.set("")
    name.set("")
    room.set("")
    email.set("")
    s.txtprescription.delete("1.0",END)
    s.txtframedetail.delete("1.0",END)

def ireset():
    building.set("")
    ref.set("")
    socks.set("")
    display.set("")
    hanky.set("")
    ug.set("")
    pant.set("")
    shirt.set("")
    expdate.set("")
    other.set("")
    blanket.set("")
    shorts.set("")
    total.set("")
    bs.set("")
    pc.set("")
    shirt.set("")
    patientnhsno.set("")
    name.set("")
    room.set("")
    email.set("")
    s.txtdisplay.delete("1.0",END)



    
def idisplay():
    s.txtframedetail.insert(END,"\t"+ref.get()+"\t" +"\t"+"     "+ total.get() +"\t"+"\t"+"  "+ building.get()  +"\t"+"\t"+"    "+ room.get() +"\t"+"\t"+"             "+ dates.get() +"\t"+"\t"+"\t" + delivery.get() + "\t"+"\t"+"     "+ s.txtprescription.get("1.0",END) + "\n")
    backend.addrecord(ref.get(),total.get(),building.get(),room.get(),dates.get(),delivery.get())
    
    cont=ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.ehlo()
        server.starttls(context=cont)
        server.ehlo()
        msg='Congratulations Mr/Mrs. ' + name.get() + "  , your clothes are being sucessfully recieved on  "+ str(date.today()) + ". \n For any washing instruction you can contact to 6397895859 . You can pick your clothes from the laundry on " + str(date.today()+timedelta(days=3)) +". \n THANK YOU HOPE YOU WILL NOT BE DISAPPOINTED."
        server.login('xxxxxx@gmail.com','password')
        message='Subject:{}\n\n{}'.format('YOUR CLOTHES ARE SUCESSFULLY RECIEVED', msg)
        server.sendmail('laundryabes@gmail.com',email.get(),message)

    return

#-------------------------------------------------------------------------------------------------------- 

titleframe=Frame(mainframe, bd=10, width=1350, padx=20 ,relief=RIDGE)
titleframe.pack(side=TOP)

s.lbtitle=Label(titleframe, font=('arial',40,'bold'),text="LAUNDRY MANAGEMENT SYSTEM",padx=2 )
s.lbtitle.grid()


framedetail=Frame(mainframe,bd=20,width=1350,height=130,padx=20,relief=RIDGE)
framedetail.pack(side=BOTTOM)


buttondetail=Frame(mainframe,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
buttondetail.pack(side=BOTTOM)

datadetail=Frame(mainframe,bd=20,width=1150,height=400,padx=60,relief=RIDGE)
datadetail.pack(side=LEFT)


datadetailleft=LabelFrame(datadetail,bd=10,width=800,height=400,padx=20,relief=RIDGE, font=('arial',12,'bold'),text='details',)
datadetailleft.pack(side=LEFT)


datadetailright=LabelFrame(datadetail,bd=10,width=450,height=400,padx=20,relief=RIDGE, font=('arial',12,'bold'),text='Washing Instructions',)
datadetailright.pack(side=RIGHT)

s.lbltablet=Label(datadetailleft, font=('arial',12,'bold'),text="Building Name",padx=2 )
s.lbltablet.grid(row=0,column=0,sticky=W)

s.building=ttk.Combobox(datadetailleft,textvariable=building,state='readonly',font=('arial',12,'bold'),width=18)
s.building['value']=('','VKB','CKB','ABB','DNB','VDB','FR')
s.building.grid(row=0,column=1)

s.lblroom=Label(datadetailleft, font=('arial',12,'bold'),text="room number",padx=2 )
s.lblroom.grid(row=0,column=2,sticky=W)
s.txtroom=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=room)
s.txtroom.grid(row=0,column=3)

s.lblref=Label(datadetailleft, font=('arial',12,'bold'),text="laundary number",padx=2 )
s.lblref.grid(row=1,column=0,sticky=W)
s.txtref=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=ref)
s.txtref.grid(row=1,column=1)


s.lblname=Label(datadetailleft, font=('arial',12,'bold'),text="name",padx=2 )
s.lblname.grid(row=1,column=2,sticky=W)
s.txtname=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=name)
s.txtname.grid(row=1,column=3)

s.lblbs=Label(datadetailleft, font=('arial',12,'bold'),text="bed sheet",padx=2 )
s.lblbs.grid(row=2,column=0,sticky=W)
s.txtbs=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=bs)
s.txtbs.grid(row=2,column=1)

s.lblpc=Label(datadetailleft, font=('arial',12,'bold'),text="pillow cover",padx=2 )
s.lblpc.grid(row=2,column=2,sticky=W)
s.txtpc=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=pc)
s.txtpc.grid(row=2,column=3)


s.lblshirt=Label(datadetailleft, font=('arial',12,'bold'),text="Shirts/T-shirts",padx=2 )
s.lblshirt.grid(row=3,column=0,sticky=W)
s.txtshirt=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=shirt)
s.txtshirt.grid(row=3,column=1)

s.lblpant=Label(datadetailleft, font=('arial',12,'bold'),text="pant/jeans",padx=2 )
s.lblpant.grid(row=3,column=2,sticky=W)
s.txtpant=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=pant)
s.txtpant.grid(row=3,column=3)

s.lblhanky=Label(datadetailleft, font=('arial',12,'bold'),text="hanky",padx=2 )
s.lblhanky.grid(row=4,column=0,sticky=W)
s.txthanky=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=hanky)
s.txthanky.grid(row=4,column=1)


s.lblstorage=Label(datadetailleft, font=('arial',12,'bold'),text="shorts/pyjamas",padx=2 )
s.lblstorage.grid(row=4,column=2,sticky=W)
s.txtstorage=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=shorts)
s.txtstorage.grid(row=4,column=3)

s.lblsocks=Label(datadetailleft, font=('arial',12,'bold'),text="socks",padx=2 )
s.lblsocks.grid(row=5,column=0,sticky=W)
s.txtsocks=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=socks)
s.txtsocks.grid(row=5,column=1)


s.lblo=Label(datadetailleft, font=('arial',12,'bold'),text="other",padx=2 )
s.lblo.grid(row=5,column=2,sticky=W)
s.txto=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=other)
s.txto.grid(row=5,column=3)



s.lblug=Label(datadetailleft, font=('arial',12,'bold'),text="under garments",padx=2 )
s.lblug.grid(row=7,column=0,sticky=W)
s.txtug=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=ug)
s.txtug.grid(row=7,column=1)


s.lblquantity=Label(datadetailleft, font=('arial',12,'bold'),text="blanket",padx=2 )
s.lblquantity.grid(row=7,column=2,sticky=W)
s.txtquantity=Entry(datadetailleft,font=('arial',12,'bold'), textvariable=blanket)
s.txtquantity.grid(row=7,column=3)


s.lbldate=Label(datadetailleft, font=('arial',12,'bold'),text="date",padx=2 )
s.lbldate.grid(row=8,column=0,sticky=W)
s.txtdate=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=dates)
s.txtdate.grid(row=8,column=1)

s.lbldatedel=Label(datadetailleft, font=('arial',12,'bold'),text="date of delivery",padx=2 )
s.lbldatedel.grid(row=8,column=2,sticky=W)
s.txtdatedel=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=delivery)
s.txtdatedel.grid(row=8,column=3)

s.lblemail=Label(datadetailleft, font=('arial',12,'bold'),text="E-mail",padx=2 )
s.lblemail.grid(row=9,column=0,sticky=W)
s.txtemail=Entry(datadetailleft,font=('arial',12,'bold'),textvariable=email)
s.txtemail.grid(row=9,column=1)


s.txttotal=Entry(datadetailleft,font=('arial',12,'bold'), textvariable=total)
s.txttotal.grid(row=9,column=3)



#-------------------------------------------frames-----------------------------------------

s.txtprescription=Text(datadetailright,font=('arial',12,'bold'),width=43,height=14,padx=2,pady=4 )
s.txtprescription.grid(row=0,column=0)


#------------------------------------------buttons----------------------------------------

s.btndisplay=Button(buttondetail,text='Display',font=('arial',12,'bold'),width=24,bd=4,command=idisplay)
s.btndisplay.grid(row=0,column=0)

s.btntotal=Button(datadetailleft,text='total',font=('arial',12,'bold'),width=10,bd=4,command=add)
s.btntotal.grid(row=9,column=2)

s.btndelete=Button(buttondetail,text='delete',font=('arial',12,'bold'),width=24,bd=4,command=idelete)
s.btndelete.grid(row=0,column=2)

s.btnreset=Button(buttondetail,text='reset',font=('arial',12,'bold'),width=24,bd=4,command=ireset)
s.btnreset.grid(row=0,column=3)

s.btnexit=Button(buttondetail,text='exit',font=('arial',12,'bold'),width=24,bd=4,command=iexit)
s.btnexit.grid(row=0,column=4)


#------------------------------------down frame ------------------------------
s.lbllabel=Label(framedetail,font=('arial',12,'bold'),pady=8,text="   Laundry Number\t\tQuantity\t\tBuilding\t\tRoom Number\t\tDate\t\tDelivery Date\t   Any washing instructions\t\t",)
s.lbllabel.grid(row=0,column=0)
s.txtframedetail=Text(framedetail,font=('arial',12,'bold'),width=141,height=5,padx=2,pady=2) 
s.txtframedetail.grid(row=1,column=0)
s.mainloop()

    
