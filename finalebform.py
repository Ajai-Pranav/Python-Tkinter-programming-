# Import Module
from tkinter import *
from PIL import Image, ImageTk

# Create Tkinter Object
root = Tk()
root.geometry('900x700')
# Read the Image
image = Image.open("Tamil_Nadu_Electricity_Board_(emblem).jpg")
# Resize the image using resize() method
resize_image = image.resize((200,170))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.place(x=50,y=20)
# Execute Tkinter
l=Label(root,text="Welcome to TNEB",fg='black',font=('Times New Roman',30),bg='white')
l.place(x=350,y=50)

l=Label(root,text="Choose Your Plan",fg='black',font=('Times New Roman',25),bg='white')
l.place(x=370,y=140)


##########
def home():
    def cals():
        a=int(txta.get())
        b=int(txtb.get())
        amt=0
        c=b-a
        if(c<100):
            amt=0#localvariable
        elif(c>100 and c<=500):
            amt=(c-100)*2
        elif(c>500):
            amt=((c-100)*5)
        amt=((amt*20)/100)+amt    
        txtd.insert(0,str(c))    
        txtc.insert(0,str(amt))
        
    la=Label(root,text="Enter the EBline Number",fg="red",font=("tahoma",12))
    la.place(x=450,y=350)

    txt1=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txt1.place(x=640,y=350)

    la=Label(root,text="Enter the Previous unit",fg="red",font=("tahoma",12))
    la.place(x=10,y=350)

    txta=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txta.place(x=200,y=350)

    lb=Label(root,text="Enter the Current unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=400)

    txtb=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtb.place(x=200,y=400)
###
    lb=Label(root,text="Net unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=500)

    lb=Label(root,text="Net amount Payable",fg="red",font=("tahoma",12))
    lb.place(x=10,y=550)
    
    txtd=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtd.place(x=200,y=500)
    txtc=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtc.place(x=200,y=550)
    cc=Button(root,text="Calculate",command=cals)
    cc.place(x=200,y=450)
###
def com():
    def cals():
        a=int(txta.get())
        b=int(txtb.get())
        amt=0
        c=b-a
        if(c<100):
            amt=c*9
        elif(c>100 and c<=500):
            amt=c*15
        elif(c>500):
               amt=c*20
        amt=((amt*20)/100)+amt       
        txtd.insert(0,str(c))    
        txtc.insert(0,str(amt))

    la=Label(root,text="Enter the EBline Number",fg="red",font=("tahoma",12))
    la.place(x=450,y=350)

    txt1=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txt1.place(x=640,y=350)    
        
    la=Label(root,text="Enter the Previous unit",fg="red",font=("tahoma",12))
    la.place(x=10,y=350)

    txta=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txta.place(x=200,y=350)

    lb=Label(root,text="Enter the Current unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=400)

    txtb=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtb.place(x=200,y=400)
###
    lb=Label(root,text="Net unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=500)

    lb=Label(root,text="Net amount Payable",fg="red",font=("tahoma",12))
    lb.place(x=10,y=550)
    
    txtd=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtd.place(x=200,y=500)
    txtc=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtc.place(x=200,y=550)
    cc=Button(root,text="Calculate",command=cals)
    cc.place(x=200,y=450)

###
def ind():
    def cals():
        a=int(txta.get())
        b=int(txtb.get())
        amt=0
        c=b-a
        if(c<100):
            amt=c*5
        elif(c>100 and c<=500):
            amt=c*10
        elif(c>500):
               amt=c*15
        amt=((amt*20)/100)+amt
        txtd.insert(0,str(c))    
        txtc.insert(0,str(amt))

    la=Label(root,text="Enter the EBline Number",fg="red",font=("tahoma",12))
    la.place(x=450,y=350)

    txt1=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txt1.place(x=640,y=350)
    
    la=Label(root,text="Enter the Previous unit",fg="red",font=("tahoma",12))
    la.place(x=10,y=350)

    txta=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txta.place(x=200,y=350)

    lb=Label(root,text="Enter the Current unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=400)

    txtb=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtb.place(x=200,y=400)
###
    lb=Label(root,text="Net unit",fg="red",font=("tahoma",12))
    lb.place(x=10,y=500)

    lb=Label(root,text="Net amount Payable",fg="red",font=("tahoma",12))
    lb.place(x=10,y=550)
    
    txtd=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtd.place(x=200,y=500)
    txtc=Entry(root,text="",bd=1,fg="blue",font=("tahoma",12))
    txtc.place(x=200,y=550)
    cc=Button(root,text="Calculate",command=cals)
    cc.place(x=200,y=450)

###
image1 = Image.open("homee.png")
resize_image1 = image1.resize((60,60))
img1 = ImageTk.PhotoImage(resize_image1)
label1 = Label(image=img1)
label1.place(x=200,y=230)
# button adding
h=Button(root,text="Home",command=home)
h.place(x=200,y=290)

##########
image2 = Image.open("store.png")
resize_image2 = image2.resize((60,60))
img2 = ImageTk.PhotoImage(resize_image2)
label1 = Label(image=img2)
label1.place(x=400,y=230)
# button adding
h=Button(root,text="Commercial",command=com)
h.place(x=400,y=290)

##########
image3 = Image.open("Industry.png")
resize_image3 = image3.resize((60,60))
img3 = ImageTk.PhotoImage(resize_image3)
label1 = Label(image=img3)
label1.place(x=600,y=230)
# button adding
h=Button(root,text="Industry",command=ind)
h.place(x=600,y=290)

root.mainloop()

