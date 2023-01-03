import string
import os
from threading import main_thread
from pip import main
import frontpg as fpg
import asyncio
import sys
import subprocess
import numpy as np
from tkinter import ttk
 
 


from tkinter import*


global counter
counter=0



class servers:
    pass

# list=[[float],["a"],["b"],["c"],["d"]]*4
list = np.array([(0.0,'a','b','c','d')]*21,
       dtype=[('var', np.float64),('type', (np.str_, 100)), ('description', (np.str_, 1000)),('provider', (np.str_, 100)),('link', (np.str_, 100)) ])




async def updlist():

    while(1):
        # for i in range(2):
        f=open("./subpro/obj1con.txt","r")
        lst=f.readlines()
        list[0][0]=float(lst[0])
        list[0][1]=lst[1].strip()
        list[0][2]=lst[2].strip()
        list[0][3]=lst[3].strip()
        list[0][4]=lst[4].strip()

        f=open("./subpro/obj2con.txt","r")
        lst=f.readlines()
        list[1][0]=float(lst[0])
        list[1][1]=lst[1].strip()
        list[1][2]=lst[2].strip()
        list[1][3]=lst[3].strip()
        list[1][4]=lst[4].strip()

        f=open("./subpro/obj3con.txt","r")
        lst=f.readlines()
        list[2][0]=float(lst[0])
        list[2][1]=lst[1].strip()
        list[2][2]=lst[2].strip()
        list[2][3]=lst[3].strip()
        list[2][4]=lst[4].strip()

        f=open("./subpro/obj4con.txt","r")
        lst=f.readlines()
        list[3][0]=float(lst[0])
        list[3][1]=lst[1].strip()
        list[3][2]=lst[2].strip()
        list[3][3]=lst[3].strip()
        list[3][4]=lst[4].strip()

        f=open("./subpro/obj5con.txt","r")
        lst=f.readlines()
        list[4][0]=float(lst[0])
        list[4][1]=lst[1].strip()
        list[4][2]=lst[2].strip()
        list[4][3]=lst[3].strip()
        list[4][4]=lst[4].strip()

        f=open("./subpro/obj6con.txt","r")
        lst=f.readlines()
        list[5][0]=float(lst[0])
        list[5][1]=lst[1].strip()
        list[5][2]=lst[2].strip()
        list[5][3]=lst[3].strip()
        list[5][4]=lst[4].strip()

        f=open("./subpro/obj7con.txt","r")
        lst=f.readlines()
        list[6][0]=float(lst[0])
        list[6][1]=lst[1].strip()
        list[6][2]=lst[2].strip()
        list[6][3]=lst[3].strip()
        list[6][4]=lst[4].strip()

        f=open("./subpro/obj8con.txt","r")
        lst=f.readlines()
        list[7][0]=float(lst[0])
        list[7][1]=lst[1].strip()
        list[7][2]=lst[2].strip()
        list[7][3]=lst[3].strip()
        list[7][4]=lst[4].strip()

        f=open("./subpro/obj9con.txt","r")
        lst=f.readlines()
        list[8][0]=float(lst[0])
        list[8][1]=lst[1].strip()
        list[8][2]=lst[2].strip()
        list[8][3]=lst[3].strip()
        list[8][4]=lst[4].strip()

        f=open("./subpro/obj10con.txt","r")
        lst=f.readlines()
        list[9][0]=float(lst[0])
        list[9][1]=lst[1].strip()
        list[9][2]=lst[2].strip()
        list[9][3]=lst[3].strip()
        list[9][4]=lst[4].strip()

        f=open("./subpro/obj11con.txt","r")
        lst=f.readlines()
        list[10][0]=float(lst[0])
        list[10][1]=lst[1].strip()
        list[10][2]=lst[2].strip()
        list[10][3]=lst[3].strip()
        list[10][4]=lst[4].strip()

        f=open("./subpro/obj12con.txt","r")
        lst=f.readlines()
        list[11][0]=float(lst[0])
        list[11][1]=lst[1].strip()
        list[11][2]=lst[2].strip()
        list[11][3]=lst[3].strip()
        list[11][4]=lst[4].strip()

        f=open("./subpro/obj13con.txt","r")
        lst=f.readlines()
        list[12][0]=float(lst[0])
        list[12][1]=lst[1].strip()
        list[12][2]=lst[2].strip()
        list[12][3]=lst[3].strip()
        list[12][4]=lst[4].strip()

        f=open("./subpro/obj14con.txt","r")
        lst=f.readlines()
        list[13][0]=float(lst[0])
        list[13][1]=lst[1].strip()
        list[13][2]=lst[2].strip()
        list[13][3]=lst[3].strip()
        list[13][4]=lst[4].strip()

        f=open("./subpro/obj15con.txt","r")
        lst=f.readlines()
        list[14][0]=float(lst[0])
        list[14][1]=lst[1].strip()
        list[14][2]=lst[2].strip()
        list[14][3]=lst[3].strip()
        list[14][4]=lst[4].strip()

        f=open("./subpro/obj16con.txt","r")
        lst=f.readlines()
        list[15][0]=float(lst[0])
        list[15][1]=lst[1].strip()
        list[15][2]=lst[2].strip()
        list[15][3]=lst[3].strip()
        list[15][4]=lst[4].strip()

        f=open("./subpro/obj17con.txt","r")
        lst=f.readlines()
        list[16][0]=float(lst[0])
        list[16][1]=lst[1].strip()
        list[16][2]=lst[2].strip()
        list[16][3]=lst[3].strip()
        list[16][4]=lst[4].strip()

        f=open("./subpro/obj18con.txt","r")
        lst=f.readlines()
        list[17][0]=float(lst[0])
        list[17][1]=lst[1].strip()
        list[17][2]=lst[2].strip()
        list[17][3]=lst[3].strip()
        list[17][4]=lst[4].strip()

        f=open("./subpro/obj19con.txt","r")
        lst=f.readlines()
        list[18][0]=float(lst[0])
        list[18][1]=lst[1].strip()
        list[18][2]=lst[2].strip()
        list[18][3]=lst[3].strip()
        list[18][4]=lst[4].strip()

        f=open("./subpro/obj20con.txt","r")
        lst=f.readlines()
        list[19][0]=float(lst[0])
        list[19][1]=lst[1].strip()
        list[19][2]=lst[2].strip()
        list[19][3]=lst[3].strip()
        list[19][4]=lst[4].strip()

        f=open("./subpro/obj21con.txt","r")
        lst=f.readlines()
        list[20][0]=float(lst[0])
        list[20][1]=lst[1].strip()
        list[20][2]=lst[2].strip()
        list[20][3]=lst[3].strip()
        list[20][4]=lst[4].strip()



        global counter
        counter+=1
        print(len(list))
        await asyncio.sleep(10)


def homeb():
     subprocess.Popen(['python', 'Frontpage2.py'])
    #  p=subprocess.Popen("./launch_all.py")
    #  p.terminate("./launch_all.py")
    #  os.system("TASKKILL /F /IM subpro1.py")
    #  os.system("TASKKILL /F /IM subpro2.py")
    #  os.system("TASKKILL /F /IM subpro3.py")
    #  os.system("TASKKILL /F /IM subpro4.py")
    #  os.system("TASKKILL /F /IM subpro5.py")
    #  os.system("TASKKILL /F /IM subpro6.py")
    #  os.system("TASKKILL /F /IM subpro7.py")
    #  os.system("TASKKILL /F /IM subpro8.py")
    #  os.system("TASKKILL /F /IM subpro9.py")
    #  os.system("TASKKILL /F /IM subpro10.py")
    #  os.system("TASKKILL /F /IM subpro11.py")
    #  os.system("TASKKILL /F /IM subpro12.py")
    #  os.system("TASKKILL /F /IM subpro13.py")
    #  os.system("TASKKILL /F /IM subpro14.py")
    #  os.system("TASKKILL /F /IM subpro15.py")
    #  os.system("TASKKILL /F /IM subpro16.py")
    #  os.system("TASKKILL /F /IM subpro17.py")

     sys.exit(0)
          
# the_widget.configure(wrap="word")
async def showdat():
    
    
    # while(1):

        # from tkinter import*
    root = Tk()
    root.geometry("1200x600+190+130")
    root.overrideredirect(True)
    # root.attributes('-fullscreen', True)
    # home_button = Button(root, text="Home", command=homeb)
    # home_button.grid(row=0,column=1)
    # home_button.place(x=0,y=0)
    # Label(root,text=f"The value of username is {fpg.lowval}").pack()
    # Label(root,text=f"counter='{list[0][0]}").pack()
    # Create A Main Frame

    root.configure(background='black')
    root.attributes('-alpha',0.97)


    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    home_button = Button(second_frame, text="Home", command=homeb,bg="black",fg='white')
    home_button.grid(row=0,column=0)

    main_frame.configure(background='black')
    # my_scrollbar.configure(background='black')
    my_canvas.configure(background='black')
    second_frame.configure(background='black')
    # second_frame.attributes('-alpha',0.97)

    # text.config(font=('Helvatical bold',20))
    Label(second_frame,text=f"Provider",bd=1,wraplength=500,font="lucida 25 bold",bg="black",fg="white").grid(row=1,column=1)
    Label(second_frame,text=f"                                  ",wraplength=500,bg="black",fg="white").grid(row=1,column=2)
    Label(second_frame,text=f"Type",bd=1,wraplength=500,font="lucida 25 bold",bg="black",fg="white").grid(row=1,column=3)
    Label(second_frame,text=f"                                  ",wraplength=500,bg="black",fg="white").grid(row=1,column=4)
    Label(second_frame,text=f"Price\n(INR)",bd=1,wraplength=500,font="lucida 25 bold",bg="black",fg="white").grid(row=1,column=5)
    Label(second_frame,text=f"                  ",wraplength=500,bg="black",fg="white").grid(row=1,column=6)
    Label(second_frame,text=f"Description",bd=1,wraplength=500,font="lucida 25 bold",bg="black",fg="white").grid(row=1,column=7)

    # if(fpg.typec==1):
    #     yaxis=10
    ct=0
    for t in range(len(list)):
        # print(t[0])
        print("above is t1")
        print("upval=")
        print(fpg.upval)
        print(fpg.lowval)
        print(list[t][1])
        print(list[t][0])
        # yaxis=10

            
        # if(list[t][1]=="storage" and list[t][0]<=fpg.upval and list[t][0]>=fpg.lowval):
        # if((((list[t][1]=="storage") and (fpg.var.get()==2))or((list[t][1]=="computation") and (fpg.var.get()==1))) and (list[t][0]<=fpg.upval and list[t][0]>=fpg.lowval)and((fpg.Checkbutton5==True)or(list[t][3]=="AWS" and fpg.Checkbutton1==True)or(list[t][3]=="Azure" and fpg.Checkbutton2==True)or(list[t][3]=="Google" and fpg.Checkbutton3==True)or(list[t][3]=="Icedrive" and fpg.Checkbutton4==True))):
        if(((fpg.var.get()==1 and list[t][1]=="computation")or(fpg.var.get()==2 and list[t][1]=="storage"))and(list[t][0]<=fpg.upval and list[t][0]>=fpg.lowval)and((fpg.Checkbutton5.get()==True)or(list[t][3]=="AWS" and fpg.Checkbutton1.get()==True)or(list[t][3]=="Azure" and fpg.Checkbutton2.get()==True)or(list[t][3]=="Google" and fpg.Checkbutton3.get()==True)or(list[t][3]=="Icedrive" and fpg.Checkbutton4.get()==True))):
        # if((fpg.Checkbutton2.get()==True and list[t][3]=="Azure")or(fpg.Checkbutton1.get()==True and list[t][3]=="AWS")):
        # if(fpg.Checkbutton1 and list[t][3]=="AWS"):
        # if(True):
            ct+=1
            print("we are inside here in this loop")
            # Label(root,text=f"{t+1}").pack()
            # Label(second_frame,text=f"{list[t][3]}",font="lucida 19 bold",justify=LEFT,padx=14,bg="black",fg="white").grid(row=t,column=1)
            # Label(second_frame,text=f"{list[t][1]}",font="lucida 19 bold",justify=LEFT,padx=14,bg="black",fg="white").grid(row=t,column=2)
            # Label(second_frame,text=f"{list[t][0]}",font="lucida 19 bold",justify=LEFT,padx=14,bg="black",fg="white").grid(row=t,column=3)
            # Label(second_frame,text=f"{list[t][2]}",font="lucida 19 bold",justify=LEFT,padx=14,bg="black",fg="white").grid(row=t,column=4)
            print(list[t][2])

            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=1)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=2)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=3)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=4)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=5)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=6)
            Label(second_frame,text=f"",bg="black",fg="white").grid(row=ct*2+1,column=7)

                
            Label(second_frame,text=f"{list[t][3]}",bd=1,relief="sunken",wraplength=500,font=("Courier", 20),bg="black",fg="white").grid(row=(ct+1)*2,column=1)
            Label(second_frame,text=f"                                  ",wraplength=500,bg="black",fg="white").grid(row=t,column=2)
            Label(second_frame,text=f"{list[t][1]}",bd=1,relief="sunken",wraplength=500,font=("Courier", 20),bg="black",fg="white").grid(row=(ct+1)*2,column=3)
            Label(second_frame,text=f"                                  ",wraplength=500,bg="black",fg="white").grid(row=t,column=4)
            Label(second_frame,text=f"{list[t][0]}",bd=1,relief="sunken",wraplength=500,font=("Courier", 20),bg="black",fg="white").grid(row=(ct+1)*2,column=5)
            Label(second_frame,text=f"                  ",wraplength=500,bg="black",fg="white").grid(row=t,column=6)
            Label(second_frame,text=f"{list[t][2]}",bd=1,relief="sunken",wraplength=500,font=("Courier", 10),bg="black",fg="white").grid(row=(ct+1)*2,column=7)


       
    root.after(60000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    root.mainloop()
        





async def main():
    if(fpg.exitval==1):
        sys.exit(0)
    

    
        
    
        # print(obj1.ccval)


    taskupd=asyncio.create_task(updlist())

    for te in range(4):
        print(list[te])

    print(len(list))
    
    while(1):
        taskshow=asyncio.create_task(showdat())
        await asyncio.sleep(0.5)


        
    


    
   
    


asyncio.run(main())


