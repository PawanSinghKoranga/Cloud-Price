from threading import main_thread
from pip import main
import frontpg as fpg
import asyncio
import sys
import subprocess
# from colobj import *


from tkinter import*
# root = Tk()
# root.geometry("655x333")
# Label(root,text=f"The value of username is {fpg.lowval}").pack()


# import asyncio
from objs import obj1
from objs import obj2
from objs import obj3
from objs import obj4

global counter
counter=0



class servers:
    pass

list=[]


def addtolist(ccval,ctype,cdescription,cprovider,url):
    obj=servers()
    obj.val=ccval
    obj.type=ctype
    obj.description=cdescription
    obj.provider=cprovider
    obj.link=url
    list.append(obj)



def upd(v1,v2,v3,v4,v5):
    list[v5].val=v1
    list[v5].type=v2
    list[v5].description=v3
    list[v5].provider=v4


async def updlist():

    while(1):
        print("we are inside updlist")
        upd(obj1.ccval,obj1.ctype,obj1.cdescription,obj1.cprovider,0)
        upd(obj2.ccval,obj2.ctype,obj2.cdescription,obj2.cprovider,1)
        upd(obj3.ccval,obj3.ctype,obj3.cdescription,obj3.cprovider,2)
        upd(obj4.ccval,obj4.ctype,obj4.cdescription,obj4.cprovider,3)
        print("length of list initially")
        global counter
        counter+=1
        print(len(list))
        await asyncio.sleep(10)


def homeb():
     subprocess.Popen(['python', 'frontpg2.py'])
     sys.exit(0)
          

async def showdat():
    
    
    # while(1):

        # from tkinter import*
    root = Tk()
    root.geometry("655x333")
    root.attributes('-fullscreen', True)
    home_button = Button(root, text="Home", command=homeb)
    home_button.pack(pady=20)
    Label(root,text=f"The value of username is {fpg.lowval}").pack()
    Label(root,text=f"counter='{counter}").pack()
    if(fpg.typec==1):
        for t in list:
            if(t.type=="storage" and t.val<=fpg.upval and t.val>=fpg.lowval):
                Label(root,text=f"{t.type}, {t.val}").pack()

       
    root.after(10000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    root.mainloop()
        





async def main():
    if(fpg.exitval==1):
        sys.exit(0)
    
    
    task1=asyncio.create_task(obj1.fetch_data())
    task2=asyncio.create_task(obj2.fetch_data())
    task3=asyncio.create_task(obj3.fetch_data())
    task4=asyncio.create_task(obj4.fetch_data())
    await asyncio.sleep(2)

    addtolist(obj1.ccval,obj1.ctype,obj1.cdescription,obj1.cprovider,obj1.url)
    addtolist(obj2.ccval,obj2.ctype,obj2.cdescription,obj2.cprovider,obj2.url)
    addtolist(obj3.ccval,obj3.ctype,obj3.cdescription,obj3.cprovider,obj3.url)
    addtolist(obj4.ccval,obj4.ctype,obj4.cdescription,obj4.cprovider,obj4.url)

    
        
    
        # print(obj1.ccval)


    taskupd=asyncio.create_task(updlist())

    for te in range(4):
        print(list[te].val)

    print(len(list))
    
    while(1):
        taskshow=asyncio.create_task(showdat())
        await asyncio.sleep(0.5)


    # Label(root,text=f"counter='{counter}").pack()
    # if(fpg.typec==1):
    #     for t in list:
    #         if(t.type=="storage" and t.val<=fpg.upval and t.val>=fpg.lowval):
    #             Label(root,text=f"{t.type}, {t.val}").pack()

    # # def refresh():
    # #     try:
    # #         # label['text'] = next(strit)
    # #         root.after(1000, refresh)
    # #     except StopIteration:
    # #         root.destroy()

    # # root.after(1000, refresh)
    # # root.mainloop()
    # root.after(4000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    # root.mainloop()

    

    

    # print(list[0].description)
    # print(list[0].val)
        
    # print(list[1].description)
    # print(list[1].val)
        
    # print(list[2].description)
    # print(list[2].val)
        
    # print(list[3].description)
    # print(list[3].val)
        
    


    
   
    


asyncio.run(main())


# if __name__ == "__main__":
#     print(obj1.ccval)
#     print(obj2.ccval)
    

#     print("we are here again")

#     asyncio.run(main()) 
#     for te in range(4):
#         print(list[te].val)

#     print(len(list))


#     Label(root,text=f"counter='{counter}").pack()
#     if(fpg.typec==1):
#         for t in list:
#             if(t.type=="storage" and t.val<=fpg.upval and t.val>=fpg.lowval):
#                 Label(root,text=f"{t.type}, {t.val}").pack()

#     def refresh():
#         try:
#             # label['text'] = next(strit)
#             root.after(1000, refresh)
#         except StopIteration:
#             root.destroy()

#     root.after(1000, refresh)
#     root.mainloop() 
            
#     # root.mainloop()
            

