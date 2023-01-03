from tkinter import *
from tkSliderWidget import Slider
from asyncio.windows_events import INFINITE
from PIL import ImageTk, Image
import sys
lowval=0
upval=INFINITE
typec=1
def getvals():
    lowup=slider.getValues()
    print(f"The value of lower limit is {lowup[0]}")
    print(f"The value of upper limit is {lowup[1]}")
    print(f"the type of storage we recieved is{var.get()}")
    if(Checkbutton1==True):
        print("below is checkbutton1")
    # print(Checkbutton1)

    global lowval
    global upval,typec
    # lowval=int(lowvalue.get())
    # upval=int(upvalue.get())
    lowval=lowup[0]
    upval=lowup[1]
    typec=var.get()
    root.destroy()
    
exitval=0
def Close():
    sys.exit(0)
    global exitval
    exitval=1
    root.destroy()

root = Tk()
root.geometry("1200x600")
root.overrideredirect(True)
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

# # bg = ImageTk.PhotoImage(Image.open("img1.jpg"))
# bg=PhotoImage(file="img1.png")
# label1 = Label( root, image = bg)
# label1.place(x = 0, y = 0)
image=Image.open("img1.jpg")
photo=ImageTk.PhotoImage(image)
label1=Label(image=photo)
label1.place(x = 0, y = 0)


root.configure(background='black')
root.attributes('-alpha',0.97)




# user = Label(root, text="lower limit")
# password = Label(root, text="upper limit")
# user.grid()
# password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

title_bar=Frame(root,bg="grey",relief="raised",bd=0,height=15,width=1200)
title_bar.pack()
slider = Slider(root, width = 400, height = 60, min_val = 0, max_val = 2, init_lis = [0,1], show_value = True)
# slider.grid(row=8,column=1)
slider.place(x=550,y=100)

# print(lowup)

title_bar.bind("<B1-Motion>",move_app)

# lowvalue = StringVar()
# upvalue = StringVar()

# userentry = Entry(root, textvariable = lowvalue)
# passentry = Entry(root, textvariable = upvalue)

# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)

var=IntVar()
# Label(root,text="choose either computation or storage",font="lucida 19 bold",justify=LEFT,padx=14).grid(row=5,column=1)
Label(root,text="choose either computation or storage",font="lucida 19 bold",justify=LEFT,padx=14,bg="pink",fg="black").place(x=20,y=200)
# radio=Radiobutton(root,text="Computation",value=1,variable=var).grid(row=10,column=1)
radio=Radiobutton(root,text="Computation",value=1,variable=var).place(x=550,y=200)

# radio=Radiobutton(root,text="Storage",value=2,variable=var).grid(row=10,column=2)
radio=Radiobutton(root,text="Storage",value=2,variable=var).place(x=750,y=200)


awslogo=ImageTk.PhotoImage(Image.open("./images/aws_logo.jpg").resize((100,55)))
labelaws=Label(image=awslogo)
labelaws.place(x = 200, y = 400)

azurelogo=ImageTk.PhotoImage(Image.open("./images/azurelogo.jpg").resize((90,55)))
labelazure=Label(image=azurelogo)
labelazure.place(x = 400, y = 400)

googlelogo=ImageTk.PhotoImage(Image.open("./images/googlecloud.jpg").resize((100,55)))
labelgoogle=Label(image=googlelogo)
labelgoogle.place(x = 600, y = 400)

icelogo=ImageTk.PhotoImage(Image.open("./images/icedrivelogo.jpg").resize((120,55)))
labelice=Label(image=icelogo)
labelice.place(x = 800, y = 400)

Checkbutton1 = BooleanVar()
Button1 = Checkbutton(root, text = "AWS", variable = Checkbutton1, onvalue = 1, offvalue = 0,height = 2, width = 10)
Button1.place(x=200, y=350)

Checkbutton2 = BooleanVar()
Button2 = Checkbutton(root, text = "Azure", variable = Checkbutton2, onvalue = 1, offvalue = 0,height = 2, width = 10)
Button2.place(x=400, y=350) 

Checkbutton3 = BooleanVar()
Button3 = Checkbutton(root, text = "Google", variable = Checkbutton3, onvalue = 1, offvalue = 0,height = 2, width = 10)
Button3.place(x=600, y=350) 

Checkbutton4 = BooleanVar()
Button4 = Checkbutton(root, text = "Icedrive", variable = Checkbutton4, onvalue = 1, offvalue = 0,height = 2, width = 10)
Button4.place(x=800, y=350) 

Checkbutton5 = BooleanVar()
Button5 = Checkbutton(root, text = "All available cloud", variable = Checkbutton5, onvalue = 1, offvalue = 0,height = 2, width = 20)
Button5.place(x=1000, y=350) 

Label(root,text="Find Suitable Cloud",font="lucida 19 bold",justify=LEFT,padx=14,bg="black",fg="white").place(x=435,y=20)
Label(root,text="Choose Price Range",font="lucida 19 bold",justify=LEFT,padx=14,bg="pink",fg="black").place(x=20,y=100)
Label(root,text="(INR pgb pm)",font="lucida 19 bold",justify=LEFT,padx=14,bg="pink",fg="black").place(x=965,y=115)
Label(root,text="Choose your preference of cloud",font="lucida 19 bold",justify=LEFT,padx=14,bg="pink",fg="black").place(x=20,y=300)




# Button(text="Submit", command=getvals).grid(row=20,column=0)
Button(text="Submit", command=getvals,bg="black",fg="white").place(x=600,y=520)
exit_button = Button(root, text="Exit", command=Close,bg="black",fg="white")
# exit_button.grid(row=22,column=0,pady=20)
exit_button.place(x=80,y=520)

root.mainloop()
