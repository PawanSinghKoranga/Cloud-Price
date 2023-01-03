import asyncio
from objs import obj1
from objs import obj2
from objs import obj3
from objs import obj4




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
        upd(obj1.ccval,obj1.ctype,obj1.cdescription,obj1.cprovider,0)
        upd(obj2.ccval,obj2.ctype,obj2.cdescription,obj2.cprovider,1)
        upd(obj3.ccval,obj3.ctype,obj3.cdescription,obj3.cprovider,2)
        upd(obj4.ccval,obj4.ctype,obj4.cdescription,obj4.cprovider,3)
        print("length of list initially")
        print(len(list))
        await asyncio.sleep(2)

        




async def main():
    task1=asyncio.create_task(obj1.fetch_data())
    task2=asyncio.create_task(obj2.fetch_data())
    task3=asyncio.create_task(obj3.fetch_data())
    task4=asyncio.create_task(obj4.fetch_data())
     
    await asyncio.sleep(2)

    # print(obj1.ccval)
    addtolist(obj1.ccval,obj1.ctype,obj1.cdescription,obj1.cprovider,obj1.url)
    addtolist(obj2.ccval,obj2.ctype,obj2.cdescription,obj2.cprovider,obj2.url)
    addtolist(obj3.ccval,obj3.ctype,obj3.cdescription,obj3.cprovider,obj3.url)
    addtolist(obj4.ccval,obj4.ctype,obj4.cdescription,obj4.cprovider,obj4.url)


    updlist()

    print(list[0].description)
    print(list[0].val)
    
    print(list[1].description)
    print(list[1].val)
    
    print(list[2].description)
    print(list[2].val)
    
    print(list[3].description)
    print(list[3].val)
    


    
   
    
asyncio.run(main())